# Car_Rental_Database

This is the car rental database project, in which we are developing a graphical user interface (GUI) in Python by accessing the data from SQL database. <br />
#How to run
The image below shows how to start the GUI from your local computer's terminal or command prompt.

![image](https://user-images.githubusercontent.com/60457052/169611705-5c850102-f080-4df1-9625-93407ab0ae66.png) <br />

#Tools used:

•	Visual Studio Code (Python) or Text Editor (Notepad++).  <br />
•	SQLite 3.  <br />
•	Terminal or command prompt (To run the database (db.)).  <br />
•	GUI (Tkinter)   <br />
•	Word & Adobe  <br />


Steps that are required to install and run your program:  <br />
We were provided with .csv files which were loaded with data regarding the car rental database. To import the .csv files to the database (CarRental2019.db)  <br />

•	 Sqlite3  <br />
•	.open CarRental2019.db (This command opens the allocated database).  <br />
•	.headers on   <br />
•	.mode csv (Exports the SQLite table as CSV)   <br />
•	.import (Store values to tables).  <br />
•	.import CUSTOMER.csv CUSTOMER  <br />
•	.import RATE.csv RATE  <br />
•	.import RENTAL.csv RENTAL  <br />
•	.import VEHICLE.csv VEHICLE  <br />
•	.mode column (Each record is displayed on a separate line).   <br />
•	.schema (To check if all the schemas are in the correct order).  <br />


We used Python and the GUI Toolkit to execute the database's graphical user interface GUI. (Tkinter).  <br />
Commands to launch the GUI and check if your computer has the correct version of Python installed.  <br />
•	Python --version (Python 3.10.2)    <br />
Once we've verified that our computer has the correct Python version, we can execute the GUI with this command.  <br />
•	Python3 gui.py   <br />

#Screenshots
•	The image below explains how to use the commands to get into the database and evaluate the schemas within the database.  <br />

 ![image](https://user-images.githubusercontent.com/60457052/169611556-c17b54cc-ee74-4524-a4f6-ecdda47f8fab.png) <br />
 ![image](https://user-images.githubusercontent.com/60457052/169611570-34222f69-4a24-4bfd-a451-5b1d95bf8d89.png) <br />
 ![image](https://user-images.githubusercontent.com/60457052/169611623-374aa46f-83e6-4e64-9694-ba2e22b6f7be.png) <br />

The images above and below demonstrate the results of importing data from.csv files into the database and verifying that there are no errors or excess data. <br />
We double-check it in the SELECT line, making sure the columns are set to. mode columns so it prints with suitable spacing.	  <br />

![image](https://user-images.githubusercontent.com/60457052/169611655-69a84441-e4a3-4127-9cb0-d2305148f2df.png)  <br />
![image](https://user-images.githubusercontent.com/60457052/169611677-4b5317db-fe1d-403f-b2d6-8a9d21d69cdb.png)  <br />

The image below shows how to start the GUI from your local computer's terminal or command prompt.  <br />

![image](https://user-images.githubusercontent.com/60457052/169611705-5c850102-f080-4df1-9625-93407ab0ae66.png) <br />
