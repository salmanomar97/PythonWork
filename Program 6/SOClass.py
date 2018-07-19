#Salman Omar section 3
from datetime import date

class Student():
    def __init__(self, firstname,lastname,dob,id):
        self.firstName = firstname
        self.lastName = lastname
        self.dateofBirth = dob
        self.TechId = id

    def setGrades(self,Grades):
        self.gradesList = Grades

    def Report(self):
        print (self.firstName,self.lastName,self.dateofBirth,self.TechId,self.gradesList)

    def currentAge(self):
        today = date.today()
        dobdetails = self.dateofBirth.split('/')
        return today.year - int(dobdetails[-1]) - ((today.month, today.day) < (int(dobdetails[0]), int(dobdetails[1])))

    def currentGPA(self):
        totalScore = 0
        numberOfCredits = 0
        for i in self.gradesList:
            score={'A':4,'B':3,'C':2,'D':1,'F':0}
            totalScore =totalScore+score[i[1]]*int(i[2])
            numberOfCredits = numberOfCredits+int(i[2])

        #Prepare for errors
        try:
            GPA = totalScore / numberOfCredits
        except ZeroDivisionError:
            GPA = None
    
        return GPA,numberOfCredits
