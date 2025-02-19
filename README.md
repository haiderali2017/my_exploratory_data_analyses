## Table of Contents
- [Introduction](#introduction)
- [Folder Structure](#folder_struct)
  - [Dublin Economic Monitor DCC Analysis](#dcc_analysis)
  - [HR Analytics PowerBI Project](#hr_analytics_proj)
  - [Product Sales Tableau Project](#prod_sales_tab_proj)
  - [Airline Reservation System Project](#airline_proj)
  - [Applied Research Project](#applied_research_proj)
  - [pharmacies_in_ireland](#pharmacies_in_ireland)
  - [second_hand_house_prices_ireland](#second_hand_house_prices_ireland)
  - [US Air Quality Index Tableau Project](#us_air_tab_proj)
  - [FireBrigadeAndAmbulanceCallOuts ETL Project](#etlproject)
  - [Mr Price Stores in Ireland](#mrpricewebscraping)
- [Contact information](#contact)

## Introduction <a name="introduction"></a>
This repository showcases multiple data analysis projects performed using Jupyter Notebook, PowerBI, etc. 

My recent project encircles around Dublin Economic Monitor DCC. This includes indicators to monitor economic development in the Dublin City Region. 

## Folder Structure <a name="folder_struct"></a>
### Dublin Economic Monitor DCC Analysis <a name="dcc_analysis"></a>
- This folder includes analysis performed on Dublin Economic Monitor DCC. Dublin Economic Monitor DCC includes indicators to monitor economic development in the Dublin City Region. 

### HR Analytics PowerBI Project <a name="hr_analytics_proj"></a>
- The **.pbix** is PowerBI file that contains the dashboard. **HR_Analytics.csv** is the relevant dataset. **.pdf** file showcases the output of dashboard created in PowerBI.

### Product Sales Tableau Project <a name="prod_sales_tab_proj"></a>
- This is my Masters 2nd Semester project made in the **Data Visualisation** course.
- The **.twb** is Tableau file that contains all the sheets and dashboards. **sales.xlsx** is the relevant dataset. **.pptx** file provides an explanation of the results within the Tableau file.
 
### Airline Reservation System Project <a name="airline_proj"></a>
- This is my Bachelors 3rd Semester project made in the **Database Development** course.
- As the name suggests, it is about an Airline Reservation System. 
- The **Airline Reservation System (NEW)** PDF file presents the conceptual schema of the Airline Reservation System.
- The **changed_dbd_normalization** Word file contains the logical schema (tables).
- The **SQL Joins** Word file showcases all possible join scenarios in the Airline Reservation System. The same applies to the **SQL Scenarios** and **SQL Views** Word files, which were created for extensive practice in SQL.

### Applied Research Project <a name="applied_research_proj"></a>
- This is my Masters final thesis project.
- The project is about identifying the causes of customer churn in telecommunication industry. It involves building machine learning models that help predict future customer churns using a dataset. 

### pharmacies_in_ireland <a name="pharmacies_in_ireland"></a>
- This project contains analysis performed on Pharmacies in Ireland.
- The analysis is performed using Pandas and Numpy whereas Seaborn and Matplotlib are used for visualisation purposes.
- The dataset is obtained from https://data.gov.ie/dataset/list-of-pharmacies-in-ireland?package_type=dataset which presents a list of Pharmacies in Ireland, with geographical coordinates.

### second_hand_house_prices_ireland <a name="second_hand_house_prices_ireland"></a>
- This project contains analysis performed on second hand property prices in Ireland.
- The analysis is performed using Pandas and Numpy whereas Matplotlib is used for visualisation purpose.
- The dataset is obtained from https://data.gov.ie/dataset/second-hand-property-prices-by-area-by-year?package_type=dataset which presents a list of house prices in major counties of Ireland with respect to year starting from 1975 to 2015.

### US Air Quality Index Tableau Project <a name="us_air_tab_proj"></a>
- This is my Masters 2nd Semester project made in the **Data Visualisation** course.
- The **.twb** is Tableau file that contains all the sheets and dashboards. Relevant dataset can be downloaded from https://drive.google.com/file/d/1Fba4OaIwrGIwopPZWMtwEZqxZBrli1wT/view?usp=sharing.

### FireBrigadeAndAmbulanceCallOuts ETL Project <a name="etlproject"></a>
- This is my Masters 1st Semester project made in the **Programming** course.
- **CA2.py** file contains all the data analysis steps using Python and Pandas library. It also contains the ETL (Extract, Transform and Load) steps using SQL.
- **FireBrigadeAndAmbulanceCallOuts.csv** is the relevant dataset.
- **document_2.docx** is the complete report explaining the steps performed.
- **high-level diagram.jpeg** is a conceptual diagram of ETL process.

### Mr Price Stores in Ireland <a name="mrpricewebscraping"></a>
- First web scraping attempt using Scrapy library.
- Used a static website to start off with static web scraping.
- Scrapped Mr. Price stores by county and areas within those counties.
- The scrapped data is stored within "Mr Price Stores in Ireland/mrprice_scraper/spiders/data.csv".
- To run the project, go to "Mr Price Stores in Ireland/mrprice_scraper/spiders/mrprice.py" and execute "scrapy crawl mrprice". This will crawl the website and generate data.csv
- Next up, I will analyze the scrapped data.csv using pandas and visualize using matplotlib and seaborn.

## Contact information <a name="contact"></a>
My email is **alisyedhaider627@gmail.com** if you want to reach out to me for questions, feedback, or support.
