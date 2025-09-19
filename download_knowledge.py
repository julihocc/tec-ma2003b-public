#!/usr/bin/env python3
"""
Google Drive Knowledge Base Downloader for MA2003B Course

Downloads all files from a shared Google Drive folder to local knowledge base.
Designed to work with public/shared folders without requiring API authentication.

Usage:
    python download_knowledge.py
    python download_knowledge.py --update  # Only download newer files
    python download_knowledge.py --clean   # Clean download folder first
"""

import os
import sys
import argparse
import logging
from pathlib import Path
from datetime import datetime
import subprocess
import json

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("knowledge/download.log"), logging.StreamHandler()],
)
logger = logging.getLogger(__name__)


class KnowledgeDownloader:
    """Downloads and manages Google Drive knowledge base content."""

    def __init__(self):
        self.script_dir = Path(__file__).parent
        self.knowledge_dir = self.script_dir / "knowledge"
        self.download_dir = self.knowledge_dir / "downloaded"
        self.metadata_file = self.knowledge_dir / "metadata.json"

        # Google Drive folder ID extracted from the shared URL
        # https://drive.google.com/drive/folders/1gTFcVC5-gmfP70kPcfpS629Mm2Z5KT3Q?usp=sharing
        self.folder_id = "1gTFcVC5-gmfP70kPcfpS629Mm2Z5KT3Q"

        # Create directories
        self.knowledge_dir.mkdir(exist_ok=True)
        self.download_dir.mkdir(exist_ok=True)

    def check_dependencies(self):
        """Check if required dependencies are available."""
        try:
            import gdown

            logger.info("✅ gdown library is available")
            return True
        except ImportError:
            logger.error("❌ gdown library not found.")
            logger.info("💡 Installation options:")
            logger.info("   - Using uv: uv add gdown")
            logger.info("   - Using pip: pip install gdown")
            logger.info("   - System package: apt install python3-gdown (if available)")

            # Try to install with uv first (project preference)
            logger.info("Attempting to install gdown with uv...")
            try:
                subprocess.check_call(["uv", "add", "gdown"])
                logger.info("✅ gdown installed successfully with uv")
                return True
            except (subprocess.CalledProcessError, FileNotFoundError):
                logger.warning("⚠️ uv not available or failed, trying pip...")
                try:
                    subprocess.check_call(
                        [sys.executable, "-m", "pip", "install", "gdown", "--user"]
                    )
                    logger.info("✅ gdown installed successfully with pip")
                    return True
                except subprocess.CalledProcessError:
                    logger.error("❌ Failed to install gdown automatically.")
                    logger.error("Please install manually: uv add gdown")
                    return False

    def load_metadata(self):
        """Load existing download metadata."""
        if self.metadata_file.exists():
            try:
                with open(self.metadata_file, "r") as f:
                    return json.load(f)
            except Exception as e:
                logger.warning(f"Could not load metadata: {e}")
        return {"last_download": None, "files": {}, "folder_id": self.folder_id}

    def save_metadata(self, metadata):
        """Save download metadata."""
        metadata["last_download"] = datetime.now().isoformat()
        try:
            with open(self.metadata_file, "w") as f:
                json.dump(metadata, f, indent=2)
            logger.info(f"✅ Metadata saved to {self.metadata_file}")
        except Exception as e:
            logger.error(f"❌ Failed to save metadata: {e}")

    def download_folder(self, clean=False, update_only=False):
        """Download entire Google Drive folder."""
        if not self.check_dependencies():
            return False

        if clean and self.download_dir.exists():
            logger.info("🧹 Cleaning download directory...")
            import shutil

            shutil.rmtree(self.download_dir)
            self.download_dir.mkdir(exist_ok=True)

        metadata = self.load_metadata()

        try:
            import gdown

            # Download the entire folder
            logger.info(f"📥 Downloading Google Drive folder: {self.folder_id}")
            logger.info(f"📁 Target directory: {self.download_dir}")

            # Use gdown to download folder contents
            # Note: This downloads to a subfolder named after the Google Drive folder
            gdown.download_folder(
                id=self.folder_id,
                output=str(self.download_dir),
                quiet=False,
                use_cookies=False,
            )

            # Update metadata
            self.update_file_metadata(metadata)
            self.save_metadata(metadata)

            logger.info("✅ Download completed successfully!")
            self.print_summary()

            return True

        except Exception as e:
            logger.error(f"❌ Download failed: {e}")
            logger.info("💡 Troubleshooting tips:")
            logger.info("   - Ensure the Google Drive folder is publicly shared")
            logger.info("   - Check your internet connection")
            logger.info("   - Try running with --clean flag")
            return False

    def update_file_metadata(self, metadata):
        """Update metadata with information about downloaded files."""
        if not metadata.get("files"):
            metadata["files"] = {}

        # Scan downloaded directory for files
        for file_path in self.download_dir.rglob("*"):
            if file_path.is_file():
                rel_path = file_path.relative_to(self.download_dir)
                file_info = {
                    "size": file_path.stat().st_size,
                    "modified": datetime.fromtimestamp(
                        file_path.stat().st_mtime
                    ).isoformat(),
                    "downloaded": datetime.now().isoformat(),
                }
                metadata["files"][str(rel_path)] = file_info

    def print_summary(self):
        """Print download summary."""
        if not self.download_dir.exists():
            logger.info("📂 No files downloaded yet")
            return

        files = list(self.download_dir.rglob("*"))
        file_count = len([f for f in files if f.is_file()])
        folder_count = len([f for f in files if f.is_dir()])

        total_size = sum(f.stat().st_size for f in files if f.is_file())
        size_mb = total_size / (1024 * 1024)

        logger.info("📊 Download Summary:")
        logger.info(f"   📄 Files: {file_count}")
        logger.info(f"   📁 Folders: {folder_count}")
        logger.info(f"   💾 Total size: {size_mb:.2f} MB")
        logger.info(f"   📍 Location: {self.download_dir}")

    def list_contents(self):
        """List downloaded contents."""
        if not self.download_dir.exists():
            logger.info("📂 Knowledge folder is empty. Run download first.")
            return

        logger.info(f"📋 Contents of {self.download_dir}:")
        for item in sorted(self.download_dir.rglob("*")):
            if item.is_file():
                rel_path = item.relative_to(self.download_dir)
                size_kb = item.stat().st_size / 1024
                logger.info(f"   📄 {rel_path} ({size_kb:.1f} KB)")
            elif item.is_dir() and item != self.download_dir:
                rel_path = item.relative_to(self.download_dir)
                logger.info(f"   📁 {rel_path}/")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Download MA2003B knowledge base from Google Drive"
    )
    parser.add_argument(
        "--clean", action="store_true", help="Clean download folder before downloading"
    )
    parser.add_argument(
        "--update",
        action="store_true",
        help="Only download newer files (not implemented yet)",
    )
    parser.add_argument("--list", action="store_true", help="List downloaded contents")

    args = parser.parse_args()

    downloader = KnowledgeDownloader()

    if args.list:
        downloader.list_contents()
    else:
        success = downloader.download_folder(clean=args.clean, update_only=args.update)
        if not success:
            sys.exit(1)


if __name__ == "__main__":
    main()
