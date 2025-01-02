Battery = "Low Charge "
LED = "Dim/Low LED"
Battery_Range = ["A:10-35%, B:36-65%, C:66-95%"]
A = "Charge For Just About 35 Minutes! "
B = "Charge For Approximately 25 Minutes! "
C = "Charge No More Than 15 Minutes! "
Color = ["Red", "Orange", "Yellow", "Green", "Blue"]
R = "Restart"
E = "Exit"
# Variables
while True:
    print(Battery + LED)
    name = input(f"May I Know Who This Is? ")
    print(f"Hello {name}, Would You Like To Recharge LED Battery? ")
    user_input = input("Please Answer By Typing: 'Yes' OR 'No' ")
    if user_input == "Yes":
        print(f"What Is The Current Battery Percentage Range In? A: 10-35% ", "B: 36-65% ", "C: 66-90%  ")
        user_input = input("Choice: ")
        if user_input == "A":
         print(A)
        elif user_input == "B":
         print(B)
        elif user_input == "C":
         print(C)
         print(f"Have A Nice Day {name}!")
        else:
            print("Invalid Input!")
            print(f"Try Typing Exactly As Displayed {name}!")  #Pick if you want to know the minutes required for each percentage range your LED needs and will output how much to charge it for; else move to next question.
    elif user_input == "No":
        user_input = input("Would You Like To Change Color Instead? Please Answer By Typing: 'Yes' OR 'No' ")
        if user_input == "Yes":
            print(f"Choose Which Color Below: ")
            for color in Color:
                print(color)
            user_input = input("Choice: ")
            if user_input in Color:
                print(f"LED Switched Into {user_input}!")
                print(f"Have A Nice Day {name}!")
            else:  
                print("Invalid Input!") 
                print(f"Try typing Exactly As Displayed {name}!")  #Pick if you want to change color of LED; else move to next question.
        else:
            user_input = input("Would You Like To Alternately Change Brightness For LED? Please Answer By Typing: 'Yes' OR 'No' ")
            if user_input == "Yes":
                print(f"Pick Between '10 ~ 100' ")
                user_input = int(input(" "))
                if 10 <= user_input <= 100:
                    print(f"Brightness Adjusted to {user_input}%: ")    
                    print(f"Have A Nice Day {name}!")
                else:
                    print("Invalid Brightness Input! Choose Between 10 Which Is Lowest Dim or 100 Which is Max Brightness!")
                    print(f"Try Typing Exactly As Displayed {name}!")
            elif user_input == "No":
                print(f"If You'd Like To Exit, Type 'E', Otherwise Type 'R' To Restart. ")
                user_input = input("")
                if user_input.upper() == "E":
                    print(f"Take Care {name}!")
                    break
                elif user_input.upper() == "R":
                    continue
                else:
                    print("Invalid Input!, Restarting...")
                    print(f"Try Typing Exactly As Displayed {name}!") #Will ask if you want to dim or increase brightness depending on percentage you chose from minimum of 10 to maximum of 100, if not, it will ask you to restart or exit.