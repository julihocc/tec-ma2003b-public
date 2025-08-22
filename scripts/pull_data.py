import os
import sys
import shutil
from utils import setup_logger

logger = setup_logger("pull_data")

cwd = os.getcwd()
logger.info(f"Current working directory: {cwd}")

# Allow overriding the source path via environment variable for portability
ORIGIN_PATH = os.environ.get(
    "MA2003B_ORIGIN_PATH",
    "/mnt/c/Users/L03071644/OneDrive - Instituto Tecnologico y de Estudios Superiores de Monterrey/Escritorio/202513/Clases/MA2003B",
)

if not os.path.exists(ORIGIN_PATH):
    logger.error(f"Origin path does not exist: {ORIGIN_PATH}")
    sys.exit(1)

logger.info(f"Origin path exists: {ORIGIN_PATH}")

try:
    BACKUP_PATH = os.path.join(os.getcwd(), "backup", "ma2003b")

    # Safety: avoid copying the origin into a backup that resides inside the origin
    try:
        origin_abs = os.path.abspath(ORIGIN_PATH)
        backup_abs = os.path.abspath(BACKUP_PATH)
        if os.path.commonpath([backup_abs, origin_abs]) == origin_abs:
            logger.error(
                "Backup path is inside the origin path; aborting to avoid recursion"
            )
            sys.exit(1)
    except Exception:
        # If commonpath check fails for any reason, continue with caution
        pass

    os.makedirs(BACKUP_PATH, exist_ok=True)
    logger.info(f"Using backup directory: {BACKUP_PATH}")

    for item in os.listdir(ORIGIN_PATH):
        src = os.path.join(ORIGIN_PATH, item)
        dst = os.path.join(BACKUP_PATH, item)
        if os.path.isdir(src):
            logger.info(f"Copying directory: {src} to {dst}")
            if os.path.exists(dst):
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
            logger.info(f"Copied directory: {src} -> {dst}")
        else:
            shutil.copy2(src, dst)
            logger.info(f"Copied file: {src} -> {dst}")

    logger.info("Data pull completed successfully.")
except Exception as e:
    logger.error(f"Error occurred: {e}")
    sys.exit(1)
