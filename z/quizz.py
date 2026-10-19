quetions = ["1. What percentage of Earths surface is covered by water? " 
, "2. Which layer of the Earth is the thickest?" 
, "3. Approximately how long does Earth take to orbit the Sun once?" 
, "4. Which gas makes up most of Earths atmosphere?" 
, "5. What is the largest ocean on Earth?" ]

options = ["A) About 50% B) About 71% C) About 85% D) About 60%" 
, "A) Crust B) Outer core C) Mantle D) Inner core" 
, "A) 24 hours B) 30 days C) 365 days D) 12 months and 10 days" 
, "A) Oxygen B) Carbon dioxide C) Hydrogen D) Nitrogen" 
, "A) Atlantic Ocean B) Indian Ocean C) Pacific Ocean D) Arctic Ocean" ] 

answers = ["B",'C','C','D','C']
print()
choice = []
result = 0

for i in range(5):
    print("__________________________________________________________________")
    print(quetions[i])
    print(options[i])
    print("------------------------------------------------------------------")

    ans = input("ENTER A OPTION A-B-C-D: ").upper()
    choice.append(ans)
    if ans == answers[i]:
        result += 1
        print("Your answer is corrct ")
    else:
        print("Your Ans in Wronge ")

print("------------------------------------------------------------------")
print(answers)
print(choice)
print(f"So You chosse total {result} options right ")


print("------------------------------------------------------------------")

