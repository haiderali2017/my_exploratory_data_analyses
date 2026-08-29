# Some cleaning
## 1. Improving column names
`ALTER TABLE` <br> `domestic_travel
`<br>` RENAME COLUMN `<br>`"Statistic Label" TO Statistic_Label;`

`ALTER TABLE` <br> `domestic_travel 
`<br>` RENAME COLUMN `<br>`"Region Visited" TO Region_Visited;
`

## 2. Concise names for Statistic Label
*We are renaming the default label names for readability purposes. <br>For example, 'Number of Trips by Irish Residents on Domestic Travel' to 'Number of Trips' and so on.*

`UPDATE domestic_travel
`<br>`SET Statistic_Label = CASE Statistic_Label
    `<br>`WHEN 'Number of Trips by Irish Residents on Domestic Travel' THEN 'Number of Trips'
    `<br>`WHEN 'Number of Nights by Irish Residents on Domestic Travel' THEN 'Number of Nights'
    `<br>`WHEN 'Average Length of Stay by Irish Residents on Domestic Travel' THEN 'Average Length of Stay'
    `<br>`WHEN 'Estimated Expenditure by Irish Residents on Domestic Travel' THEN 'Estimated Expenditure'
    `<br>`ELSE Statistic_Label
END;`
<br>
| **Statistic_Label (BEFORE)**        || **Statistic_Label (AFTER)**        |
|------------------------|-|------------------------|
| Number of Trips by Irish Residents on Domestic Travel        || Number of Trips        |
| Number of Nights by Irish Residents on Domestic Travel       || Number of Nights       |
| Average Length of Stay by Irish Residents on Domestic Travel || Average Length of Stay |
| Estimated Expenditure by Irish Residents on Domestic Travel  || Estimated Expenditure  |

# Data Exploration
## 1. Dataset size
*Total 384 rows*<br><br>
`SELECT COUNT(*) FROM domestic_travel;`

### Output
| COUNT(*) |
| --- |
| 384 |

## 2. Missing values
*There are no missing values.*<br><br>
`SELECT `<br>`
COUNT(*) AS total_rows,`<br>`
COUNT("Statistic_Label") AS label_count,`<br>`
COUNT("Year") AS year_count,`<br>`
COUNT("Region_Visited") AS region_count,`<br>`
COUNT("UNIT") AS unit_count,`<br>`
COUNT("VALUE") AS value_count`<br>`
FROM domestic_travel;
`

### Output
| total_rows | label_count | year_count | region_count | unit_count | value_count |
| --- | --- | --- | --- | --- | --- |
| 384 | 384 | 384 | 384 | 384 | 384 |

## 3. All Regions
*There are 11 regions.*<br><br>
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

## 4. 

# Original source of data
The data is also at https://data.cso.ie/table/HTA17.
