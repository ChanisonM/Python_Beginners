# Concatenation  " + "
fname = "Chanison"
lname = "Aupathin"

fullname = fname + " " + lname

# print(fullname)

# There Double String 

address = """

160 
M.11 
Soi.12
"""

# print(address)


# Format Sting (F-String)
import datetime

brithday_year  = 1998
current_year = datetime.datetime.today().year
salary = 20000

message = f"Borth : {brithday_year}"
age = f"This Year Old : {current_year - brithday_year}"
data = (f"Salary : {salary:.2f}")

# print(data)



# String (Slice)
# print(text[5:])
# print(text[-6:])
# print(text[:5])
# print(text[3:7])
# print(text[-8:-4])

# Funtion Sting
# startswith() เช็คคำขึ้นต้น
# endswith() เช็คคำลงท้าย
# find() ค้นหาคำ if true retrun [index] false retrun -1
# count() count repetitive word retrun if true retrun number false retrun 0
# replace(olddata , newdata) 
# strip() remove space between string
# format() return [index]  

# fname = input("Input month : ")
# if fname.endswith("คม"):
#     print("31 day ")
# elif fname.startswith("ยน") :
#     print("30 day")
# else :
#     print("Someting")

text = "Name {0} Age {1} year old ".format("Chanison" , 27)
print(text)
