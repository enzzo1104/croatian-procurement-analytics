# Croatian Public Procurement Analysis

[English](#english) | [Hrvatski](#hrvatski)

![Power BI Dashboard](docs/images/dashboard.png)

---

## English

End-to-end analysis of Croatian public procurement data from 2024 using Python, PostgreSQL, SQL, and Power BI.

### Project overview

This project demonstrates a complete data analysis workflow, from loading and profiling raw CSV data to storing the cleaned dataset in PostgreSQL, analyzing it with SQL, and presenting the results in an interactive Power BI dashboard.

The Python pipeline is separated into smaller modules for data extraction, profiling, transformation, and orchestration. Automated tests are included to verify the main parts of the workflow.

### Dataset

Public procurement data for Croatia was downloaded from the Open Contracting Partnership Data Registry.

The analyzed dataset contains:

- 5,924 procurement records
- 1,130 unique buyers
- 4,372 records with a known EUR value
- 11 cleaned analytical columns
- No duplicate rows in the cleaned dataset

The complete raw and processed datasets are not included in the repository because of their size.

Small sample files are included for testing the pipeline.

### Tools

- **Python** — project logic and command-line interface
- **pandas** — data loading, profiling, cleaning, and transformation
- **PostgreSQL** — storage of cleaned procurement data
- **SQL** — KPI calculations and analytical queries
- **Power BI** — interactive dashboard and visual analysis
- **pytest** — automated testing

### Data pipeline

1. Load and validate the raw CSV file
2. Profile columns, missing values, data types, unique values, and duplicates
3. Select the relevant procurement columns
4. Rename columns into a consistent analytical format
5. Convert publication dates into datetime values
6. Convert procurement amounts into numeric values
7. Create `value_eur` for EUR-only analysis
8. Export the cleaned dataset
9. Import the cleaned data into PostgreSQL
10. Analyze the data with SQL
11. Build the Power BI dashboard

### Key findings

- Total recorded EUR value is approximately **€13.04 billion**
- Median procurement value is **€377,500**
- Works have the highest total procurement value
- Goods have the highest number of procurement records
- Open procedure is the most common procurement method
- Several very large procurements make the average value significantly higher than the median
- HŽ Infrastruktura has the highest total procurement value among the analyzed buyers

### Dashboard

The Power BI dashboard includes:

- Total procurement count
- Number of records with a known EUR value
- Total EUR procurement value
- Median procurement value
- Monthly procurement value
- Procurement value by category
- Top 10 buyers by total procurement value
- Procurement method filter

The Power BI file is available here:

[`powerbi/procurement_dashboard.pbix`](powerbi/procurement_dashboard.pbix)

### SQL analysis

The PostgreSQL table definition is available in:

[`sql/create_tables.sql`](sql/create_tables.sql)

The analytical SQL queries are available in:

[`sql/analysis_queries.sql`](sql/analysis_queries.sql)

The queries include:

- General procurement KPIs
- Average, median, minimum, and maximum values
- Procurement analysis by category
- Procurement analysis by method
- Monthly analysis
- Top buyers by total value
- Largest individual procurements

### Project structure

```text
project/
├── data/
│   └── raw/
│       ├── sample.csv
│       └── sample.txt
├── docs/
│   └── images/
│       └── dashboard.png
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

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the required packages and the project:

```powershell
pip install -r requirements.txt
pip install -e .
```

### Run tests

```powershell
python -m pytest -v
```

The project currently contains **21 passing tests**.

### CLI usage

Create a JSON profile of a CSV file:

```powershell
python -m procurement_analytics.cli profile input.csv output.json
```

Create a cleaned CSV file:

```powershell
python -m procurement_analytics.cli clean input.csv output.csv
```

Example using the Croatian procurement dataset:

```powershell
python -m procurement_analytics.cli clean data/raw/2024/main.csv data/processed/main_clean.csv
```

### Currency handling

The original dataset contains multiple currencies, including EUR, HRK, BGN, SEK, and CZK.

The `value_eur` column contains a value only when the original currency is EUR. Other currencies are preserved in `value_amount` and `value_currency`, but they are excluded from EUR totals to avoid combining different currencies without a documented conversion method.

---

## Hrvatski

Cjelovita analiza podataka o hrvatskoj javnoj nabavi iz 2024. godine pomoću Pythona, PostgreSQL-a, SQL-a i Power BI-ja.

### Pregled projekta

Projekt prikazuje cijeli proces analize podataka, od učitavanja i profiliranja izvornog CSV-a do spremanja očišćenih podataka u PostgreSQL, analize SQL upitima i prikaza rezultata u interaktivnom Power BI dashboardu.

Python pipeline podijeljen je u manje module za učitavanje, profiliranje, transformaciju i povezivanje cijelog procesa. Dodani su i automatizirani testovi koji provjeravaju glavne dijelove projekta.

### Podaci

Podaci o hrvatskoj javnoj nabavi preuzeti su iz Open Contracting Partnership Data Registryja.

Analizirani skup podataka sadrži:

- 5.924 zapisa javne nabave
- 1.130 jedinstvenih naručitelja
- 4.372 zapisa s poznatom EUR vrijednošću
- 11 očišćenih analitičkih stupaca
- Nema dupliciranih redaka u očišćenom skupu podataka

Cjeloviti izvorni i obrađeni podaci nisu uključeni u repozitorij zbog njihove veličine.

U repozitoriju se nalaze male ogledne datoteke koje se koriste za testiranje pipelinea.

### Alati

- **Python** — logika projekta i sučelje naredbenog retka
- **pandas** — učitavanje, profiliranje, čišćenje i transformacija podataka
- **PostgreSQL** — spremanje očišćenih podataka
- **SQL** — izračun KPI-jeva i analitički upiti
- **Power BI** — interaktivni dashboard i vizualna analiza
- **pytest** — automatizirano testiranje

### Proces obrade podataka

1. Učitavanje i provjera izvornog CSV-a
2. Profiliranje stupaca, praznih vrijednosti, tipova, jedinstvenih vrijednosti i duplikata
3. Odabir relevantnih stupaca javne nabave
4. Preimenovanje stupaca u ujednačen analitički format
5. Pretvaranje datuma objave u datetime vrijednosti
6. Pretvaranje iznosa nabave u brojčane vrijednosti
7. Izrada stupca `value_eur` za analizu EUR vrijednosti
8. Spremanje očišćenog skupa podataka
9. Uvoz očišćenih podataka u PostgreSQL
10. Analiza podataka SQL upitima
11. Izrada Power BI dashboarda

### Ključni nalazi

- Ukupna evidentirana EUR vrijednost iznosi približno **13,04 milijarde €**
- Medijan vrijednosti nabave iznosi **377.500 €**
- Radovi imaju najveću ukupnu vrijednost nabave
- Roba ima najveći broj zapisa
- Otvoreni postupak najčešća je metoda nabave
- Nekoliko vrlo velikih nabava značajno podiže prosjek iznad medijana
- HŽ Infrastruktura ima najveću ukupnu vrijednost među analiziranim naručiteljima

### Dashboard

Power BI dashboard prikazuje:

- Ukupan broj nabava
- Broj zapisa s poznatom EUR vrijednošću
- Ukupnu EUR vrijednost nabava
- Medijan vrijednosti nabave
- Mjesečno kretanje vrijednosti
- Vrijednost nabava po kategoriji
- Deset najvećih naručitelja prema ukupnoj vrijednosti
- Filtar prema metodi nabave

Power BI datoteka dostupna je ovdje:

[`powerbi/procurement_dashboard.pbix`](powerbi/procurement_dashboard.pbix)

### SQL analiza

Definicija PostgreSQL tablice nalazi se u:

[`sql/create_tables.sql`](sql/create_tables.sql)

Analitički SQL upiti nalaze se u:

[`sql/analysis_queries.sql`](sql/analysis_queries.sql)

Upiti uključuju:

- Osnovne KPI-jeve
- Prosjek, medijan, minimum i maksimum
- Analizu prema kategoriji nabave
- Analizu prema metodi nabave
- Mjesečni pregled
- Najveće naručitelje prema ukupnoj vrijednosti
- Najveće pojedinačne nabave

### Struktura projekta

```text
project/
├── data/
│   └── raw/
│       ├── sample.csv
│       └── sample.txt
├── docs/
│   └── images/
│       └── dashboard.png
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

Izradi i aktiviraj virtualno okruženje:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Instaliraj potrebne pakete i projekt:

```powershell
pip install -r requirements.txt
pip install -e .
```

### Pokretanje testova

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

Primjer s podacima hrvatske javne nabave:

```powershell
python -m procurement_analytics.cli clean data/raw/2024/main.csv data/processed/main_clean.csv
```

### Rad s valutama

Izvorni skup podataka sadrži više valuta, uključujući EUR, HRK, BGN, SEK i CZK.

Stupac `value_eur` sadrži vrijednost samo kada je izvorna valuta EUR. Ostale valute ostaju sačuvane u stupcima `value_amount` i `value_currency`, ali nisu uključene u EUR zbrojeve kako se različite valute ne bi zbrajale bez dokumentiranog načina konverzije.
