# 

#this file will move the rows which has first column value empty to the end of the file
import os
import csv
from operator import itemgetter
path='C:/Users/Fariba Afrin Irany/Documents/unt/No_empty_row_file' 

# Python program to copy or clone a list 
# Using the Slice Operator 
def Cloning(li1): 
    li_copy = li1[:] 
    return li_copy 

# Python code to sort the tuples using second element  
# of sublist Inplace way to sort using sort() 
def Sort(sub_li): 
  
    # reverse = None (Sorts in Ascending order) 
    # key is set to sort using second element of  
    # sublist lambda has been used 
    sub_li.sort(key = lambda x: x[1]) 
    return sub_li

def Main():    
    for filename in os.listdir(path):  
      File_Path=filename  
      f = open(r'C:/Users/Fariba Afrin Irany/Documents/unt/No_empty_row_file/{}'.format(File_Path))
      csv_f = csv.reader(f)
      i=1
      #all the with first val empty are put in a separate list
      first_row_empty=[]
      #all the with first val empty are put in a separate list
      first_row_not_empty=[]
      #list that contain the header 
      header=[]
      for row in csv_f:
        if row[0]=='':
          first_row_empty.append(row)
          # print(row)
        else:
          #header row
          if i==1: 
            header.append(row)
          else:
            first_row_not_empty.append(row)
          i=i+1
      outvalue=  filename.split(".")
      # opening the csv file in 'w+' mode 
      file = open(r'C:/Users/Fariba Afrin Irany/Documents/unt/empty_first_attribute_at_end_file/{}.csv'.format(outvalue[0]), 'w+', newline ='') 
        
      # get the index of the last row of the csv which does not have empty first column 
      
      # writing the data into the file 
      with file:     
          write = csv.writer(file) 
          write.writerows(header) 
          write.writerows(first_row_not_empty) 
          write.writerows(first_row_empty)
       
if __name__=="__main__": 
    Main() 

