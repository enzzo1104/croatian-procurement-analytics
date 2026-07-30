-- 1. Osnovni KPI-jevi
SELECT COUNT(*) AS total_tenders,
    COUNT(value_eur) AS tenders_with_eur_value,
    SUM(value_eur) AS total_value_eur
FROM public.tenders;
-- 2. Deset najvećih nabava
SELECT buyer_name,
    title,
    value_eur
FROM public.tenders
WHERE value_eur IS NOT NULL
ORDER BY value_eur DESC
LIMIT 10;
-- 3. Prosjek, medijan, minimum i maksimum
SELECT AVG(value_eur) AS average_value_eur,
    PERCENTILE_CONT(0.5) WITHIN GROUP (
        ORDER BY value_eur
    ) AS median_value_eur,
    MIN(value_eur) AS minimum_value_eur,
    MAX(value_eur) AS maximum_value_eur
FROM public.tenders
WHERE value_eur IS NOT NULL;
-- 4. Analiza prema kategoriji nabave
SELECT procurement_category,
    COUNT(*) AS tender_count,
    SUM(value_eur) AS total_value_eur,
    AVG(value_eur) AS average_value_eur
FROM public.tenders
GROUP BY procurement_category
ORDER BY total_value_eur DESC NULLS LAST;
-- 5. Deset narucitelja s najvecom ukupnom vrijednoscu
SELECT buyer_name,
    COUNT(*) AS tender_count,
    SUM(value_eur) AS total_value_eur
FROM public.tenders
GROUP BY buyer_name
ORDER BY total_value_eur DESC NULLS LAST
LIMIT 10;
-- 6. Mjesecni pregled
SELECT DATE_TRUNC('month', publication_date) AS month,
    COUNT(*) AS tender_count,
    SUM(value_eur) AS total_value_eur
FROM public.tenders
GROUP BY month
ORDER BY month;
-- 7. Analiza prema metodi nabave
SELECT procurement_method,
    COUNT(*) AS tender_count,
    SUM(value_eur) AS total_value_eur
FROM public.tenders
GROUP BY procurement_method
ORDER BY tender_count DESC;
