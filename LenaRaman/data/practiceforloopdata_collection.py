#practice for importing multiple data files and plotting it using a for loop

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob
#use a for loop to read each file
#make a for loop for all GSH in PEG 30 sec 150 samples

GSHPEG_files = glob.glob('/Users/lenahsia/PycharmProjects/LenaRaman/data/RawData/10mM_GSH_PEG_*_580nm_30sec_150*.txt')

for GSHPEG_file in GSHPEG_files:
    GSHPEG_data = np.genfromtxt(fname=GSHPEG_file, delimiter=',', dtype='unicode')
    df = pd.DataFrame(GSHPEG_data)
    #read the data file into a dataframe

    df1 = pd.read_csv('fileinGSHPEG.csv')
    #drop [1] column
    if 1 in df.columns:
        df_dropped_column = df.drop(columns=[1])
    else:
        df_dropped_column = df

    #rename columns
    if 0 in df_dropped_column.columns and 2 in df_dropped_column.columns:
        df_droppedrenamed = df_dropped_column.rename(columns={0: 'raman shift', 2:'intensity'})
    else:
        df_droppedrenamed = df_dropped_column

#numeric
    df_droppedrenamed['raman shift'] = pd.to_numeric(df_droppedrenamed['raman shift'])
    df_droppedrenamed['intensity'] = pd.to_numeric(df_droppedrenamed['intensity'])
    print("\nRenamed dropped Dataframe :" )
    print(df_droppedrenamed)

    plt.figure(figsize = (10, 5))
    plt.plot(df_droppedrenamed['raman shift'], df_droppedrenamed['intensity'], ".", markersize=2)
    plt.title("10 mM GSH in PEG 30Sec 150 ", fontsize=10)
    plt.xlabel('Raman Shift', fontsize=10)
    plt.ylabel('Intensity', fontsize=10)
plt.show()













