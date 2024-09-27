#filters runs from a route

import pandas as pd
import numpy as np
import os

gtfs_folder = '' #put stuff in here if you want this to run

gtfs_Files = os.listdir(gtfs_folder)

gtfs_data = {}

for gtfs_file in gtfs_Files:
    gtfs_name = gtfs_file.replace(".txt","")
    gtfs_data[gtfs_name] = pd.read_csv(os.path.join(gtfs_folder,gtfs_file))

route = 331009
print(gtfs_data['trips'].iloc[0])
trips_filtered = gtfs_data['trips'].loc[gtfs_data['trips']['route_id'] == route]
print(trips_filtered)

print(len(gtfs_data['stop_times']))

stoptimes_filtered = gtfs_data['stop_times'].loc[gtfs_data['stop_times']['trip_id'].isin(trips_filtered['trip_id'].tolist())] 
print(len(stoptimes_filtered))

#print(stoptimes_filtered)
stoptimes_filtered.to_csv(os.path.join(gtfs_folder,'stop_times_new.txt'),index=False)
