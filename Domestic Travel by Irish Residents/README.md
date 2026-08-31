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
*There are 12 regions.*<br><br>
`SELECT DISTINCT Region_Visited FROM domestic_travel;`

### Output
| Region_Visited       |
|----------------------|
| State                |
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

## 4. Statistic Labels and their respective units
*The statistic labels are measured in their units.* <br><br>
`SELECT DISTINCT Statistic_Label, UNIT FROM domestic_travel;`

### Output
| Statistic_Label        | UNIT            |
|------------------------|-----------------|
| Number of Trips        | Thousand        |
| Number of Nights       | Thousand        |
| Average Length of Stay | Nights per Trip |
| Estimated Expenditure  | Euro Million    |
<br>

## 5. Count of records for each stat label
*Interestingly, there are exactly 96 rows for all 4 labels.* <br> *96 x 4 = 384 total rows* <br><br> 
`SELECT`<br>`Statistic_Label,`<br>`COUNT(*) as Total_Records`<br>`FROM domestic_travel`<br>`GROUP BY Statistic_Label; `

### Output
| Statistic_Label        | Total_Records |
|------------------------|---------------|
| Average Length of Stay | 96            |
| Estimated Expenditure  | 96            |
| Number of Nights       | 96            |
| Number of Trips        | 96            |

## 6. Count of records using years
*There are exactly 48 rows for all 8 years.* <br> *48 x 8 = 384 total rows* <br><br> 
`SELECT`<br>`Year,`<br>`COUNT(*) as Total_Records`<br>`FROM domestic_travel`<br>`GROUP BY Year; `

### Output
| Year | Total_Records |
|------|---------------|
| 2018 | 48            |
| 2019 | 48            |
| 2020 | 48            |
| 2021 | 48            |
| 2022 | 48            |
| 2023 | 48            |
| 2024 | 48            |
| 2025 | 48            |

## 7. Sum aggregation of values
*According to the dataset,* 
* **Number of Nights:** *712 million*
* **Number of Trips:** *286 million*
* **Estimated Expenditure:** *60 euro millions*
* **Average Length of Stay:** *242.3 nights per trip*
<br><br> 

`SELECT`<br>`Statistic_Label,`<br>`SUM(VALUE) as _Sum,`<br>`UNIT`<br>`FROM domestic_travel`<br>`GROUP BY Statistic_Label`<br>`ORDER BY _Sum DESC;`

### Output
| Statistic_Label        | _Sum    | UNIT            |
|------------------------|---------|-----------------|
| Number of Nights       | 712989  | Thousand        |
| Number of Trips        | 286083  | Thousand        |
| Estimated Expenditure  | 60489.7 | Euro Million    |
| Average Length of Stay | 242.3   | Nights per Trip |

## 8. Time trend analysis for Number of Trips
This section looks only at the "Number of Trips" statistic label. I want to see how did the trend go on for different regions during the 7-year period. 

After taking a good look at the table below, I observed that
* The pandemic year caused decline in the number of trips throughout all regions.
  * Dublin shows the heaviest decline of 49.4% followed by 46.44% of Mid-East.
  * Midland showed the least decline (16.52%).
* 2021 (post-pandemic) continues that declining trend for all regions.
* In 2022, trends show sharp inclines for all regions. Midland (212.0%), Border (163.28%) and Eastern & Midland (150.46%) are top 3 regions with highest growths.
* In 2023, except for 3 regions (Border, Midland and Northern & Western), the trend keeps going in an upward direction.
* 2024 shares the positive trend aspect of 2022.
* In 2025, the number of trips goes in a downward direction in all regions. 

