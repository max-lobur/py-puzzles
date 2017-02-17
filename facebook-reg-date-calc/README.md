#### Puzzle: Calculate a date of registration of the Facebook user.

The application runs from the command-line and takes a path to a CSV file as  
the only argument. CSV file has the following field layout:

* fbid - integer 
* token - string 
* username - string 

Example:  
```
100015396787297,EAACEdEose0cBAIxO9eZCM,Mary Alaecifghgbig Seligsteinwitz
100015236059396,EAAaURUTPjEQBANp9bUVav,John Alaebcfjeicif Dinglesen
```

The program should calculate the approximate date of the user registration in  
Facebook for each record from the csv file. 

Result should be written to the console in following format:
```
username,fbid,registration_date. registration_date mask - %Y-%m-%d
```

Example out: 
```
Mary Alaecifghgbig Seligsteinwitz,100015396787297,2017-07-07
John Alaebcfjeicif Dinglesen,100015236059396,2016-05-01
```
