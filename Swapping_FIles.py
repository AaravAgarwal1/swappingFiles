def swapFileData():
    file1=input("Enter the file 1: ")
    file2= input("Enter the file to be swapped: ")

    #Open file1 and read it’s data and save it in a variable called data_a.
    with open(file1,"r") as a:
        data_a=a.read()
        a.close()

        

    
    #Open file2 and read it’s data and save it in a variable called data_b.
    with open(file2,"r") as b:
        data_b=b.read()
        b.close()

        with open(file1,"w") as a:
            a.write(data_b)

        with open(file2,"w") as b:
            b.write(data_a)
           
     

swapFileData()



