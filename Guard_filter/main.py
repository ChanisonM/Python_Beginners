score = int(input("Enter Your Score (0 - 100) : "))

print("Your Score : " , score)

match score :
    case 100 : 
        print("Your Score is Pass")
    case score if score >= 50 and score < 100 :
        print("Your Score is Pass too!")
    case _ :
        print("your Score is Not Pass")