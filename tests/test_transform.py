import pandas as pd

from procurement_analytics.transform import (
    MAIN_COLUMNS,
    add_value_eur,
    parse_publication_date,
    parse_value_amount,
    rename_main_columns,
    select_main_columns,
    transform_main_data,
)


def test_select_main_columns() -> None:
    dataframe = pd.DataFrame(
        {
            "id": ["1"],
            "date": ["2024-01-01"],
            "ocid": ["ocds-1"],
            "buyer_id": ["buyer-1"],
            "buyer_name": ["Grad Zagreb"],
            "tender_id": ["tender-1"],
            "tender_mainProcurementCategory": ["goods"],
            "tender_title": ["Nabava opreme"],
            "tender_procurementMethod": ["open"],
            "tender_value_amount": [120000.0],
            "tender_value_currency": ["EUR"],
            "unnecessary_column": ["ne treba nam"],
        }
    )

    result = select_main_columns(dataframe)

    assert list(result.columns) == MAIN_COLUMNS
    assert "unnecessary_column" not in result.columns


def test_rename_main_columns() -> None:
    dataframe = pd.DataFrame(
        {
            "date": ["2024-01-01"],
            "tender_title": ["Nabava opreme"],
            "tender_value_amount": [120000.0],
        }
    )

    result = rename_main_columns(dataframe)

    assert list(result.columns) == [
        "publication_date",
        "title",
        "value_amount",
    ]


def test_parse_publication_date() -> None:
    dataframe = pd.DataFrame(
        {
            "publication_date": [
                "2024-01-15",
                "neispravan datum",
            ]
        }
    )

    result = parse_publication_date(dataframe)

    assert result.loc[0, "publication_date"] == pd.Timestamp("2024-01-15")
    assert pd.isna(result.loc[1, "publication_date"])


def test_parse_value_amount() -> None:
    dataframe = pd.DataFrame(
        {
            "value_amount": [
                "120000.50",
                "neispravan iznos",
            ]
        }
    )

    result = parse_value_amount(dataframe)

    assert result.loc[0, "value_amount"] == 120000.50
    assert pd.isna(result.loc[1, "value_amount"])


def test_transform_main_data() -> None:
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

    result = transform_main_data(dataframe)

    assert result.loc[0, "title"] == "Nabava opreme"
    assert result.loc[0, "value_amount"] == 120000.50
    assert result.loc[0, "publication_date"] == pd.Timestamp("2024-01-15")


def test_add_value_eur() -> None:
    dataframe = pd.DataFrame(
        {
            "value_amount": [100.0, 200.0, 300.0],
            "value_currency": ["EUR", "HRK", None],
        }
    )

    result = add_value_eur(dataframe)

    assert result.loc[0, "value_eur"] == 100.0
    assert pd.isna(result.loc[1, "value_eur"])
    assert pd.isna(result.loc[2, "value_eur"])
