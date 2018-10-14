
from math import *
from SOClass import Student

def getData():
    
    #Create a student list and student id list
    StudentsList=[]
    StudentsId=[]
    with open("students.txt","r") as l:
        for line in l:
            #Separate the input by commas
            line=line.split(",")
            s=Student(line[1],line[2],line[3].strip(),line[0])
            StudentsList.append(s)
            StudentsId.append(line[0])
            

    GradesDict = dict([(key, []) for key in StudentsId])

    with open("grades.txt","r") as l:
        for line in l:
            line=line.split(",")
            #Create a temporary List
            tempList=[]
            tempList.append(line[1].strip()[:-2])
            tempList.append(line[1].strip()[-2])
            tempList.append(line[1].strip()[-1])
            GradesDict[line[0]].append(tuple(tempList))
    return StudentsList,GradesDict
