import pandas as pd
from pathlib import Path
from typing import List

def list_csv_files(directory: Path) -> List[Path]:
    """Lista todos os arquivos CSV em um diretório."""
    return list(directory.glob("*.csv"))

def load_single_file(filepath: Path) -> pd.DataFrame:
    """Carrega um único arquivo CSV do INEP."""
    df = pd.read_csv(
        filepath,
        sep=";",
        encoding="latin1",
        low_memory=False
    )
    df.columns = df.columns.str.upper()
    return df

def load_historical_series(filepaths: List[Path]) -> pd.DataFrame:
    """Carrega e concatena todos os arquivos da série histórica."""
    dataframes = [load_single_file(fp) for fp in filepaths]
    return pd.concat(dataframes, ignore_index=True)
