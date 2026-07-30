CREATE TABLE IF NOT EXISTS public.tenders (
    id TEXT PRIMARY KEY,
    publication_date TIMESTAMPTZ NOT NULL,
    ocid TEXT NOT NULL,
    buyer_id TEXT NOT NULL,
    buyer_name TEXT NOT NULL,
    tender_id TEXT NOT NULL,
    procurement_category TEXT,
    title TEXT NOT NULL,
    procurement_method TEXT,
    value_amount NUMERIC(18, 2),
    value_currency VARCHAR(3),
    value_eur NUMERIC(18, 2)
);
