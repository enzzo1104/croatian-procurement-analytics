import argparse
from pathlib import Path

from procurement_analytics.pipeline import (
    create_clean_main_csv,
    create_csv_profile,
)


def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "action",
        choices=["profile", "clean"],
    )
    parser.add_argument("input_path", type=Path)
    parser.add_argument("output_path", type=Path)

    arguments = parser.parse_args()

    if arguments.action == "profile":
        create_csv_profile(
            arguments.input_path,
            arguments.output_path,
        )
    else:
        create_clean_main_csv(
            arguments.input_path,
            arguments.output_path,
        )


if __name__ == "__main__":
    main()
