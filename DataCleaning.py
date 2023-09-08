'''Data Cleaning'''
import csv

read_file = csv.reader(open("Data1002.csv"))

data_list = list(read_file)

#Removes the heading table 1 (This was created when converting to csv)
data_list.remove(data_list[0])

#This list contains the rows without missing data values
new_list = [] 
for row in data_list:
    if '' in row:
        pass
    else:
        new_list.append(row)

w_file = open("Data1002_Cleaned.csv", 'w')


# This counter checks if there are any invalid data, eg time has to be above 0
counter = 0
first_row = True
for row in new_list:
    if first_row:
        first_row = False
        pass

    else:
        #Change miliseconds to hours
        row[-1] = (float(row[-1])/3600000)
        #3 decimal points
        row[-1] = "{:.3f}".format((row[-1]))
        row[-2] = (float(row[-2])/3600000)
        row[-2] = "{:.3f}".format((row[-2]))

        if (float(row[-1]) < 0 or float(row[-2]) < 0):
            counter +=1
            

   
print(counter)
write_file = csv.writer(w_file)
#Creates a csv file of the new cleaned data
for row in new_list:
    write_file.writerow(row)




    
