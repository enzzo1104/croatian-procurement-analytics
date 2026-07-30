import json
from pathlib import Path

import pandas as pd

from procurement_analytics.pipeline import (
    create_clean_main_csv,
    create_csv_profile,
)


def test_create_csv_profile(tmp_path: Path) -> None:
    input_path = Path("data/raw/sample.csv")
    output_path = tmp_path / "profile_summary.json"

    create_csv_profile(input_path, output_path)

    assert output_path.exists()

    with output_path.open("r", encoding="utf-8") as file:
        summary = json.load(file)

    assert summary["row_count"] == 2
    assert summary["column_count"] == 2


def test_create_clean_main_csv(tmp_path: Path) -> None:
    input_path = tmp_path / "input.csv"
    output_path = tmp_path / "clean.csv"

    dataframe = pd.DataFrame(
        {
            "id": ["1"],
            "date": ["2024-01-15"],
            "ocid": ["ocds-1"],
            "buyer_id": ["buyer-1"],
            "buyer_name": ["Grad Zagreb"],
            "tender_id": ["tender-1"],
            "tender_mainProcurementCategory": ["goods"],
            "tender_title": ["Nabava opreme"],
            "tender_procurementMethod": ["open"],
            "tender_value_amount": ["120000.50"],
            "tender_value_currency": ["EUR"],
        }
    )

    dataframe.to_csv(input_path, index=False)

    create_clean_main_csv(input_path, output_path)

    result = pd.read_csv(output_path)

    assert output_path.exists()
    assert result.loc[0, "title"] == "Nabava opreme"
    assert result.loc[0, "value_amount"] == 120000.50
