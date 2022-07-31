import os
import glob
import psycopg2
import datetime
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    # open song file
    df = pd.read_json(filepath,lines=True)

    # insert song record
    col=['song_id','title','artist_id','year','duration']
    song_data = df[col].values[0].tolist()
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    col=['artist_id', 'artist_name', 'artist_location', 'artist_latitude', 'artist_longitude']
    artist_data = df[col].values[0].tolist()
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    # open log file
    df = pd.read_json(filepath,lines=True)

    # filter by NextSong action
    df = df.loc[df['page']=='NextSong']

    # convert timestamp column to datetime
    dates=[]
    for i in df['ts']:
        dates.append(datetime.datetime.fromtimestamp(i/1000.0))
    df['DateTime']=dates
    dates=pd.Series(df['DateTime'])
    t=pd.DataFrame()
    t['start_time']=dates
    t['year']=dates.dt.year
    t['month']=dates.dt.month
    t['week']=dates.dt.week
    t['day']=dates.dt.day
    t['hour']=dates.dt.hour
    t['weekday']=2>dates.dt.day%7
    
    # insert time data records
    time_data = ()
    column_labels = ['start_time', 'hour', 'day', 'week', 'month', 'year', 'weekday']
    time_df = t[column_labels]

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df =df[['userId', 'firstName', 'lastName', 'gender', 'level']]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    songplayID=0
    for index, row in df.iterrows():
        songplayID+=1
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
            print(songid)
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (songplayID, row.DateTime,row.userId, row.level, songid, artistid, row.sessionId, row.location, row.userAgent)
        #print(songplay_data)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()