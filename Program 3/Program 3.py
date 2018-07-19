# Salman Omar, Section 3

#Open input file
infile = open ("CityPopulation.txt", "r")
#Open output file
outfile = open("SOProg3.txt", "w")

#Reading from the file using readline method
line = infile.readline()
#Initializing County totals and Statetotal before we get into the loop
countyTotal = 0
stateTotal = 0
#Initialing a list for county names
county = []
#Initializing a list for 2014 population
census = []
#Setting up the header for the output to look organized
print ("County :","Population")
print("_____"*4)

for line in infile:
    #Splitting the comma from each line
    line = line.split(',')  
    nameOfCounty = line[0]
    pop2014 = line[3]

    if nameOfCounty not in county:
        #Add the county to the county list and the 2014 population to the census list
        county.append(nameOfCounty) 
        census.append((int(pop2014)))

    else:
        c = county.index(nameOfCounty)
        census[c] = census[c]+int(pop2014)

for c in range(len(county)):
    print (county[c] + ":",census[c])
    #Population Total for the State
    stateTotal += ((int(census[c])))
    
    #Write to the output file
    outfile.write(county[c]+":"+str(census[c])+"\n")
    
    

#Add up the Total and print it
print("_____"*4)
print ("\nTotal Population:", stateTotal)

#Close the input and output
infile.close()
outfile.close()
                  

