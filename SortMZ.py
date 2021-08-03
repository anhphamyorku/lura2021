# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 23:51:37 2021

@author: Michael
"""
#import csv library
import csv

#This part of code will filter the molecular weeight that we interest in
with open('lib1.csv') as f:
    readWord = csv.reader(f, delimiter = ',')
    #MWlist array will confirm that the amount of peptide we filtred is correct 
    MWlist = []
    #numLines array will store the lines enumaration 
    numLines = []
    for lines, row in enumerate(readWord):
        for t in row[0].split():
            if "MW" in row[0]:
                try:
                    #The if condition is where we can adjust the MW parameter that we interest in
                    if 2000 <= float(t) < 2001:
                        #Store the content filtered in the arrays
                        MWlist.append(float(t))
                        numLines.append(lines)
                except ValueError:
                    pass
#Print out the MW list in the console.                
print(MWlist)             

#This part of the code will store the number of mass per charge peaks of the filtered peptide                   
with open('lib1.csv') as f:
    numPeaks = []
    readWord = csv.reader(f, delimiter = ',')
#Using the numLines array, since the format is constant with these library
#We just take 2 lines after the MW line, which is where the number of peaks located    
    for lines, row in enumerate(readWord):
        for t in row[0].split():
            #Going through the numLines array
            for n in numLines:
                try:
                    #Moves down by 2 lines, and store the numerical information in the array called numPeaks
                    if lines == n+2:
                        numPeaks.append(float(t))
                except ValueError:
                        pass
   
#This part will write a new csv file of the lines stored in the arrays
with open('lib1.csv') as f, open('newOutFile.csv', "w",newline='') as o:
    readWord = csv.reader(f, delimiter = ',')
    writer = csv.writer(o, delimiter = ',')
    #Create two counters
    counter = 0
    temp = 0
    while counter < len(numLines):
        for lines, row in enumerate(readWord):
            try:
                #If the lines are within the range of the numLines and numLines + numPeaks, write to new csv
                #Note that the numLines - 1 and numLines+numPeaks+3 is to ensure that the name and comments of the 
                #peptides are included as well, and the format stay consistent with the original file.
                if numLines[counter] - 1 <= lines < (numLines[counter] + numPeaks[counter] + 3):
                    writer.writerow(row)
                    temp += 1
                    if temp == numPeaks[counter] + 4:
                        counter += 1
                        temp = 0
            except IndexError:
                        pass
        

                             