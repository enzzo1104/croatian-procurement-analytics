import pandas as pd

MAIN_COLUMNS = [
    "id",
    "date",
    "ocid",
    "buyer_id",
    "buyer_name",
    "tender_id",
    "tender_mainProcurementCategory",
    "tender_title",
    "tender_procurementMethod",
    "tender_value_amount",
    "tender_value_currency",
]

COLUMN_RENAMES = {
    "date": "publication_date",
    "tender_mainProcurementCategory": "procurement_category",
    "tender_title": "title",
    "tender_procurementMethod": "procurement_method",
    "tender_value_amount": "value_amount",
    "tender_value_currency": "value_currency",
}


def select_main_columns(dataframe: pd.DataFrame) -> pd.DataFrame:
    return dataframe[MAIN_COLUMNS].copy()


def rename_main_columns(dataframe: pd.DataFrame) -> pd.DataFrame:
    return dataframe.rename(columns=COLUMN_RENAMES).copy()


def parse_publication_date(dataframe: pd.DataFrame) -> pd.DataFrame:
    result = dataframe.copy()

    result["publication_date"] = pd.to_datetime(
        result["publication_date"],
        errors="coerce",
    )

    return result


def parse_value_amount(dataframe: pd.DataFrame) -> pd.DataFrame:
    result = dataframe.copy()

    result["value_amount"] = pd.to_numeric(
        result["value_amount"],
        errors="coerce",
    )

    return result


def transform_main_data(dataframe: pd.DataFrame) -> pd.DataFrame:
    result = select_main_columns(dataframe)
    result = rename_main_columns(result)
    result = parse_publication_date(result)
    result = parse_value_amount(result)
    result = add_value_eur(result)

    return result


def add_value_eur(dataframe: pd.DataFrame) -> pd.DataFrame:
    result = dataframe.copy()

    result["value_eur"] = result["value_amount"].where(
        result["value_currency"] == "EUR"
    )

    return result
