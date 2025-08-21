import os
from utils import setup_logger
import shutil

logger = setup_logger("pull_data")

cwd = os.getcwd()
logger.info(f"Current working directory: {cwd}")

ORIGIN_PATH = "/mnt/c/Users/L03071644/OneDrive - Instituto Tecnologico y de Estudios Superiores de Monterrey/Escritorio/202513/Clases/MA2003B"

if not os.path.exists(ORIGIN_PATH):
    raise FileNotFoundError(f"Origin path does not exist: {ORIGIN_PATH}")
else:
    logger.info(f"Origin path exists: {ORIGIN_PATH}")

try:
    BACKUP_PATH = os.path.join(os.getcwd(), "backup", "ma2003b")

    if not os.path.exists(BACKUP_PATH):
        os.makedirs(BACKUP_PATH)
        logger.info(f"Created backup directory: {BACKUP_PATH}")

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