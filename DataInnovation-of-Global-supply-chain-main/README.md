# DataInnovation of Global Supply Chain

Coded with Python and MySQL database. The process is as follows:  
1. Assembled a web crawler using Python to scrape product resources from original data websites using urllib.  
2. Data processing using csv reader and pandas in Python to save the resources as csv files.  
3. Data insertion and update operations of MySQL database, as well as the realization of query optimization.    


There are 4 py files:  
1. "main.py" is to run the whole program.
2. "account.py" is to record 7 different accounts and log them into the original data website. Each account has a search limit, so the program will switch to a new account after the old account's search limit is used up.
3. "search.py" is the web crawler and store the data into the csv files. The program update the last searched good and the last searched page on the data website through json file.
4. "sql.py" is to log into the local database and read all the csv files and import the data into the database using MySQL.  


I have already store the all the data of "chips" including:(customs codes, product name, time range, importers and exporters, trading countries, and start port/destination port) exporting from China(CN) to the world from March, 2021 to June, 2021. The screenshots are posted.
