from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_RAW = BASE_DIR / "data" / "raw"
DATA_INTERIM = BASE_DIR / "data" / "interim"
DATA_PROCESSED = BASE_DIR / "data" / "processed"

OUTPUT_TABLES = BASE_DIR / "outputs" / "tables"
OUTPUT_FIGURES = BASE_DIR / "outputs" / "figures"

AI_PATTERN = r"intelig[eê]ncia artificial"
GRADUATION_CODES = [1, 2, 3]  # Ajustar conforme dicionário INEP
