import re
import pandas as pd
from .config import AI_PATTERN

def contains_ai_term(course_name: str) -> bool:
    """Verifica se o nome do curso contém 'Inteligência Artificial'."""
    if not isinstance(course_name, str):
        return False
    return bool(re.search(AI_PATTERN, course_name, re.IGNORECASE))

def filter_ai_courses(df: pd.DataFrame) -> pd.DataFrame:
    """Filtra cursos que contêm a expressão alvo."""
    mask = df["NO_CURSO"].apply(contains_ai_term)
    return df[mask].copy()
