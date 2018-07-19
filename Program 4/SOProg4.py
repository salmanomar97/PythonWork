#Salman Omar, section 03
from SOtriFun import *

#Opening the input and output file
infile = open ("input4.txt","r")
outfile = open ("SO4.txt","w")



#Starting a loop to go over each line in the input file
for line in infile:
    
    #Seperate each value
    line = line.split()
    #Assign each point to a position and converting to a float
    x1 = float(line[0])
    y1 = float(line[1])
    x2 = float(line[2])
    y2 = float(line[3])
    x3 = float(line[4])
    y3 = float(line[5])

    #Checking to make sure that the triangle is a "Triangle" by using collinear and duplciatePts function
    if collinear(x1,y1,x2,y2,x3,y3):
        
        print ("Invalid Triangle, duplicate points or collinear")
        outfile.write("Invalid Triangle, Duplicate Points or Collinear\n")
        print ("______"*12)

    elif duplicatePts(x1,y1,x2,y2,x3,y3):
        print ("Invalid Triangle, duplicate points or collinear")
    #If the points are not duplicates or collinear, then the program will continue with the other functions
    else:
        
        #Putting some of the output into variables to make life easier when printing the output and formating
        lineOneL = ("Vertices: (%.2f,%.2f)(%.2f,%.2f)(%.2f,%.2f)"%(x1,y1,x2,y2,x3,y3))
        lineOneR = ("Shortest Side is: %.2f"%findShortest(x1,y1,x2,y2,x3,y3))
        lineTwoL = ("Perimeter is: %.2f"%perimeter(x1,y1,x2,y2,x3,y3))
        lineTwoR = ("Area: %.2f"%area(x1,y1,x2,y2,x3,y3))
        
        
        print ("%-50s%s"%(lineOneL,lineOneR))
        print ("%-50s%s"%(lineTwoL,lineTwoR))
    
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
        lineThreeL = angle
        lineThreeR = triangleType

        print("%-50s%s"%(lineThreeL,lineThreeR))
        
        #Writing to the output file
        outfile.write("%-50s%s\n"%(lineOneL,lineOneR))
        outfile.write("%-50s%s\n"%(lineTwoL,lineTwoR))
        outfile.write("%-50s%s\n"%(lineThreeL,lineThreeR))



        print ("______"*12)




infile.close()
outfile.close()
