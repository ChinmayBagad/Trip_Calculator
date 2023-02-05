name_list = []

while True:
    name = input("Enter the names (or 'q' to quit):-")
    if name == "q":
        break
    name_list.append(name)
    
x = len(name_list)
money_spend = []

print(name_list)

for i in range (x):
    while True:
        try:
            sel = int(input("Enter the Number of the person from the List:- "))
            if sel >= 0 and sel < x:
                name = name_list[sel]
                spend = []
                break
            else:
                print("ERROR CODE ( 0 ):- Enter a Valide Number from the list.")
        except (ValueError):
            print("ERROR CODE ( 0 ):- Enter a Valide Number from the list.")
    
    while True:
        exp = input("Enter the Amount spend by "+ name + " (or 'q' to exit):- " )
        if exp == 'q':
            break
        try:
            exp = float(exp)
            spend.append(exp)
            total = sum(spend)
            break
        except (ValueError):
            print("ERROR CODE ( 1 ) :- Enter a Valide Number.")
    
    money_spend.append(total)

ultra = sum(money_spend)

# Distribution Part
per_person = ultra / x
print("Total Money Spend = ", ultra)
print("Per Person Cost = ", per_person)

    
        
    
   

   

       