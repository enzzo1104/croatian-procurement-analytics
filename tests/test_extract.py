from pathlib import Path

import pytest

from procurement_analytics.extract import load_csv


def test_load_csv() -> None:
    csv_path = Path("data/raw/sample.csv")

    dataframe = load_csv(csv_path)

    assert len(dataframe) == 2
    assert list(dataframe.columns) == ["buyer", "amount"]


def test_load_csv_raises_error_when_file_does_not_exist() -> None:
    csv_path = Path("data/raw/ne_postoji.csv")

    with pytest.raises(FileNotFoundError):
        load_csv(csv_path)


def test_load_csv_raises_error_when_file_is_not_csv() -> None:
    casv_path = Path("data/raw/sample.txt")

    with pytest.raises(ValueError):
        load_csv(casv_path)
