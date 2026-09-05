## Table of Contents
- [Some cleaning](#cleaning_main_heading)
    - [Improving column names](#improving_column_names)
    - [Concise names for Statistic Label](#concise_names_for_stat_labels)
- [Data Exploration](#data_exploration)
  - [1. Dataset size](#dataset_size)
  - [2. Missing values](#missing_values)
  - [3. All Regions](#all_regions)
  - [4. Statistic Labels and their respective units](#stat_labels_and_units)
  - [5. Count of records for each stat label](#each_stat_label_record_count)
  - [6. Count of records using years](#counting_records_through_years)
  - [7. Sum aggregation of values](#sum_of_values)
  - [8. Time trend analysis for Number of Trips](#time_trend_analysis)
      - [Number of Trips](#number_of_trips)
      - [Number of Nights](#number_of_nights)
      - [Average Length of Stay](#avg_length_of_stay)
      - [Estimated Expenditure](#estimated_expenditure)
- [Source of data](#data_source)


# Some cleaning <a name="cleaning_main_heading"></a>
## 1. Improving column names <a name="improving_column_names"></a>
```sql
ALTER TABLE domestic_travel
RENAME COLUMN "Statistic Label" TO Statistic_Label;

ALTER TABLE domestic_travel 
RENAME COLUMN "Region Visited" TO Region_Visited;
```

## 2. Concise names for Statistic Label <a name="concise_names_for_stat_labels"></a>
*We are renaming the default label names for readability purposes. <br>For example, 'Number of Trips by Irish Residents on Domestic Travel' to 'Number of Trips'.*

```sql
UPDATE domestic_travel
SET Statistic_Label = CASE Statistic_Label
    WHEN 'Number of Trips by Irish Residents on Domestic Travel' THEN 'Number of Trips'
    WHEN 'Number of Nights by Irish Residents on Domestic Travel' THEN 'Number of Nights'
    WHEN 'Average Length of Stay by Irish Residents on Domestic Travel' THEN 'Average Length of Stay'
    WHEN 'Estimated Expenditure by Irish Residents on Domestic Travel' THEN 'Estimated Expenditure'
    ELSE Statistic_Label
END;
```

### Outcome
| **Statistic_Label (BEFORE)**        || **Statistic_Label (AFTER)**        |
|------------------------|-|------------------------|
| Number of Trips by Irish Residents on Domestic Travel        || Number of Trips        |
| Number of Nights by Irish Residents on Domestic Travel       || Number of Nights       |
| Average Length of Stay by Irish Residents on Domestic Travel || Average Length of Stay |
| Estimated Expenditure by Irish Residents on Domestic Travel  || Estimated Expenditure  |

# Data Exploration <a name="data_exploration"></a>
## 1. Dataset size <a name="dataset_size"></a>
*Total 384 rows*
```sql
`SELECT COUNT(*) FROM domestic_travel;`
```

### Output
| COUNT(*) |
| --- |
| 384 |

## 2. Missing values <a name="missing_values"></a>
*There are no missing values.*

```sql
SELECT 
COUNT(*) AS total_rows,
COUNT("Statistic_Label") AS label_count,
COUNT("Year") AS year_count,
COUNT("Region_Visited") AS region_count,
COUNT("UNIT") AS unit_count,
COUNT("VALUE") AS value_count
FROM domestic_travel;
```

### Output
| total_rows | label_count | year_count | region_count | unit_count | value_count |
| --- | --- | --- | --- | --- | --- |
| 384 | 384 | 384 | 384 | 384 | 384 |

## 3. All Regions <a name="all_regions"></a>
*There are 12 regions.*
```sql
SELECT DISTINCT Region_Visited FROM domestic_travel;
```
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

## 4. Statistic Labels and their respective units <a name="stat_labels_and_units"></a>
*The statistic labels are measured in their own units.*
```sql
SELECT DISTINCT Statistic_Label, UNIT FROM domestic_travel;
```

### Output
| Statistic_Label        | UNIT            |
|------------------------|-----------------|
| Number of Trips        | Thousand        |
| Number of Nights       | Thousand        |
| Average Length of Stay | Nights per Trip |
| Estimated Expenditure  | Euro Million    |
<br>

## 5. Count of records for each stat label <a name="each_stat_label_record_count"></a>
*There are exactly 96 rows for all 4 labels.* <br> *96 x 4 = 384 total rows*
```sql
SELECT
    Statistic_Label,
    COUNT(*) as Total_Records
FROM domestic_travel
GROUP BY Statistic_Label;
```

### Output
| Statistic_Label        | Total_Records |
|------------------------|---------------|
| Average Length of Stay | 96            |
| Estimated Expenditure  | 96            |
| Number of Nights       | 96            |
| Number of Trips        | 96            |

## 6. Count of records using years <a name="counting_records_through_years"></a>
*There are exactly 48 rows for all 8 years.* <br> *48 x 8 = 384 total rows*
```sql
SELECT
    Year,
    COUNT(*) as Total_Records
FROM domestic_travel
GROUP BY Year;
```

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

## 7. Sum aggregation of values <a name="sum_of_values"></a>
* **Number of Nights:** *712 million*
* **Number of Trips:** *286 million*
* **Estimated Expenditure:** *60 euro millions*
* **Average Length of Stay:** *242.3 nights per trip*

```sql
SELECT
    Statistic_Label,
    SUM(VALUE) as _Sum,
    UNIT
FROM domestic_travel
GROUP BY Statistic_Label
ORDER BY _Sum DESC;
```

### Output
| Statistic_Label        | _Sum    | UNIT            |
|------------------------|---------|-----------------|
| Number of Nights       | 712989  | Thousand        |
| Number of Trips        | 286083  | Thousand        |
| Estimated Expenditure  | 60489.7 | Euro Million    |
| Average Length of Stay | 242.3   | Nights per Trip |

## 8. Time trend analysis for Number of Trips <a name="time_trend_analysis"></a>
This section looks at time trend analysis for all 4 statistic labels. I want to see how was the growth for different regions during the 7-year period.

### Number of Trips <a name="number_of_trips"></a>
I observed that
* The pandemic year caused decline in the number of trips throughout all regions.
  * Dublin shows the heaviest decline of 49.4% followed by 46.44% of Mid-East.
  * Midland showed the least decline (16.52%).
* 2021 (post-pandemic) continues that declining trend for all regions.
* In 2022, trends show sharp inclines for all regions. Midland (212.0%), Border (163.28%) and Eastern & Midland (150.46%) are top 3 regions with highest growths.
* In 2023, except for 3 regions (Border, Midland and Northern & Western), the trend keeps going in an upward direction.
* 2024 shares the positive trend aspect of 2022.
* In 2025, the number of trips goes in a downward direction in all regions. 

<br>

| Year | Border | Dublin | Eastern & Midland | Mid-East | Mid-West | Midland | Northern & Western | South-East | South-West | Southern | State | West |
|------|--------|--------|-------------------|----------|----------|---------|--------------------|------------|------------|----------|-------|------|
| 2019 | ▲18.78% | ▲3.71% | ▲6.29% | ▲23.3% | ▲9.82% | ▼12.71% | ▲14.04% | ▲6.65% | ▼3.54% | ▲2.59% | ▲6.43% | ▲11.19% |
| 2020 | ▼25.4% | ▼49.4% | ▼43.83% | ▼46.44% | ▼26.4% | ▼16.52% | ▼26.84% | ▼40.45% | ▼26.21% | ▼31.07% | ▼33.56% | ▼27.76% |
| 2021 | ▼31.23% | ▼12.22% | ▼17.17% | ▼12.94% | ▼39.73% | ▼34.9% | ▼29.88% | ▼25.63% | ▼26.57% | ▼29.46% | ▼26.65% | ▼29.06% |
| 2022 | ▲163.28% | ▲137.68% | ▲150.46% | ▲139.71% | ▲148.96% | ▲212.0% | ▲122.85% | ▲138.87% | ▲120.16% | ▲131.89% | ▲134.4% | ▲97.04% |
| 2023 | ▼5.35% | ▲29.82% | ▲14.78% | ▲6.8% | ▲8.4% | ▼9.23% | ▼0.03% | ▲4.95% | ▲9.7% | ▲7.89% | ▲7.8% | ▲4.56% |
| 2024 | ▲20.2% | ▲16.85% | ▲18.83% | ▲16.15% | ▲23.87% | ▲30.37% | ▲23.51% | ▲6.02% | ▲5.25% | ▲9.62% | ▲15.81% | ▲26.14% |
| 2025 | ▼10.18% | ▼15.09% | ▼12.89% | ▼11.58% | ▼6.14% | ▼8.13% | ▼5.2% | ▼5.58% | ▼5.24% | ▼5.57% | ▼7.77% | ▼1.54% |

<br>

### Number of Nights <a name="number_of_nights"></a>
* The pandemic year caused decline in the number of nights throughout all regions.
  * Dublin shows the heaviest decline of 44.48% followed by 43.69% of Mid-East.
  * Mid-West showed the least decline (3.65%).
* 2021 (post-pandemic) continues that declining trend for all regions except,
  * Mid-East, which is an outlier that year. It shows a 1.41% ascent. 
* In 2022, trends show sharp inclines for all regions. 
  * Midland (280.36%), Eastern & Midland (131.86%) and South-East (127.11%) are top 3 regions with highest growths.
* In 2023, some regions show upward trend and others show downward trend. 
  * Dublin marks highest growth (22.47%).
  * Midland shows the most decline (27.81%).
* In 2024, amongst all other growing regions, only Southern and State show a decline.
* In 2025, opposite to 2024, amongst all other declining regions, only Southern and State show growth.

<br>

| Year | Border | Dublin | Eastern & Midland | Mid-East | Mid-West | Midland | Northern & Western | South-East | South-West | Southern | State | West |
|------|--------|--------|-------------------|----------|----------|---------|--------------------|------------|------------|----------|-------|------|
| 2019 | ▲5.21% | ▼7.57% | ▲1.59% | ▲26.66% | ▼2.35% | ▼7.82% | ▲10.49% | ▼2.98% | ▲5.73% | ▲1.31% | ▲3.79% | ▲14.0% |
| 2020 | ▼10.38% | ▼44.48% | ▼34.31% | ▼43.69% | ▼3.65% | ▲29.15% | ▼13.97% | ▼30.63% | ▼14.82% | ▼17.58% | ▼20.19% | ▼16.18% |
| 2021 | ▼15.05% | ▼2.39% | ▼13.93% | ▲1.41% | ▼36.41% | ▼50.09% | ▼22.93% | ▼24.64% | ▼26.05% | ▼28.0% | ▼23.95% | ▼28.1% |
| 2022 | ▲81.99% | ▲101.25% | ▲131.86% | ▲110.48% | ▲89.25% | ▲280.36% | ▲70.64% | ▲127.11% | ▲66.91% | ▲87.76% | ▲91.41% | ▲61.86% |
| 2023 | ▼15.05% | ▲22.47% | ▲0.1% | ▼9.22% | ▲6.75% | ▼27.81% | ▼12.57% | ▼16.31% | ▲20.31% | ▲5.53% | ▼0.75% | ▼10.43% |
| 2024 | ▲36.1% | ▲13.08% | ▲13.39% | ▲12.13% | ▲2.52% | ▲16.27% | ▲37.64% | ▲4.01% | ▼18.29% | ▼8.27% | ▲8.15% | ▲38.92% |
| 2025 | ▼25.57% | ▼24.61% | ▼16.9% | ▼8.26% | ▼8.81% | ▼7.28% | ▼19.97% | ▼2.97% | ▲13.16% | ▲3.43% | ▼9.01% | ▼15.44% |

<br>

### Average Length of Stay <a name="avg_length_of_stay"></a>
* In 2020, average length of stay improved compared with 2019.
* Same for 2021; the average length of stay improved in comparison to 2020.
  * However, only Midland showed a decline of 24.14%.
* Contrary to 2021, the average length of stay declined everywhere except Midland (22.73%) in 2022.
* The trend continued to decline in 2023 in all regions except South-West (10.71%).
* In 2024, most regions show a declining average length of stay except,
  * Border, improved to 16.67%.
  * Northern & Western, improved to 8.33%.
  * West, improved to 8.7%.
* In 2025, there is no clear pattern of increase or decrease. 
  * Mid-West, Midland and State show 0.0% change.
  * 4 regions improved.
  * 5 regions declined.
<br><br>

| Year | Border | Dublin | Eastern & Midland | Mid-East | Mid-West | Midland | Northern & Western | South-East | South-West | Southern | State | West |
|------|--------|--------|-------------------|----------|----------|---------|--------------------|------------|------------|----------|-------|------|
| 2019 | ▼13.33% | ▼13.64% | ▲0.0% | ▲0.0% | ▼11.11% | ▲5.56% | ▼3.57% | ▼7.14% | ▲10.34% | ▲0.0% | ▼3.85% | ▲3.7% |
| 2020 | ▲23.08% | ▲10.53% | ▲15.0% | ▲5.0% | ▲29.17% | ▲52.63% | ▲18.52% | ▲15.38% | ▲15.63% | ▲17.86% | ▲20.0% | ▲14.29% |
| 2021 | ▲21.87% | ▲14.29% | ▲4.35% | ▲19.05% | ▲6.45% | ▼24.14% | ▲9.37% | ▲0.0% | ▲0.0% | ▲3.03% | ▲6.67% | ▲3.12% |
| 2022 | ▼30.77% | ▼16.67% | ▼8.33% | ▼12.0% | ▼24.24% | ▲22.73% | ▼22.86% | ▼3.33% | ▼24.32% | ▼17.65% | ▼18.75% | ▼18.18% |
| 2023 | ▼11.11% | ▼5.0% | ▼13.64% | ▼13.64% | ▼4.0% | ▼18.52% | ▼11.11% | ▼20.69% | ▲10.71% | ▼3.57% | ▼7.69% | ▼14.81% |
| 2024 | ▲16.67% | ▼5.26% | ▼5.26% | ▼5.26% | ▼16.67% | ▼13.64% | ▲8.33% | ▼4.35% | ▼22.58% | ▼14.81% | ▼8.33% | ▲8.7% |
| 2025 | ▼17.86% | ▼11.11% | ▼5.56% | ▲5.56% | ▲0.0% | ▲0.0% | ▼15.38% | ▲4.55% | ▲20.83% | ▲8.7% | ▲0.0% | ▼12.0% |

<br>

### Estimated Expenditure <a name="estimated_expenditure"></a>
* In 2020, estimated expenditure went down across all regions.
* In 2021, estimated expenditure went down across all regions except Dublin.
  * Dublin displayed a 4.67% increase. 
* In 2022, estimated expenditure went up across all regions.
  * Midland showed the highest increase of 287.23% amongst all regions.
  * The second-highest increase was 175.93%, marked by Eastern & Midland.
  * The third-highest increase was 166.88%, marked by Dublin.
* In 2023, there is no clear pattern. 
* In 2024, estimated expenditure went up across all regions except South-West.
* In 2025, there is no clear pattern. 
<br><br>

| Year | Border | Dublin | Eastern & Midland | Mid-East | Mid-West | Midland | Northern & Western | South-East | South-West | Southern | State | West |
|------|--------|--------|-------------------|----------|----------|---------|--------------------|------------|------------|----------|-------|------|
| 2019 | ▲11.4% | ▼13.56% | ▼1.29% | ▲34.47% | ▲29.53% | ▼2.5% | ▲10.29% | ▲2.73% | ▲7.74% | ▲9.99% | ▲7.01% | ▲9.69% |
| 2020 | ▼9.18% | ▼49.41% | ▼41.11% | ▼43.93% | ▼22.01% | ▼2.44% | ▼12.69% | ▼42.27% | ▼23.5% | ▼28.82% | ▼27.61% | ▼14.86% |
| 2021 | ▼25.27% | ▲4.67% | ▼6.65% | ▼1.1% | ▼30.77% | ▼38.16% | ▼24.7% | ▼10.0% | ▼12.53% | ▼16.08% | ▼16.92% | ▼24.13% |
| 2022 | ▲157.35% | ▲166.88% | ▲175.93% | ▲136.67% | ▲123.08% | ▲287.23% | ▲115.73% | ▲135.19% | ▲94.44% | ▲110.47% | ▲126.96% | ▲92.05% |
| 2023 | ▼2.71% | ▲15.78% | ▲2.01% | ▲2.82% | ▲13.83% | ▼30.6% | ▼5.57% | ▼5.07% | ▲25.46% | ▲14.24% | ▲5.37% | ▼7.76% |
| 2024 | ▲12.86% | ▲18.9% | ▲27.69% | ▲40.68% | ▲16.29% | ▲38.88% | ▲29.93% | ▲15.68% | ▼9.65% | ▲1.65% | ▲15.65% | ▲43.65% |
| 2025 | ▼7.39% | ▼14.32% | ▼6.81% | ▼20.42% | ▼10.74% | ▲41.85% | ▼5.14% | ▲13.72% | ▲14.65% | ▲8.61% | ▲0.21% | ▼3.72% |


```sql
--- The query says select some columns and calculate percent 
--- growth from a table which has two copies (d1 and d2) and 
--- self join them on regions and year. Also ensure the label is 
--- Number of trips and order by Regions then Year.

SELECT     --- Choose the columns to show
    d1.Year,    --- The current year
    d1.Region_Visited,    --- The regions
    d1.VALUE AS current_,    --- The current year
    d2.VALUE AS previous_,    --- The previous year
    ROUND(
        ((d1.VALUE - d2.VALUE) * 100.0 / d2.VALUE), 2) 
    AS yoy_growth_pct    --- Year-over-year growth percentage
FROM domestic_travel d1    --- Create an alias d1 (This will hold the current year's data.)
LEFT JOIN domestic_travel d2    --- Alias d2 will hold the previous year's data. For each row in d1, try to find the matching rows from the same table again.
    ON d1.Region_Visited = d2.Region_Visited    --- Example: d1=Border will only try to match d2=Border 
    AND d1.Year = d2.Year + 1     --- Example: if d1.Year=2019, then d2.Year must be 2018.
    AND d2.Statistic_Label = 'Number of Trips'    --- Choose the desired Statistic_Label
WHERE d1.Statistic_Label = 'Number of Trips'    --- After the join is done, keep only the rows from d1 where Statistic_Label is 'Number of Trips'
ORDER BY d1.Region_Visited, d1.Year;    --- Sort the final result first by region then by year (oldest to newest)
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

*There are total 96 rows in this output. I have only shown 26 for example.*

# Source of data <a name="data_source"></a>
The data is also at https://data.cso.ie/table/HTA17.
