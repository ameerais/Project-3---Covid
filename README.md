COVID-19 Vaccination Data Analysis & Visualization Project
Overview- For this part of the project we have focused on analyzing and visualizing data related to COVID-19 cases, vaccinations, and deaths across various countries in 2021. 
This analysis is aimed at answering some common questions regarding the relationship between vaccination status and the number of COVID-19 cases, as well as examining which types of vaccines were most commonly used.

The data used in this project was sourced from: Kaggle: For COVID-19 case counts and vaccination data.

https://www.kaggle.com/datasets/digvijaysinhgohil/covid19-data-deaths-and-vaccinations
https://www.kaggle.com/datasets/gpreda/covid-world-vaccination-progress
https://www.kaggle.com/datasets/gpreda/covid-world-vaccination-progress?select=country_vaccinations_by_manufacturer.csv
Using data from 2021, we used Python (pandas, matplotlib) and Flask API for visualizations, building graphs, and analyzing the trends.

Project Purpose-The project aims to provide insights into:
How vaccination progress relates to the number of new cases and deaths ?
Which countries had the most cases, deaths, and vaccinations.

Technologies Used- Python was used for data processing, cleaning, and visualization with libraries like pandas, matplotlib, Flask.
Flask API was used to serve the data and visualizations.
SQL was used for querying and database usage.

Files and Structure
The project consists of the following key files- The file app.py is the Flask API backend for serving data and rendering HTML templates.
Vaccination.ipynb is a Jupyter Notebook used for data cleaning, analysis, and generating visualizations.
Resources/: This folder contains the various CSV files used in the project, including country_vaccinations.csv, covid_data_cleaned.csv,merged_df_2021_cleaned.csv
and index.html which is the front-end HTML page that displays visualizations through Flask.

How to Use the Project- Running the Vaccination.ipynb where the cleaning, analysis and visualizations can be explored.
The notebook uses the cleaned data from merged_df_2021_cleaned.csv to create various insights into cases, deaths, and vaccinations.
Then the app.py application after that open your browser and go to http://127.0.0.1:5000 to interact with the visualizations.

Key Analysis-
Scatter Plot Analysis: It showed relationships between vaccination counts and new cases/deaths caused by Covid-19. 
R-squared values were calculated to quantify the strength of the relationships.

Bar Graphs: It helped to identify which vaccines were most commonly used and how countries compared in terms of COVID-19 metrics like cases and deaths.
Top 10 Countries with the most cases, deaths, and vaccinations were identified using SQL and pandas.

Ethical Considerations- Since, the data used in this project relates to public health and personal well-being, it was important to handle the data responsibly.
Therefore, the dataset used does not contain personal identifiers and represents aggregated public health data.
No sensitive information was exposed or misused in this project.

