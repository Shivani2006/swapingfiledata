

def swapFileData():

   
    assignment= input ('enter the file name here ')
    assignment2= input ('enter the 2nd file name here ')
   
    with open(assignment, 'r') as a:
        assignment1_data = a.read()
    with open(assignment2,'r') as b:
        assignment2_data = b.read()

    with open(assignment,'w') as a:
        a.write(assignment2_data)
    with open(assignment2,'w') as b:
        b.write(assignment1_data)
    
    print(assignment)
swapFileData()
