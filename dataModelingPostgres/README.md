## Goals
Sparkify is an online music streaming application and they would like to improve the user experience. 
The aim of this database is to analyse user behaviour on the Songify app. The database allows a data analyst to examine past experiences by users in an attempt to give future recommendations to them based on things like artist, genre and popularity. 
For example: 
1. If a user listens to artist X, we can check the listening habits of all other users who listen to artist X. 
2. Check the main genre of music listened to by a user and offer additional songs from the same genre. 
3. Notice that in a recent timeframe a new song or artist is getting a lot of hits. Then offer songs from that artist to everyone. 

## How to run the Python scripts
1. Make sure all notebook kernals have been terminated. 
2. In the terminal run: *python create_tables.py*
3. In the terminal run: *python etl.py*

## Project Files
- create_tables.py : This is to be run at the begining of the project. It will make sure you are working with a clean DB by deleting tables if they exist and then creating them. 
- sql_queries.py : This file contains the DELETE, CREATE, INSERT queries to be used by the other files. DB schemas are defined here. 
- etl.ipynb : This is an notebook where extract transform and load jobs were practiced and a working solution was built using a subset of the data. 
- etl.py : This is a python script to be run in the terminal once everything above is working. It will create your DB and fill it with data from the json files in the data directory. 
- test.ipynb : This file can help you confirm the DB you created is acceptable and makes sense in terms of dataypes and constraints. 

## DB Schema
#### songplay
<table>
  <tr>
    <th>ColumnName</th>
    <th>DataType</th>
    <th>Constraint</th>
  </tr>
  <tr>
    <td>songplay_id</td>
    <td>varchar</td>
    <td>PRIMARY KEY, NOT NULL</td>
  </tr>
  <tr>
    <td>start_time</td>
    <td>timestamp</td>
    <td>NOT NULL</td>
  </tr>
    <tr>
    <td>user_id</td>
    <td>varchar</td>
    <td></td>
  </tr>
    <tr>
    <td>level</td>
    <td>varchar</td>
    <td></td>
  </tr>
    <tr>
    <td>song_id</td>
    <td>varchar</td>
    <td></td>
  </tr>
  <tr>
    <td>artist_id</td>
    <td>varchar</td>
    <td></td>
  </tr>
  <tr>
    <td>session_id</td>
    <td>varchar</td>
    <td></td>
  </tr>  
  <tr>
    <td>location</td>
    <td>varchar</td>
    <td></td>
  </tr>
  <tr>
    <td>user_agent</td>
    <td>varchar</td>
    <td></td>
  </tr>
</table>

#### users
<table>
  <tr>
    <th>ColumnName</th>
    <th>DataType</th>
    <th>Constraint</th>
  </tr>
  <tr>
    <td>user_id</td>
    <td>varchar</td>
    <td>PRIMARY KEY, NOT NULL</td>
  </tr>
  <tr>
    <td>first_name</td>
    <td>varchar</td>
    <td>NOT NULL</td>
  </tr>
    <tr>
    <td>last_name</td>
    <td>varchar</td>
    <td>NOT NULL</td>
  </tr>
    <tr>
    <td>gender</td>
    <td>char</td>
    <td></td>
  </tr>
    <tr>
    <td>level</td>
    <td>varchar</td>
    <td></td>
  </tr>
</table>

#### songs
<table>
  <tr>
    <th>ColumnName</th>
    <th>DataType</th>
    <th>Constraint</th>
  </tr>
  <tr>
    <td>song_id</td>
    <td>varchar</td>
    <td>PRIMARY KEY, NOT NULL</td>
  </tr>
  <tr>
    <td>title</td>
    <td>varchar</td>
    <td>NOT NULL</td>
  </tr>
    <tr>
    <td>artist_id</td>
    <td>varchar</td>
    <td>NOT NULL</td>
  </tr>
    <tr>
    <td>year</td>
    <td>int</td>
    <td></td>
  </tr>
    <tr>
    <td>duration</td>
    <td>float</td>
    <td></td>
  </tr>
</table>

#### artists
<table>
  <tr>
    <th>ColumnName</th>
    <th>DataType</th>
    <th>Constraint</th>
  </tr>
  <tr>
    <td>artist_id</td>
    <td>varchar</td>
    <td>PRIMARY KEY, NOT NULL</td>
  </tr>
  <tr>
    <td>name</td>
    <td>varchar</td>
    <td>NOT NULL</td>
  </tr>
    <tr>
    <td>location</td>
    <td>varchar</td>
    <td></td>
  </tr>
    <tr>
    <td>latitude</td>
    <td>float</td>
    <td></td>
  </tr>
    <tr>
    <td>longitude</td>
    <td>float</td>
    <td></td>
  </tr>
</table>

#### time
<table>
  <tr>
    <th>ColumnName</th>
    <th>DataType</th>
    <th>Constraint</th>
  </tr>
  <tr>
    <td>start_time</td>
    <td>timestamp</td>
    <td>PRIMARY KEY, NOT NULL</td>
  </tr>
  <tr>
    <td>hour</td>
    <td>int</td>
    <td></td>
  </tr>
    <tr>
    <td>day</td>
    <td>int</td>
    <td></td>
  </tr>
    <tr>
    <td>week</td>
    <td>int</td>
    <td></td>
  </tr>
  <tr>
    <td>month</td>
    <td>int</td>
    <td></td>
  </tr>
  <tr>
    <td>year</td>
    <td>int</td>
    <td></td>
  </tr>
  <tr>
    <td>weekday</td>
    <td>boolean</td>
    <td></td>
  </tr>
</table>

These schemas were designed off of the instructions and the datatypes were chosen based off an initial view of the data inside the json files. Datatypes where joins would be used were kept the same. A primary key and not null were implemented in places to prevent unecessary duplicated data or any data with errors like missing critical values. 

[Optional] Provide example queries and results for song play analysis.
