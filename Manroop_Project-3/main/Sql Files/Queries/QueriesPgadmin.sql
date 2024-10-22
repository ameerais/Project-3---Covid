--Query to compare vaccination rates and case counts for countries
SELECT location, SUM(total_vaccinations) AS total_vaccinations, 
                 SUM(total_cases) AS total_cases
FROM covid_vaccinedata_2021
GROUP BY location
ORDER BY total_vaccinations DESC;

--Query to find death to case ratio in all the countries
SELECT location, SUM(total_deaths) / SUM(total_cases) AS death_to_case_ratio
FROM covid_vaccinedata_2021
GROUP BY location
ORDER BY death_to_case_ratio DESC;

-- Query to find out if there is a connection between deaths and vaccine type
SELECT vaccine_types_used, SUM(total_deaths) AS total_deaths
FROM covid_vaccinedata_2021
GROUP BY vaccine_types_used
ORDER BY total_deaths DESC;
--This result does not give an output that can be used for visualization

--The above query is being broken down by countries
SELECT location, vaccine_types_used, SUM(total_deaths) AS total_deaths
FROM covid_vaccinedata_2021
GROUP BY location, vaccine_types_used
ORDER BY total_deaths DESC;

--Query to make the data more comparable
SELECT location, vaccine_types_used, 
       SUM(total_deaths) / SUM(total_cases) AS death_rate
FROM covid_vaccinedata_2021
GROUP BY location, vaccine_types_used
ORDER BY death_rate DESC;

--Did the number of doses have an impact on the deaths
SELECT location, SUM(people_fully_vaccinated) AS fully_vaccinated, 
                 SUM(total_deaths) AS total_deaths
FROM covid_vaccinedata_2021
GROUP BY location
ORDER BY fully_vaccinated DESC;

--Query to find counties with most vaccinations
SELECT location, SUM(total_vaccinations) AS total_vaccinations
FROM covid_vaccinedata_2021
WHERE year = 2021
GROUP BY location
ORDER BY total_vaccinations DESC;

--Query to find countries with most deaths
SELECT location, SUM(total_deaths) AS total_deaths
FROM covid_vaccinedata_2021
WHERE year = 2021
GROUP BY location
ORDER BY total_deaths DESC;

--Query to compare people vaccinates with people fully vaccinated and death rates 
SELECT location, 
       SUM(people_vaccinated) AS total_vaccinated_one_dose,
       SUM(people_fully_vaccinated) AS total_fully_vaccinated,
       SUM(total_deaths) AS total_deaths
FROM covid_vaccinedata_2021
GROUP BY location
ORDER BY total_fully_vaccinated DESC;


