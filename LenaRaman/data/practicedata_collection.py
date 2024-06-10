#practice for importing one data file and plotting it

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob

GSHPEG_file = '/Users/lenahsia/PycharmProjects/LenaRaman/data/RawData/10mM_GSH_PEG_1_580nm_30sec_150gg67112_1.txt'
GSHPEG_data = np.genfromtxt(fname=GSHPEG_file, delimiter = ',', dtype = 'unicode')

#displaying and printing the data frame GSHPEG_data
df = pd.DataFrame(GSHPEG_data)

#save to csv (practice for saving dataframe before dropping)
df.to_csv('GSHPEG_dataoutput.csv',index=False)

#read df
df_from_csv= pd.read_csv('GSHPEG_dataoutput.csv')

#dropping
df_dropped_column = df.drop(columns= [1])

#add labels with rename function to dropped dataframe
df_droppedrenamed = df_dropped_column.rename(columns={0: 'raman shift', 2:'intensity'})
print("\nRenamed dropped Dataframe :")
print(df_droppedrenamed)
#not string its an int, so no brackets or quotes around 0 and 1
#string has quotes
#int has no quotes

#make a plot of the dropped dataframe
plt.figure(figsize=(10,5))
plt.plot(df_droppedrenamed['raman shift'], df_droppedrenamed['intensity'], ".", markersize=2)
plt.title("10 mM GSH in PEG 30Sec 150 sample 1", fontsize=10)
plt.xlabel('Raman Shift', fontsize=10)
plt.ylabel('Intensity', fontsize=10)
plt.xticks(np.arange(0, 1500, 100),fontsize = 7)
plt.yticks(np.arange(0, 1300, 100), fontsize=7)
#why is the intensity not increasing linearly
plt.show()






























