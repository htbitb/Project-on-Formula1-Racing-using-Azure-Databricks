## Real World Project on Formula1 Racing using Azure Databricks

### Project Overview

This project is created to implement a data engineering solution using Azure Databricks and Spark core for a real world project of analysing and reporting on Formula1 motor racing data.

![alt text](/source/databricks_overview.png)


### What will we learn about?
**Azure Databricks**

* Building a solution architecture for a data engineering solution using Azure Databricks, Azure Data Lake Gen2, Azure Data Factory and Power BI

* Creating and using Azure Databricks service and the architecture of Databricks within Azure

* Working with Databricks notebooks as well as using Databricks utilities, magic commands etc

* Passing parameters between notebooks as well as creating notebook workflows

* Creating, configuring and monitoring Databricks clusters, cluster pools and jobs

* Mounting Azure Storage in Databricks using secrets stored in Azure Key Vault

* Working with Databricks Tables, Databricks File System (DBFS) etc

* Using Delta Lake to implement a solution using Lakehouse architecture

* Creating dashboards to visualise the outputs

* Connecting to the Azure Databricks tables from PowerBI
  

<br>


**Spark (Only PySpark and SQL)**

* Spark architecture, Data Sources API and Dataframe API

* PySpark - Ingestion of CSV, simple and complex JSON files into the data lake as parquet files/ tables.

* PySpark - Transformations such as Filter, Join, Simple Aggregations, GroupBy, Window functions etc.

* PySpark - Creating local and temporary views

* Spark SQL - Creating databases, tables and views

* Spark SQL - Transformations such as Filter, Join, Simple Aggregations, GroupBy, Window functions etc.

* Spark SQL - Creating local and temporary views

* Implementing full refresh and incremental load patterns using partitions


<br>

**Delta Lake**

* Emergence of Data Lakehouse architecture and the role of delta lake.

* Read, Write, Update, Delete and Merge to delta lake using both PySpark as well as SQL 

* History, Time Travel and Vacuum

* Converting Parquet files to Delta files

* Implementing incremental load pattern using delta lake

<br>

**Azure Data Factory**

* Creating pipelines to execute Databricks notebooks

* Designing robust pipelines to deal with unexpected scenarios such as missing files

* Creating dependencies between activities as well as pipelines

* Scheduling the pipelines using data factory triggers to execute at regular intervals

* Monitor the triggers/ pipelines to check for errors/ outputs