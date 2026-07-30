import json
from collections.abc import Mapping
from pathlib import Path

import pandas as pd


def get_row_count(dataframe: pd.DataFrame) -> int:
    return len(dataframe)


def get_column_count(dataframe: pd.DataFrame) -> int:
    return len(dataframe.columns)


def get_column_names(dataframe: pd.DataFrame) -> list[str]:
    return dataframe.columns.tolist()


def get_column_types(dataframe: pd.DataFrame) -> dict[str, str]:
    return {column: str(dataframe[column].dtype) for column in dataframe.columns}


def get_missing_values(dataframe: pd.DataFrame) -> dict[str, int]:
    missing_values = dataframe.isna().sum()

    return {str(column): int(count) for column, count in missing_values.items()}


def get_unique_value_counts(dataframe: pd.DataFrame) -> dict[str, int]:
    return {
        str(column): int(dataframe[column].nunique(dropna=True))
        for column in dataframe.columns
    }


def get_missing_percentages(dataframe: pd.DataFrame) -> dict[str, float]:
    percentages = dataframe.isna().mean() * 100

    return {
        str(column): round(float(percentage), 2)
        for column, percentage in percentages.items()
    }


def get_duplicate_row_count(dataframe: pd.DataFrame) -> int:
    return int(dataframe.duplicated().sum())


def create_profile_summary(dataframe: pd.DataFrame) -> dict[str, object]:
    return {
        "row_count": get_row_count(dataframe),
        "column_count": get_column_count(dataframe),
        "column_names": get_column_names(dataframe),
        "column_types": get_column_types(dataframe),
        "missing_values": get_missing_values(dataframe),
        "unique_value_counts": get_unique_value_counts(dataframe),
        "missing_percentages": get_missing_percentages(dataframe),
        "duplicate_row_count": get_duplicate_row_count(dataframe),
    }


def save_profile_summary(
    summary: Mapping[str, object],
    output_path: Path,
) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(summary, file, ensure_ascii=False, indent=2)
