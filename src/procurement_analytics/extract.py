from pathlib import Path

import pandas as pd


def validate_csv_path(csv_path: Path) -> None:
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV datoteke ne postoji: {csv_path}")

    if not csv_path.is_file():
        raise ValueError(f"Putanja nije datoteka: {csv_path}")

    if csv_path.suffix.lower() != ".csv":
        raise ValueError("Datoteka mora imati .csv ekstenziju.")


def load_csv(csv_path: Path) -> pd.DataFrame:
    validate_csv_path(csv_path)

    return pd.read_csv(csv_path)
