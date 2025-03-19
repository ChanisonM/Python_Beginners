# OR Pattern

data = input("ป้อนคำนำหน้าชื่อของคุณ : ")
match data :
    case "เด็กชาย" | "นาย"  :
        print("เพศชาย")
    case "เด็กหญิง" | "นางสาว"| "นาง" :
        print("เพศหญิง")
    case _ :
        print("ไม่พบข้อมูล")