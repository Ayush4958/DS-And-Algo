import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Entering Demo Data
cl= ['XI-A', 'XI-B', 'XI-C', 'XII-A', 'XII-B', 'XII-C'] #
# Data of class names
rn= [101, 102, 103, 4, 5, 6] # Data of Class Room number
ct= ['Sweety ujjwal mam', 'Sakshi meena mam', 'Poojasainimam','Shailygupta mam', 'Sudha pandey mam', 'Vivekkumar sir'] # Data of Class Teacher
ql= ['PGT Physics', 'PGT Chemistry', 'PGT Mathematics', 'PGTChemistry','PGT Physics', 'PGT Commerce'] # Data of Classteacher Subjects
ts= [55, 49, 50, 33, 38, 31] # Data of total students
gm= ['Khushi', 'Mansi', 'Anamika', 'Muskan','Khushi','Anamika'] # Data of girls monitors
bm= ['Shivam', 'Abhinav', 'Krishna', 'Hardik','Yash','Luv'] # Data of boys monitors
cd= {"Room No.": rn,"Class_Teacher": ct,"Subject":ql,"Total_Students": ts,"Girls_Monitor": gm,"Boys_Monitor":bm}
# creating dictionary from all above data
df=pd.DataFrame(cd,index=cl)
print("Enter 1 for Entering Data \nEnter 2 for DisplayingData of class of your choice \nEnter 3 for deleting theclass \nEnter 4 for changing the data \nEnter 5 for see thegraphical representation of classes on basis of theirStrength")
# Taking number from user to further proceed the function
opt=int(input('Enter a Number :- '))
#Entering the New Class Data
if opt == 1:
    new_cl=input("Enter Class (in upper roman count) :- ")
    new_rn=int(input("Enter Room No. :- "))
    new_ct=input("Enter Class Teacher's name :- ")
    new_ql=input("Enter the Qualifcation :- ")
    new_ts=int(input("Enter the Total No. of Student:- "))
    new_gm=input("Enter Girl's Monitor name :- ")
    new_bm=input("Enter Boy's Monitor name :- ")
    cl.append(new_cl)
    rn.append(new_rn)
    ct.append(new_ct)
    ql.append(new_ql)
    ts.append(new_ts)
    gm.append(new_gm)
    bm.append(new_bm)
    df=pd.DataFrame(cd)
    print(df)
# Showing each Class Base on user choice
elif opt == 2:
    print(df.index)
    row_desire=input("Enter the class of your choice :- ")
    if row_desire in df.index:
        print(df.loc[[row_desire],:].to_string())
    else:
        print("Invalid class is entered. Please Try again.....")
# Deleting the row through Class recieved by User
elif opt == 3:
    print(df.index)
    row_deletion=input("Enter the Class to Delete :- ")
    if row_deletion in df.index:
        df=df.drop(row_deletion)
        print("\nRow deleted successfully!")
        print("\nUpdatedDataFrame:")
        print(df)
    else:
        print("Invalid class is entered. Please Try again.....")
# Changing the data of particular class
elif opt == 4:
    print(df.index)
    print(df.columns)
# taking class from user to update
    row_updation=input("Enter the class you want to update the data :- ")
# checking if class exist
    if row_updation in df.index:
# taking field to update from user
        col_updation = input("Enter the field you want to update :-")
# checking if field exists or not
        if col_updation in df.columns:
            updated_col=input("Enter the updated value :- ")
# updating the field
            df.loc[[row_updation],[col_updation]]=updated_col
            print("Data has been updated !!!!!")
            print(df)
        else:
            print("Entered field doesn't exist!!! Try again")
    else:
        print("Entered class is not valid!!!! ")
# Making the line graph of all classes on basis of their class strength
elif opt == 5:
    plt.xlabel('Classes')
    plt.ylabel('Class Strength')
    plt.title('Comparison of perforamnce of each classes')
    plt.plot(df.index,df['Total_Students'])
    plt.show()