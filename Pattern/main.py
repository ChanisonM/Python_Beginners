service = int(input("กรุณากรอกหมายเลข : "))
match service :
    case 1 :
        print("ฝากเงิน")
    case 2 : 
        print("ถอนเงิน")
    case 3 :
        print("สอบถามยอดคงเหลือ")
    case service :
        print(f"หมายเลขบริการหมายเลข {service} ในระบบ กรุณาทำรายการใหม่อีกครั้ง")