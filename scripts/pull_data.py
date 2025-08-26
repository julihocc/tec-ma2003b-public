import argparse
import os
import sys
import shutil
from typing import Optional

from utils import setup_logger


def copy_tree(origin: str, backup: str, dry_run: bool = False) -> None:
    logger = setup_logger("pull_data")
    logger.info(f"Origin: {origin}")
    logger.info(f"Backup: {backup}")

    # Safety: avoid copying the origin into a backup that resides inside the origin
    try:
        origin_abs = os.path.abspath(origin)
        backup_abs = os.path.abspath(backup)
        if os.path.commonpath([backup_abs, origin_abs]) == origin_abs:
            logger.error(
                "Backup path is inside the origin path; aborting to avoid recursion"
            )
            sys.exit(1)
    except Exception:
        # If commonpath check fails for any reason, continue with caution
        pass

    if dry_run:
        logger.info("Dry run enabled; no files will be copied")

    os.makedirs(backup, exist_ok=True)
    logger.info(f"Using backup directory: {backup}")

    for item in os.listdir(origin):
        src = os.path.join(origin, item)
        dst = os.path.join(backup, item)
        if os.path.isdir(src):
            logger.info(f"Copying directory: {src} to {dst}")
            if not dry_run:
                if os.path.exists(dst):
                    shutil.rmtree(dst)
                shutil.copytree(src, dst)
            logger.info(f"Copied directory: {src} -> {dst}")
        else:
            logger.info(f"Copying file: {src} to {dst}")
            if not dry_run:
                shutil.copy2(src, dst)
            logger.info(f"Copied file: {src} -> {dst}")


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Pull course files from a source folder into repo backup"
    )
    parser.add_argument("--origin", "-o", help="Origin folder to copy from")
    parser.add_argument(
        "--backup", "-b", help="Backup folder to copy to (default: ./backup/ma2003b)"
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="List actions without copying files"
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Increase log verbosity"
    )

    args = parser.parse_args(argv)

    # Resolve origin: CLI, env var, or default
    default_origin = os.environ.get("MA2003B_ORIGIN_PATH")

    logger = setup_logger("pull_data")
    logger.info(f"default origin: {default_origin}")
    origin = args.origin or default_origin
    logger.info(f"Using origin: {origin}")

    if origin is None:
        logger.error("No origin path provided via --origin or MA2003B_ORIGIN_PATH")
        return 2

    if not os.path.exists(origin):
        logger.error(f"Origin path does not exist: {origin}")
        return 2

    # Resolve backup
    backup = args.backup or os.path.join(os.getcwd(), "backup", "ma2003b")

    # Adjust logging verbosity
    if args.verbose:
        setup_logger("pull_data", level=10)

    try:
        copy_tree(origin, backup, dry_run=args.dry_run)
    except Exception as e:
        logger = setup_logger("pull_data")
        logger.error(f"Error occurred: {e}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
