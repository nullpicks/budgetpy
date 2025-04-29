from datetime import datetime
import os
def get_valid_number(prompt):
    while True: 
        try: #used to catch errors
            value =float(input(prompt)) # a variable named value is being set, value takes the prompt and checks it to see if its a float
            if value < 0: 
                print("Value can not be less than 0")
                continue
            return value #if it is true, it returns it 
        except ValueError: 
            print("Error: Please enter a valid number") # if its not  it throws an error ; 


def get_valid_string(prompt):
    while True:
        try: 
            string=input(prompt).strip() #string variable is equal to input filled with prompt which would be expense and it is stripped of its white space 
            if not string: #checks to see if string is empty
                print("error: String can not be empty ")
                continue
            if string.isnumeric(): #checks to see if the string is numeric
                print("String can not contain any numbers ")
                continue
            if all(c.isalpha() or c.isspace() or c == '-' for c in string): 
                return string
            else:
                print("Only Letters, spaces and hyphens allowed here")
        except EOFError:
            print("error: Input interrupted (EOF)")
            continue
            #checks each character to see if there is space, "-" 
            # isalpha checks to see if a single characters  contains letters 
            # isspace checks to see if the string only contains whitespace 




def write_file(filename):
    i = 1
    total_price = 0
    with open(filename, 'w') as file:
     file.write(f"Created on: {timestamp()}\n" )
     while(i != 0):
         expense = get_valid_string("Enter the name of your expense or type done to exit\n ")
         if expense == "done":
             break
            
         expense_price = get_valid_number("Enter the price of your expense  ")
         print(expense,expense_price)
         total_price = float(expense_price) + total_price
         file.write(f"{expense}: {expense_price}\n")
    file.write(f"The total price is {total_price:.2f}\n")             
     

def append_file(filename):
    i = 1
    total_price = 0; 
    try: 
        with open(filename,'a') as file:
            file.write(f"Appending file on: {timestamp()}\n")
            while( i!= 0):
                expense = get_valid_string("Enter the name of your expense or type done to exit\n")
                if expense == "done": 
                    break 
                expense_price = get_valid_number("Enter the price of your expense\n ")
                print(expense,expense_price)
                total_price = float(expense_price) + total_price
                file.write(f"{expense}: {expense_price}\n")
            file.write(f"{total_price:.2f}\n")
    except FileNotFoundError: 
        print("Error,File does not exist")




def read_file(filename):

    try:
        with open(filename,'r') as file:
            lines = file.readlines()
            for lines in lines:
                print(lines.strip())
    except FileNotFoundError: 
        print("Error, The file does not exist")
        
def timestamp():
    timestring = datetime.now()
    timestamp = timestring.strftime("%c")
    return timestamp

filename =input("Enter a name for this file\n")
while(True):

    menu =input("1.Write new file\n2.Read File\n3.Append a file\n4.Quit\n")

    if(menu == '1'):
        write_file(filename)
    elif(menu =='2'):
        read_file(filename)
    elif(menu=='3'):
        append_file(filename)
    elif(menu=='4'):
        print("Exiting File")
        break
    else:
        print("Enter a valid answer")
