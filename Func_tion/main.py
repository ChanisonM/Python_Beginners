#Function None Parameter
def sayHello () :
    print("Hello!!!")

def showTable () :
    print("-------")
    for i in range(1 , 13) :
        print(f"2 x {i}  = {2 * i}")


# Funtion Parametor & argument
def sayHi(usrename , age):
    print("Hello : " , usrename)
    print("Age : " , age)

def mutiTabel(num) :
    print("-------")
    for i in range(1 , 13) :
        print(f"{num} x {i}  = {num * i}")

def saveEmployee(name , department , salary) :
    print(f"Your Name : {name}")
    print(f"Department : {department}")
    print(f"Salary : {salary}")


# *args
# tuple ข้อมูลลำดับ
def saveEmployees(*args)  : 
    print(f"Your Name : {args[0]}")
    print(f"Department : {args[1]}")
    print(f"Salary : {args[2]}")
    print(f"Address : {args[3]}")

# **kwargs
# dictionary ข้อมูลกำหนดชื่อ 
def saveData(**kwargs):
    print(f"Your Name : {kwargs["name"]}")
    print(f"Department : {kwargs["departmet"]}")
    print(f"Salary : {kwargs["salary"]}")
    print(f"Address : {kwargs["country"]}")
    print("----------")



# return Funtion
def getCapital():
    return "Bangkok"
def getPI():
    return 3.14

data = getCapital()

radius = 5
area = getPI() * radius**2


# parametor + return Funtion
def CheckNumber(number) :
    if number % 2 == 0 :
        return("Even")
    else :
        return("Odd")

def summation(*args) :
    total = 0
    for item in args :
        total += item
    return total
    
result = summation(10 , 20 ,30 , 40)




# Lambda Funtion 
result = lambda base , n : base**n 




balance = 1000 
# balance is global variable

def displayBalance():
    print(f"ยอดเงินคงเหลือ {balance} บาท")

def depisit(value):
    global balance
    money = value
    print(f"ฝากเงินจำนวน {money} บาท")
    if(money <= 0 ):
        print("ไม่สามารถฝากเงินได้")
        return
    balance += money

def withdraw(value):
    global balance
    amount = value 
    print(f"ถอนเงินจำนวน {amount} บาท")
    if amount <= 0 or amount > balance :
        print("ไม่สามารถถอนเงินได้")
        return
    balance -= amount

withdraw(1100)
displayBalance()

