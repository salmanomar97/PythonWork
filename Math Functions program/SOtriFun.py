#Salman Omar, section 03
#This program is the function program that will do all the math for the main program

import math

def duplicatePts(x1,y1,x2,y2,x3,y3):
# Find if there are duplicate points in the triangle
   if (x1,y1)==(x2,y2):
      print("true")
      return True
   elif (x2,y2) == (x3,y3):
      print("Duplicate Points")
      return True
   elif (x3,y3)==(x1,y1):
      print("Duplicate Points")
      return True
   else:
      print
      return False

#This function will make sure that no two points lie on the same line    
def collinear(x1,y1,x2,y2,x3,y3):
    if x1==x2:
        return True
    else:
        
       slope = (y2-y1)/(x2-x1)
       slope2 = (y3-y2)/(x3-x2)
       if slope==slope2:
           return True
       else:
           return False 


# Finds the length of the line between (x1,y1) and (x2, y2)    
def sideLength(x1,x2,y1,y2):
   side1 = (x2-x1)**2
   side2 = (y2-y1)**2
   
   distance = math.sqrt((side1 + side2))
    
   return distance
       
      
#This function finds the shortest side of the triangle
def findShortest(x1,y1,x2,y2,x3,y3):
   side1 = math.sqrt((((x2-x1)**2)+(y2-y1)**2))
       
   side2 = math.sqrt((((x3-x2)**2)+(y3-y2)**2))
       
   side3 = math.sqrt((((x3-x1)**2)+(y3-y1)**2))
   shortestSide = min(side1, side2, side3)
   
   return shortestSide

    # Finds the lognest side length
    

#This function finds the longest side of the triangle
def findLongest (x1,y1,x2,y2,x3,y3):
   side1 = math.sqrt((((x2-x1)**2)+(y2-y1)**2))
       
   side2 = math.sqrt((((x3-x2)**2)+(y3-y2)**2))
       
   side3 = math.sqrt((((x3-x1)**2)+(y3-y1)**2))
   longestSide = max(side1, side2, side3)
   
   return longestSide
#This function calculates the perimeter of the triangle
def perimeter(x1,y1,x2,y2,x3,y3):
   side1 = math.sqrt((((x2-x1)**2)+(y2-y1)**2))
       
   side2 = math.sqrt((((x3-x2)**2)+(y3-y2)**2))
       
   side3 = math.sqrt((((x3-x1)**2)+(y3-y1)**2))
   semiPerimeter = (side1 + side2 + side3)
   return semiPerimeter
    # Calculates the perimeter when you add all the side lengths together.
    # example with a square would be S1 + S2 + S3 +S4 = perimeterOfSquare
#This function calculates the area of the triangle    
def area(x1,y1,x2,y2,x3,y3):
   
   side1 = math.sqrt((((x2-x1)**2)+(y2-y1)**2))
       
   side2 = math.sqrt((((x3-x2)**2)+(y3-y2)**2))
       
   side3 = math.sqrt((((x3-x1)**2)+(y3-y1)**2))
   sPerimeter = (side1 + side2 + side3)/2
   area = (sPerimeter*(sPerimeter-side1)*(sPerimeter-side2)*(sPerimeter-side3))**.5
   return area
    # area is found by the 3 sidelengths, taking the height from the longest side (base) * base divided by 2
    # A = H(b)*b/2
    
def right(x1,y1,x2,y2,x3,y3):
   side1 = math.sqrt((((x2-x1)**2)+(y2-y1)**2))
       
   side2 = math.sqrt((((x3-x2)**2)+(y3-y2)**2))
       
   side3 = math.sqrt((((x3-x1)**2)+(y3-y1)**2))
   if (side3**2) == ((side1**2) + (side2**2)):
      return True
   elif (side2**2) == ((side1**2) + (side3**2)):
      return True
   elif (side1**2) == ((side3**2) + (side2**2)):
      return True
   else:
      return False
   #return False # or True
    # checks all the angles of the triangle, if angle = 90 degrees, returns truewse
    # if side1 is longest and side2 is shortest then S2^2 + S3^2 = S1^2
    
def acute(x1,y1,x2,y2,x3,y3):
   side1 = math.sqrt((((x2-x1)**2)+(y2-y1)**2))
       
   side2 = math.sqrt((((x3-x2)**2)+(y3-y2)**2))
       
   side3 = math.sqrt((((x3-x1)**2)+(y3-y1)**2))
   if (side3**2) < ((side1**2) + (side2**2)):
      return True
   elif (side2**2) < ((side1**2) + (side3**2)):
      return True
   elif (side1**2) < ((side3**2) + (side2**2)):
      return True
   else:
      return False
      #return False # or True
    # checks all the angles of the triangle, if angle < 90 degrees, returns true
    #Therefore, if S2^2 + S3^2 > S1^2, then lengths S2, S3, and S1 make up an acute triangle.  It is important to note that the length ‘‘S1′′ is always the longest.
    
def obtuse(x1,y1,x2,y2,x3,y3):
   side1 = math.sqrt((((x2-x1)**2)+(y2-y1)**2))
       
   side2 = math.sqrt((((x3-x2)**2)+(y3-y2)**2))
       
   side3 = math.sqrt((((x3-x1)**2)+(y3-y1)**2))
   
   if (side3**2) > ((side1**2) + (side2**2)):
      return True
   elif (side2**2) > ((side1**2) + (side3**2)):
      return True
   elif (side1**2) > ((side3**2) + (side2**2)):
      return True
   else:
      return False
   #return False # or True
    # checks all the angles of the triangle, if angle > 90 degrees, returns true
    #Conversely, if a2 + b2 < c2, then lengths a, b, and c make up the sides of an obtuse triangle.
    
def scalene(x1,y1,x2,y2,x3,y3):
   side1 = math.sqrt((((x2-x1)**2)+(y2-y1)**2))
       
   side2 = math.sqrt((((x3-x2)**2)+(y3-y2)**2))
       
   side3 = math.sqrt((((x3-x1)**2)+(y3-y1)**2))
   #return False # or True
   # This will check the triangle sides, if all sides are unequal in length, returns true
   if side1 != side2 and side1 != side3 and side2 != side3:
      return True
   else:
      return False
    
def isosceles(x1,y1,x2,y2,x3,y3):
    # This will check the triangle sides, if only two sides are equal in length, returns true
   side1 = math.sqrt((((x2-x1)**2)+(y2-y1)**2))
       
   side2 = math.sqrt((((x3-x2)**2)+(y3-y2)**2))
       
   side3 = math.sqrt((((x3-x1)**2)+(y3-y1)**2)) 
   if side1 == side3 and side1 != side2 and side3 != side2:
      return True
   elif side3 == side2 and side3 != side1 and side3 != side1:
      return True
   elif side1 == side2 and side1 != side3 and side2 != side3:
        return True
   else:
       return False
def equilateral(x1,y1,x2,y2,x3,y3):
   side1 = math.sqrt((((x2-x1)**2)+(y2-y1)**2))
       
   side2 = math.sqrt((((x3-x2)**2)+(y3-y2)**2))
       
   side3 = math.sqrt((((x3-x1)**2)+(y3-y1)**2))
   #return False # or True
   # This will check the triangle sides, if all sides are unequal in length, returns true
   if side1 == side2 and side1 == side3 and side2 == side3:
        return True
   else:
      return False
