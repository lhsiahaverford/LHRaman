#scatter
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob

#for datafile 1
GSHPEG_file = '/Users/lenahsia/PycharmProjects/LenaRaman/data/RawData/10mM_GSH_PEG_1_580nm_30sec_150gg67112_1.txt'
GSHPEG_data = np.genfromtxt(fname=GSHPEG_file, delimiter = ',', dtype = 'unicode')

#displaying and printing the data frame GSHPEG_data
df = pd.DataFrame(GSHPEG_data)

#dropping
df_dropped_column = df.drop(columns= [1])

#add labels with rename function to dropped dataframe
df_droppedrenamed = df_dropped_column.rename(columns={0: 'raman shift', 2:'intensity'})
#converting the values to numerical values (int or float) from a str
df_droppedrenamed['raman shift'] = pd.to_numeric(df_droppedrenamed['raman shift'])
df_droppedrenamed['intensity'] = pd.to_numeric(df_droppedrenamed['intensity'])
print("\nRenamed dropped Dataframe 1 :")
print(df_droppedrenamed)
#not string its an int, so no brackets or quotes around 0 and 1
#string has quotes
#int has no quotes

#for datafile 2

GSHPEG_file2 = '/Users/lenahsia/PycharmProjects/LenaRaman/data/RawData/10mM_GSH_PEG_1_580nm_30sec_150gg67125_1.txt'
GSHPEG_data2 = np.genfromtxt(fname=GSHPEG_file2, delimiter = ',', dtype = 'unicode')

#displaying and printing the data frame GSHPEG_data
df = pd.DataFrame(GSHPEG_data2)

#dropping
df_dropped_column2 = df.drop(columns= [1])

#add labels with rename function to dropped dataframe
df_droppedrenamed2 = df_dropped_column2.rename(columns={0: 'raman shift', 2:'intensity'})
df_droppedrenamed2['raman shift'] = pd.to_numeric(df_droppedrenamed2['raman shift'])
df_droppedrenamed2['intensity'] = pd.to_numeric(df_droppedrenamed2['intensity'])
print("\nRenamed dropped Dataframe 2 :")
print(df_droppedrenamed2)
#not string its an int, so no brackets or quotes around 0 and 1
#string has quotes
#int has no quotes

#plot

plt.plot(df_droppedrenamed['raman shift'], df_droppedrenamed['intensity'], label='data 1', c="blue")
plt.plot(df_droppedrenamed2['raman shift'], df_droppedrenamed2['intensity'], label='data 2', c="red")
plt.title("10 mM GSH in PEG 30Sec 150 ", fontsize=10)
plt.xlabel('Raman Shift', fontsize=10)
plt.ylabel('Intensity', fontsize=10)
plt.legend(fontsize=10)
plt.show()



