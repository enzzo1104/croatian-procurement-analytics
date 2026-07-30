from pathlib import Path

from procurement_analytics.extract import load_csv
from procurement_analytics.profile import (
    create_profile_summary,
    save_profile_summary,
)
from procurement_analytics.transform import transform_main_data


def create_csv_profile(
    input_path: Path,
    output_path: Path,
) -> None:
    dataframe = load_csv(input_path)
    summary = create_profile_summary(dataframe)
    save_profile_summary(summary, output_path)


def create_clean_main_csv(
    input_path: Path,
    output_path: Path,
) -> None:
    dataframe = load_csv(input_path)
    cleaned_dataframe = transform_main_data(dataframe)

    output_path.parent.mkdir(parents=True, exist_ok=True)

    cleaned_dataframe.to_csv(
        output_path,
        index=False,
    )
