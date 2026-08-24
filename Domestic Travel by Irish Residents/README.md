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
COUNT("Statistic Label") AS label_count,
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
The data source is also at https://data.cso.ie/. <br>
I am listing the steps below as the URL doesn't generate a direct link to the data source.
1. Go to https://data.cso.ie/.
2. In the date range (below the grey 'Search' button), select 1-August-2026.
3. Type 'HTA17' in the search text field below the date field.
4. Select the top search result.
