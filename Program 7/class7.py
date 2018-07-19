#Salman Omar, section 03

#Create the superclass Appointment
class Appointment :


#Initializing the Instance Variables
   def __init__(self, month, day, year, time, desc) :


      self.month = month


      self.day = day


      self.year = year

      self.time = time

      self.desc = desc


   #Make getters

   def getMonth(self):
      return self.month

   def getDay(self):
      return self.day

   def getYear(self):
      return self.year

   def getDesc(self):
      return self.desc
   
      

   #Make setters
   def setMonth(self, newmonth ):
      self.month = newmonth

   def setDay(self, newday):
      self.day = newday

   def setYear(self, newyear):
      self.year = newyear

   def setDesc(self, newdesc):
      self.desc = newdesc
      
      
 


   def occursOn(self, month, day, year) :


      return day == self.day and month == self.month and year == self.year





## An appointment that occurs only one time on a specific date.


#


class Onetime(Appointment) :




   def __init__(self, month, day, year, time,desc) :

      #Inherit instance variables from the superclass
      super().__init__(month, day, year, time,desc)


   def getType(self):
      return ("OneTime")






   def __repr__(self) :


      return "One time appointment starting at %s on(%d/%d/%d): %s" % (self.time, self.month, self.day, self.year, self.desc)





## An appointment that occurs daily.


#


class Daily(Appointment) :




 

   def __init__(self, month, day, year, time, desc) :

      #Inherit instance variables from the superclass
      super().__init__(month, day, year, time, desc)




   def getType(self):
      return ("Daily")





   def __repr__(self) :


      return "Daily appointment starting at %s on(%d/%d/%d): %s" % (self.time, self.month, self.day, self.year, self.desc)











   def occursOn(self, month, day, year) :


      if year > self.year :


         return True


      if year == self.year and month > self.month :


         return True


      if year == self.year and month == self.month and day >= self.day :


         return True


      return False






#Subclass Monthly that imports form the Appointment superclass
class Monthly(Appointment) :



   def __init__(self, month, day, year, time, desc) :

      #Inherit instance variables from the superclass
      super().__init__(month, day, year, time, desc)




   def getType(self):
      return ("Monthly")




   def __repr__(self) :


      return "Monthly appointment starting at %s on(%d/%d/%d): %s" % (self.time, self.month, self.day, self.year, self.desc)




   def occursOn(self, month, day, year) :


      if year > self.year and day == self.day:


         return True


      if year == self.year and month >= self.month and day == self.day :


         return True


      return False


