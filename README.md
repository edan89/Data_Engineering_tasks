This repository showcases my experience in data engineering and analytics, including data ingestion, transformation, and analysis using Python, SQL, SQLite, and BigQuery. 
I worked with real-world datasets, built ETL pipelines, performed data quality validation, created visualizations and dashboards, and deployed applications using Docker, Airflow, Kafka, and Streamlit, both locally and in cloud environments.

I went through the next exercises which now I'm able to understand and apply:

Exercises

1:  Read Global temperature data from Github. 

a) Save it to both a local .csv file and a SQLite database.
b) Convert time information to Pandas datetime format and Unix epoch.
c) Convert data to the format, where the data source is the column header. 
d) Compare observations from two sources (when both are available).
e) Visualise global temperature trends (separately from two sources).
f) Estimate future temperatures using interpolation methods.

2: The zip package contains of seven .csv files. Download the package, extract the files and carry out the following:

a) Create SQL database company_database.db where each csv file appears as a table. Use SQLite
b) Query project id, employee id and hours worked from employee_projects and employee id's and salaries from employees_realistic. Join them on employee id.
c) Calculate the salary costs per project, assuming that the employers salary is annual and number of working hours is 1900 per year. 
d) Join this with the budget in projects table
e) Calculate how large fraction of the project budget the salary costs are.

You can use VS code SQL or Python SQLite in the task 2 b - e. 
Example of the output of the query in 2e

3.Use company database from Exercise 2. Use SQLite and query the daily total amount of sales from table orders. Make a line plot of daily sales using matplotlib.pyplot

4: Use penguins data  (bigquery-public-data.ml_datasets.penguins). Write a query to calculate the average body mass, culmen length and culmen depth for females and males in different islands. Use BigQuery Console and save results first to Google Sheets and then to BigQuery table.

5: Estimate data storage costs over five years in BigQuery for a company that collects 5 Gb of data every day and keeps all the old data. 

6: Use World Bank population data (bigquery-public-data.world_bank_global_population.population_by_country). Query entire data set to your computer using BigQuery API. Transform the data in Python to the format where the first column is year, other columns are populations in countries. Create table for population in Nordics (headers will be ['year','Finland','Sweden','Norway','Denmark','Iceland’]). Upload this table to BigQuery using API.

7: Use BigQuery public data for names in USA (`bigquery-public-data.usa_names.usa_1910_current`). Write a query to find the most common male and female name for every year. Save results to table US_common_names. Use BigQuery API and action query in a way that the data is not moved from BigQuery.

8. Write a Jupyter notebook to complete the following tasks.
a) Query raw data from Google Analytics 4 example table bigquery-public-data.ga4_obfuscated_sample_ecommerce  from the time range  from 2021-01-15 to  2021-01-31 (WHERE _TABLE_SUFFIX between '20210115' and  '20210131') Query user_pseudo_id, number of events and total revenue per user. 
b) Save query results to the destination BigQuery table. Note that data should stay in BigQuery during the processing, don’t download a local copy! The destination should be under your own project and data set, like my_project_name.G4_daily_user.G4_daily_user_data. You need to create the data set in the BigQuery console
c) Query data from the table you created. Import data to the local pandas dataframe.
d) Visualize basic quantities, like a bar chart of revenue for the top 20 customers. 

9: Create a Docker image and container using this data visualization and related data file from earlier course.

10. Polar Sportswatch saves exercise data to JSON files; each training session produces one JSON.
a) Write a Python program to read general information from all the files to one CSV-file
b) Visualize basic quantities using Streamlit
c) Write a program to visualize data from one exercise. You can have line plot, bar charts, maps (folium), etc.
You can see some tips from this Notebook

11. Make sure you have completed this example from lecture: Load data file cars.csv from Moodle
a) Install Pandas profiler (see script example) and Great Expectations (you can also try Openrefine)
b) Examine using Pandas profiler and Great Expectations. You can also test OpenRefine
c) Do you find quality issues?
d) Can they be fixed?

12. The data file titanic.csv contains a fraction of the Titanic passenger list, but some values are erroneous.

a) What could be the validation criteria for each column? In other words, how the data in each column should be. Note that all the columns don't have very strong validation criteria and sometimes you have to investigate the data before defining the criteria.
b) Investigate the data quality using Python Pandas Profiler, Openrefine and/or Great Expectations
c) Describe the possible errors you found in each column and how you could fix them (if possible, no need to fix them)
 
13. Tempereture observations have some gaps.
a) Investigate the fraction of missing data
b) Fill the gaps using different interpolation methods
c) Investigate how different methods perform statistically and compare results visually
Tip: Pandas interpolate, methods: ['linear', 'time', 'index', 'values', 'nearest', 'zero', 'slinear', 'quadratic', 'cubic', 'barycentric', 'krogh', 'spline', 'polynomial', 'from_derivatives', 'piecewise_polynomial', 'pchip', 'akima', 'cubicspline']
Example: df3['column'].interpolate(method='cubicspline', limit=10)
 

14. Let's assume that you are collecting training data from multiple persons for scientific purposes. The goal is to have a SQL database and related visualisations that contain the following:
- Long-term general statistics that aggregate all the users
- Long-term statistics for individual users 
- Exercise-specific statistics for individual users
Assume that the raw data format is the JSON data in exercise 10.
Create the plans for:
a) Conceptual, logical and physical data model.
b) Related DAG workflow. 
c) Related data quality measures.
Note that you don't need to include all the observations and parameters. The aim of this exercise is to see the "big picture" and understand how data processing takes place.

15: Install Kafka using WSL and Docker and complete the following:
a) Write a producer that checks whether some information has changed (like electricity price or stock price) and sends new information to Kafka. 
b) Write a listener that reads new data from Kafka and saves it to local file
c) Visualize data using Streamlit or some other Python library


16. Complete the following steps:

    [Install WSL https://learn.microsoft.com/en-us/windows/wsl/install and install Docker] <-- You should already have these
    Download docker-compose.yaml file from https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html
    Save yaml-file to folder Airflow and navigate there WSL
    Start container "sudo docker compose up" or "sudo docker compose up -d"
    Go to http://localhost:8080/ Some example DAGs should be visible there
    Containers are now also visible in Docker Desctop and you can easily start and pause them. 

17.  Create your first pipeline in Mage or Airflow. See DAG example and tutorials. [Note that Docker desktop is used in some videos (unless teacher finds time tu update them. ) However, this does not change the workflow at all. You'll use WSL terminal in a same way. The only difference is that there is no Windows UI, but it is not needed.]
The pipeline should do the following (in a same way as in exercise 5):

    Query some interesting data from BigQuery public data on the local machine
    Transform the data in Python and upload it back to BigQuery
    Carry out some transform also using action query, when data is not moved from BigQuery

18.  Create your CSC account and set up Ubuntu virtual machine

    Install Docker
    Use Dockerfile from Task 9, create image and run container or use Airflow or Kafka docker-compose.yaml file
    Configure that port needed is open to your local machine IP
    Check that you can find the program from selected port
