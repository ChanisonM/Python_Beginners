# Mapping Pattern
customers = [
    {"name" : "Chanison" , "type" : "general"},
    {"name" : "Mon" , "type" : "member"},
    {"name" : "Mai" , "type" : "general"},
]

id = int(input("Please input your ID : "))

print(f"Welcom Your Customer ID : {id} : {customers[id]["name"]}")

match customers[id] :
    case {"type" : "member"} :
        print("Your are Member discount 50 %")
    case _ :
        print("Your are Not Member")