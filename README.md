# Croatian Public Procurement Analysis

[English](#english) | [Hrvatski](#hrvatski)

---

## English

End-to-end analysis of Croatian public procurement data from 2024 using Python, PostgreSQL, SQL, and Power BI.

### Dataset

Public procurement data for Croatia was downloaded from the Open Contracting Partnership Data Registry.

The analyzed dataset contains:

- 5,924 procurement records
- 1,130 unique buyers
- 4,372 records with an EUR value
- 11 cleaned analytical columns

The complete raw and processed datasets are not included in the repository because of their size.

### Tools

- **Python**
- **pandas** — data loading, profiling, cleaning, and transformation
- **PostgreSQL** — storage of cleaned procurement data
- **SQL** — KPI calculations and analytical queries
- **Power BI** — interactive dashboard
- **pytest** — automated testing

### Data Pipeline

1. Load and validate the raw CSV file
2. Profile columns, missing values, data types, and duplicates
3. Select relevant procurement columns
4. Rename columns into a consistent format
5. Convert publication dates and procurement values
6. Create `value_eur` for EUR-only analysis
7. Export the cleaned dataset
8. Import the data into PostgreSQL
9. Analyze the data with SQL
10. Build the Power BI dashboard

### Key Findings

- Total recorded EUR value is approximately **€13.04 billion**
- Median procurement value is **€377,500**
- Works have the highest total procurement value
- Goods have the highest number of procurement records
- Open procedure is the most common procurement method
- Several very large procurements make the average much higher than the median

### Dashboard

The Power BI dashboard includes:

- Total procurement count
- Procurement records with an EUR value
- Total EUR value
- Median procurement value
- Monthly procurement value
- Procurement value by category
- Top 10 buyers by total value
- Procurement method filter

The Power BI file is available here:

[`powerbi/procurement_dashboard.pbix`](powerbi/procurement_dashboard.pbix)

### SQL Analysis

The SQL scripts are available in:

- [`sql/create_tables.sql`](sql/create_tables.sql)
- [`sql/analysis_queries.sql`](sql/analysis_queries.sql)

### Project Structure

```text
project/
├── data/
│   └── raw/
│       ├── sample.csv
│       └── sample.txt
├── powerbi/
│   └── procurement_dashboard.pbix
├── sql/
│   ├── analysis_queries.sql
│   └── create_tables.sql
├── src/
│   └── procurement_analytics/
│       ├── __init__.py
│       ├── cli.py
│       ├── extract.py
│       ├── pipeline.py
│       ├── profile.py
│       └── transform.py
├── tests/
│   ├── test_extract.py
│   ├── test_pipeline.py
│   ├── test_profile.py
│   └── test_transform.py
├── .gitignore
├── pyproject.toml
├── requirements.txt
└── README.md
```

### Installation

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -e .
```

### Run Tests

```powershell
python -m pytest -v
```

The project currently contains **21 passing tests**.

### CLI Usage

Create a JSON profile of a CSV file:

```powershell
python -m procurement_analytics.cli profile input.csv output.json
```

Create a cleaned CSV file:

```powershell
python -m procurement_analytics.cli clean input.csv output.csv
```

---

## Hrvatski

End-to-end analiza podataka o hrvatskoj javnoj nabavi iz 2024. godine pomoću Pythona, PostgreSQL-a, SQL-a i Power BI-ja.

### Podaci

Podaci o hrvatskoj javnoj nabavi preuzeti su iz Open Contracting Partnership Data Registryja.

Analizirani skup podataka sadrži:

- 5.924 zapisa javne nabave
- 1.130 jedinstvenih naručitelja
- 4.372 zapisa s poznatom EUR vrijednošću
- 11 očišćenih analitičkih stupaca

Cjeloviti izvorni i obrađeni podaci nisu uključeni u repozitorij zbog njihove veličine.

### Alati

- **Python**
- **pandas** — učitavanje, profiliranje, čišćenje i transformacija podataka
- **PostgreSQL** — spremanje očišćenih podataka
- **SQL** — izračun KPI-jeva i analitički upiti
- **Power BI** — interaktivni dashboard
- **pytest** — automatizirano testiranje

### Proces Obrade Podataka

1. Učitavanje i provjera izvornog CSV-a
2. Profiliranje stupaca, praznih vrijednosti, tipova i duplikata
3. Odabir relevantnih stupaca
4. Preimenovanje stupaca u ujednačen format
5. Pretvaranje datuma objave i vrijednosti nabave
6. Izrada stupca `value_eur` za analizu EUR vrijednosti
7. Spremanje očišćenog skupa podataka
8. Uvoz podataka u PostgreSQL
9. Analiza podataka SQL upitima
10. Izrada Power BI dashboarda

### Ključni Nalazi

- Ukupna evidentirana EUR vrijednost iznosi približno **13,04 milijarde €**
- Medijan vrijednosti nabave iznosi **377.500 €**
- Radovi imaju najveću ukupnu vrijednost nabave
- Roba ima najveći broj zapisa
- Otvoreni postupak najčešća je metoda nabave
- Nekoliko vrlo velikih nabava značajno podiže prosjek iznad medijana

### Dashboard

Power BI dashboard prikazuje:

- Ukupan broj nabava
- Broj zapisa s poznatom EUR vrijednošću
- Ukupnu EUR vrijednost
- Medijan vrijednosti nabave
- Mjesečno kretanje vrijednosti
- Vrijednost nabava po kategoriji
- Deset najvećih naručitelja
- Filtar prema metodi nabave

Power BI datoteka dostupna je ovdje:

[`powerbi/procurement_dashboard.pbix`](powerbi/procurement_dashboard.pbix)

### SQL Analiza

SQL skripte nalaze se u:

- [`sql/create_tables.sql`](sql/create_tables.sql)
- [`sql/analysis_queries.sql`](sql/analysis_queries.sql)

### Struktura Projekta

```text
project/
├── data/
│   └── raw/
│       ├── sample.csv
│       └── sample.txt
├── powerbi/
│   └── procurement_dashboard.pbix
├── sql/
│   ├── analysis_queries.sql
│   └── create_tables.sql
├── src/
│   └── procurement_analytics/
│       ├── __init__.py
│       ├── cli.py
│       ├── extract.py
│       ├── pipeline.py
│       ├── profile.py
│       └── transform.py
├── tests/
│   ├── test_extract.py
│   ├── test_pipeline.py
│   ├── test_profile.py
│   └── test_transform.py
├── .gitignore
├── pyproject.toml
├── requirements.txt
└── README.md
```

### Instalacija

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -e .
```

### Pokretanje Testova

```powershell
python -m pytest -v
```

Projekt trenutačno sadrži **21 uspješan test**.

### Korištenje CLI-ja

Izrada JSON profila CSV datoteke:

```powershell
python -m procurement_analytics.cli profile input.csv output.json
```

Izrada očišćene CSV datoteke:

```powershell
python -m procurement_analytics.cli clean input.csv output.csv
```
