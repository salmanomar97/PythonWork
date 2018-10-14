#Salman Omar, Section 3
import math
    
#Ask user for radius input
circleRadius = float(input("Enter the radius of the circle "))

#Calculate the circumference of the circle
circleCircumference = (circleRadius * (2 * math.pi))

#Calculate the area of the circle
circleArea = (circleRadius**2 * (math.pi))

#Calculate the volume of the sphere
sphereVolume = ((4/3) * (math.pi) * (circleRadius**3))

#Calculate the surface area of the sphere
sphereSurfaceArea = (4 * (circleRadius**2) * (math.pi))

#Print the following outputs
print ("The input radius is ", circleRadius)
print ("")
print ("Circle Circumference: %8.2f  " %circleCircumference )               
print ("Circle Area: %17.2f " %circleArea )                     
print ("Sphere Volume: %15.2f " % sphereVolume )                     
print ("Sphere Surface Area: %9.2f " % sphereSurfaceArea )

#End of Program
