import json
from pathlib import Path

import pandas as pd

from procurement_analytics.profile import (
    create_profile_summary,
    get_column_count,
    get_column_names,
    get_column_types,
    get_duplicate_row_count,
    get_missing_percentages,
    get_missing_values,
    get_row_count,
    get_unique_value_counts,
    save_profile_summary,
)


def test_get_row_count() -> None:
    dataframe = pd.DataFrame(
        {
            "buyer": ["Grad Zagreb", "Bolnica"],
            "amount": [120000, 85000],
        }
    )

    assert get_row_count(dataframe) == 2


def test_get_column_count() -> None:
    dataframe = pd.DataFrame(
        {
            "buyer": ["Grad Zagreb", "Bolnica"],
            "amount": [120000, 85000],
        }
    )

    assert get_column_count(dataframe) == 2


def test_get_column_names() -> None:
    dataframe = pd.DataFrame(
        {
            "buyer": ["Grad Zagreb", "Bolnica"],
            "amount": [120000, 85000],
        }
    )

    assert get_column_names(dataframe) == ["buyer", "amount"]


def test_get_column_types() -> None:
    dataframe = pd.DataFrame(
        {
            "buyer": ["Grad Zagreb", "Bolnica"],
            "amount": [120000, 85000],
        }
    )

    assert get_column_types(dataframe) == {
        "buyer": "str",
        "amount": "int64",
    }


def test_get_missing_values() -> None:
    dataframe = pd.DataFrame(
        {
            "buyer": ["Grad Zagreb", None],
            "amount": [120000, 85000],
        }
    )

    assert get_missing_values(dataframe) == {
        "buyer": 1,
        "amount": 0,
    }


def test_get_unique_value_counts() -> None:
    dataframe = pd.DataFrame(
        {
            "buyer": ["Grad Zagreb", "Bolnica", "Bolnica", None],
            "amount": [120000, 85000, 85000, 85000],
        }
    )

    assert get_unique_value_counts(dataframe) == {
        "buyer": 2,
        "amount": 2,
    }


def test_get_missing_percentages() -> None:
    dataframe = pd.DataFrame(
        {
            "buyer": ["Grad Zagreb", None],
            "amount": [120000, 85000],
        }
    )

    assert get_missing_percentages(dataframe) == {
        "buyer": 50.0,
        "amount": 0.0,
    }


def test_get_duplicate_row_count() -> None:
    dataframe = pd.DataFrame(
        {
            "buyer": ["Grad Zagreb", "Bolnica", "Bolnica"],
            "amount": [120000, 85000, 85000],
        }
    )

    assert get_duplicate_row_count(dataframe) == 1


def test_create_profile_summary() -> None:
    dataframe = pd.DataFrame(
        {
            "buyer": ["Grad Zagreb", "Bolnica", "Bolnica"],
            "amount": [120000, 85000, 85000],
        }
    )

    assert create_profile_summary(dataframe) == {
        "row_count": 3,
        "column_count": 2,
        "column_names": ["buyer", "amount"],
        "column_types": {
            "buyer": "str",
            "amount": "int64",
        },
        "missing_values": {
            "buyer": 0,
            "amount": 0,
        },
        "missing_percentages": {
            "buyer": 0.0,
            "amount": 0.0,
        },
        "unique_value_counts": {
            "buyer": 2,
            "amount": 2,
        },
        "duplicate_row_count": 1,
    }


def test_save_profile_summary(tmp_path: Path) -> None:
    summary = {
        "row_count": 2,
        "column_count": 2,
    }

    output_path = tmp_path / "profile_summary.json"

    save_profile_summary(summary, output_path)

    with output_path.open("r", encoding="utf-8") as file:
        saved_summary = json.load(file)

    assert saved_summary == summary
