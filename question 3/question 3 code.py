class employee_details:
    def __init__(self,Name,Pay_rate,Hours_worked,Salary): #define all the atributes of the worker
        self.Name=Name
        self.Pay_rate=Pay_rate
        self.Hours_worked = Hours_worked
        self.Salary = Salary


    def __str__(self): #format how the data is presented when called for  
        return(f"""Name: {self.Name}
Pay rate: {self.Pay_rate}
Hours worked: {self.Hours_worked}
Salary: {self.Salary}""")

while True:#get the name as long as its not an empty space 
    name = input("What is the name of the employee? ").strip()
    if name.isnumeric():
        print("name must be a string")
    elif name:
        break
    else:
        print("Name cannot be empty.")
while True: # dont take the input if it is anything other than a float and makes sures its not a negative 
    try:
        Pay_rate=float(input("what is the employees pay rate?"))
        if Pay_rate < 0:
            print("Pay rate cannot be negative!")
        else:
            break
    except ValueError:  
        print("input has to be a number!")
while True: # dont take the input if it is anything other than a float and makes sures its not a negative 
    try:
        Hours_worked=float(input("how many hours do they work?"))
        if Hours_worked < 0:
            print("Pay rate cannot be negative!") 
        else:
            break
    except ValueError:
        print("input has to be a number!")
while True: # dont take the input if it is anything other than a float and makes sures its not a negative 
    try:
        Salary=float(input("what is the employees salary?"))
        if Salary < 0:
            print("Pay rate cannot be negative!")
        else:
            break
    except ValueError:
        print("input has to be a number!")

user=employee_details(name,Pay_rate,Hours_worked,Salary) #assign the attributes to the user using the class 
print(user)#display the details in the requested format 