| Year | Border | Dublin | Eastern & Midland | Mid-East | Mid-West | Midland | Northern & Western | South-East | South-West | Southern | State | West |
|------|--------|--------|-------------------|----------|----------|---------|--------------------|------------|------------|----------|-------|------|
| 2019 | ▲18.78% | ▲3.71% | ▲6.29% | ▲23.3% | ▲9.82% | ▼12.71% | ▲14.04% | ▲6.65% | ▼3.54% | ▲2.59% | ▲6.43% | ▲11.19% |
| 2020 | ▼25.4% | ▼49.4% | ▼43.83% | ▼46.44% | ▼26.4% | ▼16.52% | ▼26.84% | ▼40.45% | ▼26.21% | ▼31.07% | ▼33.56% | ▼27.76% |
| 2021 | ▼31.23% | ▼12.22% | ▼17.17% | ▼12.94% | ▼39.73% | ▼34.9% | ▼29.88% | ▼25.63% | ▼26.57% | ▼29.46% | ▼26.65% | ▼29.06% |
| 2022 | ▲163.28% | ▲137.68% | ▲150.46% | ▲139.71% | ▲148.96% | ▲212.0% | ▲122.85% | ▲138.87% | ▲120.16% | ▲131.89% | ▲134.4% | ▲97.04% |
| 2023 | ▼5.35% | ▲29.82% | ▲14.78% | ▲6.8% | ▲8.4% | ▼9.23% | ▼0.03% | ▲4.95% | ▲9.7% | ▲7.89% | ▲7.8% | ▲4.56% |
| 2024 | ▲20.2% | ▲16.85% | ▲18.83% | ▲16.15% | ▲23.87% | ▲30.37% | ▲23.51% | ▲6.02% | ▲5.25% | ▲9.62% | ▲15.81% | ▲26.14% |
| 2025 | ▼10.18% | ▼15.09% | ▼12.89% | ▼11.58% | ▼6.14% | ▼8.13% | ▼5.2% | ▼5.58% | ▼5.24% | ▼5.57% | ▼7.77% | ▼1.54% |

The above table is a beautiful presentation of results generated by the following query.


```sql
--- The query says select some columns and calculate percent 
--- growth from a table which has two copies (d1 and d2) and 
--- self join them on regions and year. Also ensure the label is 
--- Number of trips and order by Regions first then Year.

SELECT
    d1.Year,
    d1.Region_Visited,
    d1.VALUE AS current_,
    d2.VALUE AS previous_,
    ROUND(
        ((d1.VALUE - d2.VALUE) * 100.0 / d2.VALUE), 2) 
    AS yoy_growth_pct
FROM domestic_travel d1
LEFT JOIN domestic_travel d2
    ON d1.Region_Visited = d2.Region_Visited
    AND d1.Year = d2.Year + 1
    AND d2.Statistic_Label = 'Number of Trips'
WHERE d1.Statistic_Label = 'Number of Trips'
ORDER BY d1.Region_Visited, d1.Year;
```

### Output

| Year | Region_Visited      | current_ | previous_ | yoy_growth_pct |
|------|---------------------|----------|-----------|----------------|
| 2018 | Border              | 1001     |           |                |
| 2019 | Border              | 1189     | 1001      | 18.78          |
| 2020 | Border              | 887      | 1189      | -25.4          |
| 2021 | Border              | 610      | 887       | -31.23         |
| 2022 | Border              | 1606     | 610       | 163.28         |
| 2023 | Border              | 1520     | 1606      | -5.35          |
| 2024 | Border              | 1827     | 1520      | 20.2           |
| 2025 | Border              | 1641     | 1827      | -10.18         |
| 2018 | Dublin              | 1700     |           |                |
| 2019 | Dublin              | 1763     | 1700      | 3.71           |
| 2020 | Dublin              | 892      | 1763      | -49.4          |
| 2021 | Dublin              | 783      | 892       | -12.22         |
| 2022 | Dublin              | 1861     | 783       | 137.68         |
| 2023 | Dublin              | 2416     | 1861      | 29.82          |
| 2024 | Dublin              | 2823     | 2416      | 16.85          |
| 2025 | Dublin              | 2397     | 2823      | -15.09         |
| 2018 | Eastern and Midland | 3082     |           |                |
| 2019 | Eastern and Midland | 3276     | 3082      | 6.29           |
| 2020 | Eastern and Midland | 1840     | 3276      | -43.83         |
| 2021 | Eastern and Midland | 1524     | 1840      | -17.17         |
| 2022 | Eastern and Midland | 3817     | 1524      | 150.46         |
| 2023 | Eastern and Midland | 4381     | 3817      | 14.78          |
| 2024 | Eastern and Midland | 5206     | 4381      | 18.83          |
| 2025 | Eastern and Midland | 4535     | 5206      | -12.89         |
| 2018 | Mid-East            | 854      |           |                |
| 2019 | Mid-East            | 1053     | 854       | 23.3           |

*There are total 96 rows in this output. I have only shown 26 for space-saving.*

# Source of data
The data is also at https://data.cso.ie/table/HTA17.
