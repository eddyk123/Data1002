'''Data Summaries'''
import csv
#Total amount of days
count = 0

sum_total_time_in_bed = 0
sum_total_slept = 0
csv_read= csv.reader(open("Data1002_Cleaned.csv"))

'''Calculating the Average time '''
list_of_sleeptime = []
list_of_bedtime = []
first_row = True
for row in csv_read:
    count +=1
    if first_row:
        first_row = False
        pass
    else:
        list_of_bedtime.append(float(row[-2]))
        list_of_sleeptime.append(float(row[-1]))
        sum_total_time_in_bed += float(row[-2])
        sum_total_slept += float(row[-1])

average_time_in_bed = sum_total_time_in_bed / count
average_time_slept = sum_total_slept / count
average_time_in_bed = "{:.3f}".format(average_time_in_bed)
average_time_slept = "{:.3f}".format(average_time_slept)
print(f"Average Time in bed : {average_time_in_bed} hours")
print(f"Average Time slept : {average_time_slept} hours")

'''Max and Lowest Sleep Time'''

print(f"Highest Sleep Time : {max(list_of_sleeptime)} hours")
print(f"Lowest Sleep Time : {min(list_of_sleeptime)} hours")

'''Correlation Coefficient BedTime vs SleepTime'''

import numpy as np

correlation = np.corrcoef(list_of_bedtime, list_of_sleeptime)[0, 1]
print("Correlation coefficient:", correlation)

'''Sleep Efficiency (This measures the percentage of time spent in bed that is actually spent asleep)'''
efficiency = (sum_total_slept/ sum_total_time_in_bed)*100
print(f"Sleep Efficiency percentage = {efficiency:.3f}")

