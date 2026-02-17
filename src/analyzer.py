import pandas as pd
from .config import GRADUATION_CODES

def separate_academic_levels(df: pd.DataFrame) -> tuple:
    """Separa graduação e pós-graduação."""
    graduation = df[df["TP_GRAU_ACADEMICO"].isin(GRADUATION_CODES)]
    postgraduate = df[~df["TP_GRAU_ACADEMICO"].isin(GRADUATION_CODES)]
    return graduation, postgraduate

def identify_first_course(df: pd.DataFrame) -> pd.Series:
    """Identifica o primeiro curso registrado."""
    return df.sort_values("NU_ANO_CENSO").iloc[0]

def compute_annual_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """Calcula número de cursos e IES por ano."""
    return (
        df.groupby("NU_ANO_CENSO")
        .agg(
            number_of_courses=("NO_CURSO", "nunique"),
            number_of_institutions=("NO_IES", "nunique")
        )
        .reset_index()
        .rename(columns={"NU_ANO_CENSO": "Year"})
    )
