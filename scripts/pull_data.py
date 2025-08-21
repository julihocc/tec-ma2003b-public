import os

ORIGIN_PATH = "/mnt/c/Users/L03071644/OneDrive - Instituto Tecnologico y de Estudios Superiores de Monterrey/Escritorio/202513/Clases/MA2003B"

if not os.path.exists(ORIGIN_PATH):
    raise FileNotFoundError(f"Origin path does not exist: {ORIGIN_PATH}")