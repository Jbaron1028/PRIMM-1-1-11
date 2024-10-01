"""
PRIMM: 1+1 = 11
Description of program here
Name - Date
"""

def main():
  
    num1: int = int(input("Enter a number: ")) #creating a new variable and asking the user for the input and changing the variable type to int from str
    num2: int = int(input("Enter another number: ")) #creating a new variable and asking the user for the input and changing the variable type to int from str
    total: int = num1+num2 #creating a new variable and adding up the two inputs

    print(f"{num1} + {num2} = {total}") #printing out the total

if __name__ == "__main__":
  main()
