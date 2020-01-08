## Snowflake
* https://www.snowflake.com/
* TLDR: Snowflake is a cloud-based Data Warehouse solution provided as a Saas (Software-as-a-Service) with full support for ANSI SQL. It also has a unique architecture that enables users to just create tables and start querying data with less administration or DBA activities needed.

* natively load and use SQL to query semi-structured and structured data within a single system
* near-zero management solution - no need to create partitions, indexes like in RDBMS or run vacuum operations like in Redshift either.
* Time Travel allows you to track the change of data over time. This Snowflake feature is available to all accounts and enabled by default to all, free of cost.  This feature allows us to access the historical data of a Table. One can find out how the table looked at any point in time within the last 90 days.
* We can use clone feature to create an instant copy of any Snowflake object such as databases, schemas, tables, and other Snowflake objects at a near real-time without much waiting time.
* Snowflake provides various connectivity options including Native connectors (e.g. Python), JDBC/ODBC drivers, Command Line tool called `SnowSQL`,  Web Interface which helps to manage Snowflake as well as to query the data.
* Snowflake account can be hosted on either Amazon AWS or Microsoft Azure cloud platform.
* Snowflake data warehouse charges for the Storage and Compute separately. Snowflake provides $400 free credits to try and explore the warehouse.

## Data_warehouse
* https://en.wikipedia.org/wiki/Data_warehouse -> a data warehouse (DW or DWH), is a system used for reporting and data analysis, and is considered a core component of business intelligence. DWs are central repositories of integrated data from one or more disparate sources