#Salman Omar, section 03
#Import All the neccasary files we need

from getData7 import getData
from class7 import *
from datetime import *




def main():
    #Call the getData Function
    aptDetails = getData()
    #Ask the user to input a month. If 0 is entered, it will exist
    #x = int(input("Enter the month:(0 to quit) "))
    #print(x)
    #Make an infinite loop that will run as long as 0 isn't entered
    #while x != ("0"):
        

    #Setup the first round of input from the user. Ask for a number
    print ("Get appointments for:\n1. Today\n2. Tomorrow\n3. Seven days(including today)\n4. A specific date\nEnter 1,2,3,4: Enter 0 to quit ")
    v = input()
    #Initialize a loop to force the user to input a valid number
    while v != ("0"):
        #If the user asks for today's appointments
        if v == ("1"):
            date = datetime.today()
            month= date.month
            day = date.day
            year = date.year

            print("On (%d/%d/%d) you have: "%(month,day,year))
            for i in aptDetails:
                #Conditional statements to see if the appointment occurs today
                if i.occursOn(month,day,year):
                    print(i)
            print("__"*37)


        elif v == ("2"):
            date =datetime.today() + timedelta(days=1)
            month = date.month
            day = date.day
            year = date.year

            print("Tomorrow (%d/%d/%d) you have: "%(month,day,year))
            for i in aptDetails:
                #Conditional statements to see if the appointment occurs tomorrow
                if i.occursOn(month,day,year):
                    print(i)
            print("__"*37)


        #The following statements are if the user wants to know the events for the next seven days including today.
        elif v == ("3"):
            dayOne = datetime.today()
            month = dayOne.month
            day = dayOne.day
            year = dayOne.year
            print("Today (%d/%d/%d) you have: "%(month,day,year))
            for i in aptDetails:
                if i.occursOn(month,day,year):
                    print(i)
            print("__"*37)

            dayTwo = datetime.today()+ timedelta(days=1)
            month = dayTwo.month
            day = dayTwo.day
            year = dayTwo.year
            print("Tomorrow (%d/%d/%d) you have: "%(month,day,year))
            for i in aptDetails:
                if i.occursOn(month,day,year):
                    print(i)
            print("__"*37)

            dayThree = datetime.today()+ timedelta(days=2)
            month = dayThree.month
            day = dayThree.day
            year = dayThree.year
            print("In two days (%d/%d/%d) you have: "%(month,day,year))
            for i in aptDetails:
                if i.occursOn(month,day,year):
                    print(i)
            print("__"*37)

            dayFour = datetime.today()+ timedelta(days=3)
            month = dayFour.month
            day = dayFour.day
            year = dayFour.year
            print("In three days (%d/%d/%d) you have: "%(month,day,year))
            for i in aptDetails:
                if i.occursOn(month,day,year):
                    print(i)
            print("__"*37)

            dayFive = datetime.today()+ timedelta(days=4)
            month = dayFive.month
            day = dayFive.day
            year = dayFive.year
            print("In four days (%d/%d/%d) you have: "%(month,day,year))
            for i in aptDetails:
                if i.occursOn(month,day,year):
                    print(i)
            print("__"*37)

            daySix = datetime.today()+ timedelta(days=5)
            month = daySix.month
            day = daySix.day
            year = daySix.year
            print("In five days (%d/%d/%d) you have: "%(month,day,year))
            for i in aptDetails:
                if i.occursOn(month,day,year):
                    print(i)
            print("__"*37)

            daySeven = datetime.today()+ timedelta(days=6)
            month = daySeven.month
            day = daySeven.day
            year = daySeven.year
            print("In six days (%d/%d/%d) you have: "%(month,day,year))
            for i in aptDetails:
                if i.occursOn(month,day,year):
                    print(i)
            print("__"*37)

        #Option if the user asks to input a specific date
        elif v == ("4"):

            #First, we need to make sure that the user enters a valid day.
            #use try and except exception handling
            try:
                month = int(input("Enter a valid month: "))
                day = int(input("Enter a valid day: "))
                year = int(input("Enter a valid year: "))

                t = datetime(year, month,day)
                print("(%d,%d,%d): " % (month,day,year))
                t = (month, day, year)
                print("On this day (%d/%d/%d) you have: "%(month,day,year))
                for i in aptDetails:
                    if i.occursOn(month,day,year):
                        print(i)
                print("__"*37)

            except ValueError: #This handles a situaiton if the user enters an invalid date
                #Make a little print statement telling them to try again
                print("Invalid Input. Please try again\n")


            

            

                
     
        #Make sure that the end of the loop can ask the user for input again, otherwise, enter 0 to quit.
        print ("Get appointments for:\n1. Today\n2. Tomorrow\n3. Seven days(including today)\n4. A specific date\nEnter 1,2,3,4: Enter 0 to quit ")
        v = input()
    

#call the main function
main()
