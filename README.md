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

# Correlation Between Cases and Healthcare Systems
Overview:
This data analysis focused on the correlation between COVID-19 cases and various healthcare system factors across different countries. The goal is to explore how healthcare infrastructure, public health policies, and socioeconomic conditions have influenced the spread and impact of COVID-19.

Contents:
Data: Datasets related to COVID-19 cases, healthcare spending, testing rates, vaccination rates, and socioeconomic indicators.
Analysis: Analysis code and visualizations.
Results: Summary of findings and correlations observed from the analysis.
References: Sources of data and literature relevant to the analysis.

Analysis Workflow:
Data Preparation: Import datasets and clean the data for analysis.
Exploratory Data Analysis (EDA): Visualize trends and correlations between COVID-19 cases and healthcare metrics.
Statistical Analysis: Conduct correlation analyses to determine relationships.
Results Interpretation: Summarize key findings and their implications.

Key Findings:
- Countries with strong healthcare infrastructure exhibited better management of COVID-19 cases.
- Early testing and tracing efforts significantly reduced transmission rates.
- Higher healthcare spending correlated with lower case fatality rates.
- Vaccination rates played a crucial role in decreasing severe cases.

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

#Relationship between COVID-19 cases and racial/ethnic groups 

In this part we are going to tackle the following question:
'Is there a relationship between racial and ethnic groups with the number of COVID-19 Cases? 

In order to answer the following question we chose a dataset called "COVID-19_Cases_and_Deaths_by_Race_Ethnicity_-_ARCHIVE.csv"

The first step, we loaded the dataset into a Pandas DataFrame. 
Before any analysis, we cleaned the columns names to avoid any errors when referring to specific columns later. 
Next, we dropped rows with missing values to have useful information 
We also filled missing values with 0 since the missing value implies that no cases or deaths were recorded for that group. 
We ensured the correct data types are being used which is integers in order to perform statistical analysis correctly. 
We then connected to SQLite Database, and verified that the data is in the database by querying the first 5 rows. Using an SQLite database helped make querying for specific race/ethnicity groups more efficient, especially when working with large datasets.
Because the data is in SQL, we ran a query to aggregate the total cases by race/ethnicity group. We got the total cases in descending order here. 
Before plotting charts, we make sure we are only working with rows where values are not missing - race/ethnicity and total cases and that the data type is correct. 
First, we plotted a bar chart of total cases to visualize. We found that NH White has the highest number of total cases. 
We then calculated descriptive statistics for cases by race/ethnicity
To make a fair comparison across different population sizes of different racial/ethnic groups, we calculated the case rate per 100,000 people - this helps us normalize the data. We represented that by doing a bar chart per 100k of COVID-19 case rates. The results were different here, and we can see that the Hispanic group.

This means that now we have two bar charts - one that shows the total number of cases by race/ethnicity and another showing the case rate per 100,000 people. This makes it easier to compare the impact. 

Total cases bar chart: larger groups such as NH White have more cases around 77 million simply because their population is larger 

Case rates per 100,000 people chart: we are normalizing the data here and notice that case rate is diferrent with Hispanic group having the highest case rates. 

The raw number of COVID-19 cases differs significantly across racial and ethnic groups, with larger population groups generally having more total cases. 
However, this raw number alone does not provide a clear picture of the impact on each group due to differences in population size. 
we can see that while some groups had higher total case numbers, when adjusted for population size, other groups were more severely impacted by the pandemic in terms of the proportion of their population that was infected
We additionally created a scatter plot between the total cases and total deaths to visually represent the relationship between both variables. 

Lastly, to answer our question we did a correlation analysis to see if there is a relationship between case rates and deaths.

The correlation between case_rates_per_100k to total deaths is 0.076 indicating a weak positive correlation suggesting that there is little to no linear relationship between these two. The number of cases does not predict the total number of deaths suggesting other factors (healthcare access, demographics) may play a larger role in determining death rates. 

However, when doing the correlation between the total cases and total death we get a value of 0.714 indicating a strong positive correlation. This means as the number of cases increases, the total number of deaths also tends to increase. Other factors like healthcase access, age distrbution, pre-existing conditions play a role which explains why the correlation is not perfect. This is expected and reflects the direct relationship between infections and fatalities.

This difference between the two correlations highlights the complexity of COVID-19 outcomes. While high case numbers generally lead to more deaths, other factors beyond infection rates, especially in vulnerable groups, seem to contribute heavily to mortality risk. This emphasizes the importance of considering socio-economic conditions, healthcare infrastructure, and public health interventions when addressing the pandemic's impacts on different communities.

We conclude that there is a clear relationship between racial and ethnic groups and the number of COVID-19 cases. Some groups were disproportionately affected when adjusting for population size, experiencing higher case rates per 100,000 people. However, the severity of the impact in terms of deaths is influenced by more than just the case numbers or infection rates—other socioeconomic and health factors likely contribute to the disparities in outcomes.




