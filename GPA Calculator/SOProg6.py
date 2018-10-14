#Salman Omar section 3
from math import *
from SOClass import Student
from SOgetData import getData

def main():
    #Set the student list and grades dictionary equal to the getdata function
    studentsList,gradesDict = getData()
    outfile = open("output.txt","w")

    for s in studentsList:
        s.setGrades(gradesDict[s.TechId])
    
        #apply the methods to the student object
        firstLine = ("%s %s (#%s)"%(s.firstName,s.lastName,s.TechId))
        print(firstLine)
        dobdetails=s.dateofBirth.split('/')
        secondLine = ("Age: %d (%d/%d/%d)"%(s.currentAge(),int(dobdetails[0]),int(dobdetails[1]),int(dobdetails[2])))
        print(secondLine)
        
        GPA,cred = s.currentGPA()
        if GPA is None:
            gpa = ("GPA: None (0 crdeits)\n\n")
        else:
            gpa = ("GPA: %.2f (%d credits)\n\n"%(GPA,cred))
        
        print(gpa)

        #Print to the output file
        outfile.write("%-4s\n"% firstLine)
        outfile.write("%-4s\n"% secondLine)
        outfile.write("%-4s\n"% gpa)
        
    outfile.close()
    


main()
    
