# COVID-19 Conditions Contributing to Deaths - Data Visualization Project

Overview: 
This project section explores the first research questions, the correlation between pre-existing conditions and their contribution to COVID-19 fatalities. The goal is to identify which conditions had the greatest impact on the severity of COVID-19 outcomes, specifically in terms of death rates. Using Python for data analysis and visualization, this project provides static and interactive plots to illustrate these relationships.

Features: 
i. Data Loading and Cleaning: Load raw data from publicly available datasets, clean the data, and filter relevant information.
ii. Database Integration: Store the cleaned dataset in an SQLite database, enabling fast querying for visualizations.
iii. Static and Interactive Visualizations: Generate both static (Matplotlib) and interactive (Plotly) plots to visualize the top 10 conditions contributing to COVID-19 deaths.
iv. User Interaction: The user can select from various types of visualizations via a command-line interface (CLI).
v. Modular Design: The project is structured with modular Python scripts for easier management and extensibility.


Data Source: 
The dataset used in this project comes from a public repository on Kaggle. The dataset provides information about pre-existing health conditions contributing to COVID-19 deaths.

Source: Kaggle - COVID-19 Conditions Contributing to Deaths
Description: The dataset contains information about pre-existing health conditions and their contributions to COVID-19-related deaths across different demographics in the United States. The data includes details such as the condition name, the number of deaths attributed to the condition, and demographic information about the affected individuals.
Dataset Fields
Condition: The name of the pre-existing condition contributing to the death.
Deaths: The total number of deaths where this condition was a contributing factor.
The data was filtered and cleaned to focus on the most relevant conditions contributing to COVID-19 fatalities.

Visualizations: 
Static Bar Chart (using Matplotlib): Generates and saves a bar chart showing the top 10 pre-existing conditions contributing to COVID-19 deaths.
Interactive Bar Chart (using Plotly): Opens an interactive bar chart in the browser, allowing users to explore the data dynamically.
Heat Map: An interactive map, visually representing the correlation between pre-existing conditions and death rates due to COVID-19. 

Ethical Considerations: 
This project considers ethical data usage and ensures that personal information is not included in the analysis. All data is anonymized, and only aggregated statistics about conditions and deaths are analyzed. Additionally, the project acknowledges that correlations between conditions and deaths do not imply causation, and care is taken in interpreting the results.



# COVID-19 Vaccination Type Data Analysis & Visualization Project
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

