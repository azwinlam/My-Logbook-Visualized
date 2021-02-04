# My Logbook Visualized: Project Overview 
* Created a python script that can take the standardized digital logbook issued by Cathay Pacific Group and produce simple graphs that give some insight on the pilot's career.


## Code and Resources Used 
**Python Version:** 3.9.1 
**Packages:** pandas, numpy, seaborn, matplotlib, dateutil

## Importing the data
*The logbook is given in a .txt format. The easiest method to convert the .txt to csv is to import it using Excel and add External Data. Pandas does have a read_fwf function but the output was not in a clean format.

## Data Cleaning
The columns were quite clean as this was a computer generated file and flight records were complete. I split the city pairs into origin and destination for easier analysis. The date/time of flight was changed into datetime dtype using pandas.to_datetime.

## EDA
Below are the highlights from the logbook visualization

![alt text](https://github.com/azwinlam/My-Logbook-Visualized/blob/master/Which%20route%20did%20I%20fly%20most.png "Which route did I fly most.png")
![alt text](https://github.com/azwinlam/My-Logbook-Visualized/blob/master/Which%20aircraft%20type%20did%20I%20fly%20most.png "Which aircraft type did I fly most.png")
![alt text](https://github.com/azwinlam/My-Logbook-Visualized/blob/master/Which%20captain%20did%20I%20fly%20with%20most%20by%20sectors.png "Which captain did I fly with most by sectors.png")
![alt text](https://github.com/azwinlam/My-Logbook-Visualized/blob/master/Cockpit%20Hours%20Shared%20Top%2030%20Commanders.png "Cockpit Hours Shared Top 30 Commanders.png")
![alt text](https://github.com/azwinlam/My-Logbook-Visualized/blob/master/Which%20aircraft%20type%20did%20I%20fly%20most.png "Sectors By Airframe.png")
![alt text](https://github.com/azwinlam/My-Logbook-Visualized/blob/master/Destinations%20Count%20Not%20Hong%20Kong.png "Destinations Count Not Hong Kong.png"
