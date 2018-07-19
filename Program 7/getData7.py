#Salman Omar section 3
from class7 import *
from math import *


def getData():
    
    #Create a appointment details list
    
    aptDetails = []
    with open("dates.txt","r") as l:
        for line in l:
            #Separate the input by commas
            line=line.split(",")
            #Occurence
            occurence = (line[0])
            #Month
            month = int(line[1])
            #Day
            day = int(line[2])
            #Year
            year = int(line[3])
            #Time
            time = (line[4])
            #Type of Job being Done
            typeJob = (line[5])

            #Conditional Statements
            if occurence == ("Monthly"):
                typeOfapt = Monthly(month, day, year, time, typeJob)
                aptDetails.append(typeOfapt)
                
            elif occurence == ("Daily"):
                typeOfapt = Daily(month, day, year, time, typeJob)
                aptDetails.append(typeOfapt)

            elif occurence == ("OneTime"):
                typeOfapt = Onetime(month, day, year, time, typeJob)
                aptDetails.append(typeOfapt)
                
    return aptDetails


            

    

            
            
            
            


