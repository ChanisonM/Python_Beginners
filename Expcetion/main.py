# Expction


try :
    number1 = int(input("Enter Number 1 : "))
    number2 = int(input("Enter Number 2 : "))
    if number1 < 0 or number2 < 0:
         raise Exception("ข้อมูลตัวเลขต้องเป็นค่าบวกเท่านั้น")
        
    result = number1 / number2
    print(result)
except ValueError:
    print("ข้อมูลไม่ถูกต้อง กรุณาป้อนเลขข้อมูลเฉพาะตัวเลขเท่านั้น")
except ZeroDivisionError :
    print("หารด้วย 0 ไม่ได้ เนื่องจากไม่ได้ถูกนิยามทางคณิตศาสตร์")

finally:
    print("End Program")