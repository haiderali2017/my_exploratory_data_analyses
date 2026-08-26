# Cleaning practices
## 1. Improving column names
`ALTER TABLE domestic_travel 
RENAME COLUMN "Statistic Label" TO Statistic_Label;`

`ALTER TABLE domestic_travel 
RENAME COLUMN "Region Visited" TO Region_Visited;
`

## 2. Concise names for Statistic Label
`UPDATE domestic_travel
SET Statistic_Label = CASE Statistic_Label
    WHEN 'Number of Trips by Irish Residents on Domestic Travel' THEN 'Number of Trips'
    WHEN 'Number of Nights by Irish Residents on Domestic Travel' THEN 'Number of Nights'
    WHEN 'Average Length of Stay by Irish Residents on Domestic Travel' THEN 'Average Length of Stay'
    WHEN 'Estimated Expenditure by Irish Residents on Domestic Travel' THEN 'Estimated Expenditure'
    ELSE Statistic_Label
END;`


# SQL Findings
## 1. Dataset size
`SELECT COUNT(*) FROM domestic_travel;`

### Output
| COUNT(*) |
| --- |
| 384 |

## 2. Missing values
`SELECT 
    COUNT(*) AS total_rows,
COUNT("Statistic_Label") AS label_count,
    COUNT("Year") AS year_count,
COUNT("Region_Visited") AS region_count,
COUNT("UNIT") AS unit_count,
    COUNT("VALUE") AS value_count
FROM domestic_travel;
`

### Output
| total_rows | label_count | year_count | region_count | unit_count | value_count |
| --- | --- | --- | --- | --- | --- |
| 384 | 384 | 384 | 384 | 384 | 384 |

## 3. All Regions
`SELECT DISTINCT "Region_Visited" FROM domestic_travel;`

### Output
| State                |
|----------------------|
| Northern and Western |
| Border               |
| West                 |
| Southern             |
| Mid-West             |
| South-East           |
| South-West           |
| Eastern and Midland  |
| Dublin               |
| Mid-East             |
| Midland              |
<br>

## 4. Top 5 Regions Visited (In terms of all 4 stat labels)
`SELECT
Region_Visited,
Year,
SUM(VALUE) as Total,
UNIT,
RANK() OVER (ORDER BY SUM(VALUE) DESC) AS Ranking
FROM domestic_travel
WHERE Statistic_Label = 'Number of Trips'
GROUP BY Year, Region_Visited
LIMIT 5;`

### Output (Number of Trips)
| Region_Visited | Year | Total | UNIT | Ranking |
|-------|------|-------|----------|---|
| State | 2024 | 16571 | Thousand | 1 |
| State | 2025 | 15283 | Thousand | 2 |
| State | 2023 | 14309 | Thousand | 3 |
| State | 2022 | 13274 | Thousand | 4 |
| State | 2019 | 11621 | Thousand | 5 |

### Output (Number of Nights)
| Region_Visited | Year | Total | UNIT | Ranking |
|-------|------|-------|----------|---|
| State | 2024 | 36747 | Thousand | 1 |
| State | 2022 | 34236 | Thousand | 2 |
| State | 2023 | 33978 | Thousand | 3 |
| State | 2025 | 33435 | Thousand | 4 |
| State | 2019 | 29469 | Thousand | 5 |

### Output (Average Length of Stay)
| Region_Visited | Year | Total | UNIT | Ranking |
|-------|------|-------|----------|---|
| Border               | 2021 | 3.9 | Nights per Trip | 1 |
| South-West           | 2020 | 3.7 | Nights per Trip | 2 |
| South-West           | 2021 | 3.7 | Nights per Trip | 2 |
| Northern and Western | 2021 | 3.5 | Nights per Trip | 4 |
| Southern             | 2021 | 3.4 | Nights per Trip | 5 |

### Output (Estimated Expenditure)
| Region_Visited | Year | Total | UNIT | Ranking |
|-------|------|-------|----------|---|
| State | 2025 | 3578   | Euro Million | 1 |
| State | 2024 | 3570.5 | Euro Million | 2 |
| State | 2023 | 3087.4 | Euro Million | 3 |
| State | 2022 | 2930   | Euro Million | 4 |
| State | 2019 | 2146.6 | Euro Million | 5 |

# Original source of data
The data is also at https://data.cso.ie/table/HTA17.
