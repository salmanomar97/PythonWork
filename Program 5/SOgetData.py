def getData():
    infile = open ("input5.txt","r")

    name = []
    vertices = []
    myList = []
    line = infile.readline()
    for line in infile:
        #Seperate each value
        line = line.split()
        #Assign each point to a position
        
        
        x0 = str(line[0])
        x1 = float(line[1])
        y1 = float(line[2])
        x2 = float(line[3])
        y2 = float(line[4])
        x3 = float(line[5])
        y3 = float(line[6])

    
        
        
        name.append(x0)
        vertices.append([[x1,y1],[x2,y2],[x3,y3]])


    myList.append(name)
    myList.append(vertices)

    return myList

    infile.close()    
  




