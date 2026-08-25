# Cleaning practices
## 1. Changing column name
`ALTER TABLE domestic_travel 
RENAME COLUMN "Statistic Label" TO Statistic_Label;`

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
COUNT("Region Visited") AS region_count,
COUNT("UNIT") AS unit_count,
    COUNT("VALUE") AS value_count
FROM domestic_travel;
`

### Output
| total_rows | label_count | year_count | region_count | unit_count | value_count |
| --- | --- | --- | --- | --- | --- |
| 384 | 384 | 384 | 384 | 384 | 384 |

## 3.	All Regions
`SELECT DISTINCT "Region Visited" FROM domestic_travel;`

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

# Original source of data
The data is also at https://data.cso.ie/table/HTA17.
