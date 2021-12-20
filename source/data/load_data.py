""" Modulo de carregamento de dados"""

from typing import List
import pandas as pd
from source.types import ClearDataFnType
from toolz import curry
import numpy as np


def load_from_file(path: str, clear_fn: ClearDataFnType) -> pd.DataFrame:
    """Load Dataset fropm file

    Args:
        path (str): File path
        clear_fn (ClearDataFnType): Clear function

    Returns:
        pd.DataFrame: Dataframe loaded
    """
    df = pd.read_csv(path)
    return clear_fn(df)



@curry
def clear_data(df: pd.DataFrame, column_text: str, column_label: str,
        bins: list = [0, 2, 5], classes: list = [0,1]) -> pd.DataFrame:
    """
    Clear dataframe loaded

    Args:
        df (pd.DataFrame): Dataframe loaded
        column_text (str): Column text
        column_label (str): Column label
        bins (array, optional): Column score. Defaults to [0, 2, 5].
        classes (array, optional): Sentiments classe. Defaults to [0,1].

    Returns:
        pd.DataFrame: Dataframe cleaned
    """
    df = df.dropna(subset=[column_text])
    df['label'] = pd.cut(df[column_label], bins=bins, labels=classes)
    df = df.rename(columns={column_text: 'text'})
    df = df[['text','label']]
    
    return df