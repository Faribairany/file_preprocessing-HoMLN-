# import csv


# with open('unt_1.csv') as in_file:
#     with open('unt_1_out.csv', 'w',newline='') as out_file:
#         writer = csv.writer(out_file)
#         for row in csv.reader(in_file):
#             if any(row):
#                 writer.writerow(row)

# print('hello')
# import pandas as pd
# df = pd.read_csv('unt_1.csv')
# df.to_csv('unt_1_output.csv', index=False)

# import pandas as pd
# df = pd.read_csv('unt_1.csv')
# #checking the number of empty rows in th csv file
# print (df.isnull().sum())
# #Droping the empty rows
# modifiedDF = df.dropna()
# #Saving it to the csv file 
# modifiedDF.to_csv('unt_1out.csv',index=False)

import os
import csv
path='C:/Users/Fariba Afrin Irany/Documents/unt/inputfile'
  
def Main():    
    for filename in os.listdir(path):  
        File_Path=filename  
        outvalue=  filename.split(".")                  
        with open(r'C:/Users/Fariba Afrin Irany/Documents/unt/inputfile/{}'.format(File_Path)) as input_file:
              # file_name="C:/Users/Fariba Afrin Irany/Desktop/ra-multicode/No_empty_row_file/unt_{}.csv".format(outvalue[0])
              with open(r'C:/Users/Fariba Afrin Irany/Documents/unt/No_empty_row_file/{}.csv'.format(outvalue[0]),'w',newline='') as out_file:
                writer = csv.writer(out_file)
                for row in csv.reader(input_file):
                    if any(row):
                        writer.writerow(row)
                        # file_name_array=File_Path.split('.')

if __name__=="__main__": 
    Main() 