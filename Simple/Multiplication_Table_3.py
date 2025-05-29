start = int(input("Start Multiplication"))
end = int(input("End Multiplication"))
                    # 2 - 11 +1
for number in range(start , end + 1):
    print("-" * 20)
    print("Multiplication : " , number)
                    # 1 - 12
    for i in range(1 , 13) :
        print(number , "x" , i , " = " , number * i)
    