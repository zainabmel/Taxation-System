# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 19:17:21 2021

@author: zainab
"""

# Name: Zainab Melaibari
# Email: zainabmel@gmail.com
# Course: CCCS 111
# Title: (Taxation System) Project-Phase2
# Date: 26-11-2019


#This program will calculate the final TaxPayable and write user information into file

 
def displayMenu():
    
    #Display the menu
    print("||******************Menu*********************||\n",
          "Please select the country:\n  A. Amereica\n  B. Australia\n  C. Exit\n",
          "||*******************************************||",sep="")
    
def isValid_ITIN(ITIN):
    
    #Test the ITIN number to make sure it follows the requirements
    #ITIN = 900-xx-0000
    #Index= 012-34-5678
    
    if len(ITIN)==9:
        
        num=ITIN[3:5]  #num = xx with index 3,(5-1) --> 3,4
        
        num=int(num)  #convert num to integer
        
        if (ITIN[0]!="9") or (not(num in range(70,88+1) or num in range(90,92+1) or num in range(94,99+1))):
            Boolean_Valid_ITIN=False
        else:
            Boolean_Valid_ITIN=True
            
    else:
         Boolean_Valid_ITIN=False
            
    return Boolean_Valid_ITIN 
    
def isValid_TFN(TFN): 
    
    #Test the TFN number to make sure it follows the requirement
    #TFN = 000-000-000
    
    if len(TFN)!=9 :
        Boolean_Valid_TFN=False
    else:
        Boolean_Valid_TFN=True
  
    return Boolean_Valid_TFN 
        
def US_TaxPaid(A_Salary):
    
    #Define the tax for every salary value, based on the progressive tax rate system for America
    
    if 8700>=A_Salary>=0:
        Tax=0.10
    elif 35350>=A_Salary>=8701:
        Tax=0.15
    elif 85650>=A_Salary>=35351:
        Tax=0.25
    elif 178650>=A_Salary>=85651:   
        Tax=0.28
    elif 388350>=A_Salary>=178651: 
        Tax=0.33
    elif A_Salary>=388351: 
        Tax=0.35
    
    #return the tax percentage in US to the main function     
    return Tax    

def AU_TaxPaid(A_Salary):
    
    #Define the tax for every salary value, based on the progressive tax rate system for Australia
    
    if 6000>=A_Salary>=0:
        Tax=0
    elif 37000>=A_Salary>=6001:
        Tax=0.15
    elif 80000>=A_Salary>=37001:
        Tax=0.30
    elif 180000>=A_Salary>=80001:   
        Tax=0.37
    elif A_Salary>=180001: 
        Tax=0.45
    
    #return the tax percentage in AU to the main function      
    return Tax
    
def CalculateTax(A_Salary,Tax):
    
    #Calculate the tax Payable amount by multiply the salary by the tax percentage 
    TAX_Paid=A_Salary*Tax
    
    #return the result "tax Payable amount" to the main function
    return TAX_Paid
           
def WriteToFile(FullName,ID,Salary,TaxPayable):
    
    #Convert the type of salary and tax payable data into "string" to make writing data into the text file possible
    
    Salary=str(Salary)
    
    TaxPayable=str(format(TaxPayable,",.1f"))
    
    Recordfile=open("TaxPayableReport.txt","a") #Open the text file in "append mode"
    Recordfile.write(FullName+"\n"+ID+"\n"+Salary+"\n"+TaxPayable+"\n") #Write user's data in the file
    Recordfile.close() #Close the file
    
    #return following sentence to the main function to be printed there
    return "The citizen's record has been written to the output file."
    

def main():
    
    #Assume that Country variable equal string "A" to enter into the loop for the first time
    Country="A"
    
    while Country=="A" or Country=="B" or Country=="a" or Country=="b":#while user choose America or Australia  
    
        #print the beginning of program interface
        print("||*******************************************||",
              "\n\t Welcome to Taxation System\n",
              "||*******************************************||\n",sep='')
        
        #Call function to display the menu
        displayMenu()
        
        #Get user's choice about his\her country or C to exit
        Country=input("Enter your choice(A or B or C): ")
        
        #Exclude options except America or Australia or exit (A,a,B,b,C,c)
        while Country!="A" and Country!="B" and Country!="C" and Country!="a" and Country!="b" and Country!="c":
            
            print("---------------------------\nWrong entry!",
                  "\nYou should enter A for America or B for Australia or C to exit!",
                  "\nTry Again!\n---------------------------",sep='')
            
            displayMenu()#Call function to display the menu again
            
            Country=input("Enter your choice(A or B or C): ")#Get user's choice again about his\her country or C to exit
        
        #If the user choose America
        if Country=="A" or Country=="a":
            
            print("---------------------------")#To organize the interface
            
            #Get user's information
            
            ITIN=input("Enter the Individual Taxpayer Identification Number (ITIN): ")#Get the ITIN number from user
            
            Boolean_Valid_ITIN=isValid_ITIN(ITIN) #Call function to test the ITIN
            
            #If the Boolean value returned from the isValid_ITIN funtion is "not equal True">(ITIN not follows the requirements)
            while Boolean_Valid_ITIN !=True:
                    print("Wrong entry, ITIN does not follow the rules!\nTry again!\n",sep='')
                    ITIN=input("Enter the Individual Taxpayer Identification Number (ITIN): ")#Get the ITIN number again from user
                    Boolean_Valid_ITIN=isValid_ITIN(ITIN) #Call function again to test the ITIN
            
            Name=input("Enter your Full name: ")
            
            A_Salary=float(input("Enter your annual salary: "))
            
            #Exclude negative salary
            while A_Salary<0:
               print("---------------------------","\nIncorrect salary value!\nTry Again\n","---------------------------",sep='')
               A_Salary=float(input("Enter your annual salary: "))
            
            #Call function to determine the Tax
            USTax=US_TaxPaid(A_Salary)
            
            #Call function to calculate the Tax payable amount
            TAX_Paid=CalculateTax(A_Salary,USTax)
            
            #view user's information
            print("---------------------------",
                  "\nThe Entered data: \nFull name:  ",Name,"\nITIN:  ",ITIN,"\nThe annual Salary: ",
                  format(A_Salary,".2f"),"$\n","---------------------------",sep="")
            
            #print the resulte of Calculation "The Tax Paid"
            print("The citizen's Tax-payable ammount is: ",format(TAX_Paid,",.1f"),"$",sep="")  
            
            #Call function to write data into file and print the output message
            print((WriteToFile(FullName=Name,ID=ITIN,Salary=A_Salary,TaxPayable=TAX_Paid)),"\n","---------------------------",sep="")
            
        #If the user choose Australia
        elif Country=="B" or Country=="b":
            
            print("---------------------------")#To organize the interface
            
            #Get user's information
            
            TFN=input("Enter the Tax File Number (TFN): ")#Get the TFN number from user
            
            Boolean_Valid_TFN=isValid_TFN(TFN) #Call function to test the TFN
            
            #If the Boolean value returned from the isValid_TFN funtion is "not equal True">(TFN not follows the requirement)
            while Boolean_Valid_TFN !=True:
                print("Wrong entry, TFN should be 9 digits!\nTry again!\n",sep='')
                TFN=input("Enter the Tax File Number (TFN): ") #Get the TFN number again from user
                Boolean_Valid_TFN=isValid_TFN(TFN)#Call function again to test the TFN
            
            Name=input("Enter your Full name: ")
            
            A_Salary=float(input("Enter your annual salary: "))
            
            #Exclude negative salary
            while A_Salary<0:
               print("---------------------------","\nIncorrect salary value!\nTry Again\n","---------------------------",sep='')
               A_Salary=float(input("Enter your annual salary: "))
            
            #Call function to determine the Tax
            AUTax=AU_TaxPaid(A_Salary)
            
            #Call function to calculate the Tax payable amount
            TAX_Paid=CalculateTax(A_Salary,AUTax)
            
            #view user's information
            print("---------------------------",
                  "\nThe Entered data: \nFull name:  ",Name,"\nTFN:  ",TFN,
                  "\nThe annual Salary: ",format(A_Salary,".2f"),"$\n","---------------------------",sep="")
            
            #print the resulte of Calculation "The Tax Paid"
            print("The citizen's Tax-payable ammount is: ",format(TAX_Paid,",.1f"),"$",sep="")  
            
            #Call function to write data into file and print the output message
            print((WriteToFile(FullName=Name,ID=TFN,Salary=A_Salary,TaxPayable=TAX_Paid)),"\n","---------------------------",sep="")
            
    #If the user choose to exit
    if Country=="C" or Country=="c":
        #Display message then end the program
        print("---------------------------","\nYou have choosen to End the program!\n",
              "---------------------------","\nThanks for Using Taxation System",sep="")
                   
main() #Call the main function to start the program   

input()       