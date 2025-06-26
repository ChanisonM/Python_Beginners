colors = {
    "red" : "สีแดง" ,
    "blue" : "น้ำเงิน",
    "yellow" : "เหลือง"

}


# print(colors.keys()) get key
# print(colors.values()) get value
# print(colors.get("red")) # Get data
# colors.pop(key) renmove key red
# colors.updata(key : value)

colors["black"] = "ดำ" #add key : value
colors["blue"] = "คราม" #update key : value
colors.update({"purple" : "ม่วง"}) # add key : value
colors.update({"red" : "แดงเข้ม"})


mainColor = colors.copy() # Copy dic
print(mainColor)
