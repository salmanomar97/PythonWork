from SOtriFun import *
from SOgetData import *
outfile = open ("SOoutput5.txt","w")
 #Initializing a mainlist and setting it equal to the getdata function
mainlist = getData()

for i in range (len(mainlist[0])):
    person = mainlist[0][i]
    x1 = float(mainlist[1][i][0][0])
    y1 = float(mainlist[1][i][0][1])
    x2 = float(mainlist[1][i][1][0])
    y2 = float(mainlist[1][i][1][1])
    x3 = float(mainlist[1][i][2][0])
    y3 = float(mainlist[1][i][2][1])
    
    #Making conditional statements to make sure coordinates aren't duplicates or collinear
    if collinear(x1,y1,x2,y2,x3,y3):
        
        print ("Invalid Triangle, duplicate points or collinear\n")
        outfile.write("Invalid Triangle, Duplicate Points or Collinear\n")
        print ("______"*12)

    elif duplicatePts(x1,y1,x2,y2,x3,y3):
        print ("Invalid Triangle, duplicate points or collinear\n")
        outfile.write("Invalid Triangle, duplicate points or collinear\n")
        
        #If the points are not duplicates or collinear, then the program will continue with the other functions

    else:
        
        
        #Putting some of the output into variables to make life easier when printing the output and formating
        lineOneL = (mainlist[0][i])
        lineOneR = (mainlist[1][i])
        print ("%-4s%s"%(lineOneL,lineOneR))
        
        
        side1 = (sideLength(x1,x2,y1,y2))
        side2 = (sideLength(x2,x3,y2,y3))
        side3 = (sideLength(x1,x3,y1,y3))
        lineTwoL = ("Perimeter:%.2f"%perimeter(x1,y1,x2,y2,x3,y3))
        lineTwoR = ("Sidelengths: %.2f,%.2f,%.2f"%(side1,side2,side3))
        print ("%-20s%s"%(lineTwoL,lineTwoR))
        
        
       
    
        #Conditional statements for the Boolean outputs
        if acute(x1,y1,x2,y2,x3,y3):
            angle = ("Acute")
        elif obtuse(x1,y1,x2,y2,x3,y3):
            angle = ("Acute")
        elif right(x1,y1,x2,y2,x3,y3):
            angle = ("Acute")
           

        if scalene(x1,y1,x2,y2,x3,y3):
            triangleType = ("Scalene")
        elif isosceles(x1,y1,x2,y2,x3,y3):
            triangleType = ("Isoceles")
        elif equilateral(x1,y1,x2,y2,x3,y3):
            triangleType = ("Equilateral")

        #Putting more output into variables for formating purposes
        left = (angle)
        right = (triangleType)
        lineThreeL = (left+"&"+right)
        lineThreeR = ("Area: %.2f"%area(x1,y1,x2,y2,x3,y3))

        print("%-20s%s"%(lineThreeL,lineThreeR))
        
        
        #Writing to the output file
        outfile.write("%-4s%s\n"%(lineOneL,lineOneR))
        outfile.write("%-20s%s\n"%(lineTwoL,lineTwoR))
        outfile.write("%-20s%s\n"%(lineThreeL,lineThreeR))
        outfile.write("\n")


        print ("______"*12)





outfile.close()













    

