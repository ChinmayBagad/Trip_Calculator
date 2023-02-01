name_list=[]
 
while True:
    name=input("Enter the names (or 'q' to quit):-")
    if name == "q":
        break
    name_list.append(name)
    

x=len(name_list)
money_spend = []

print(name_list)
for i in range (x):
    sel=int(input("Enter the Number of the person from the List:- "))
    if sel >= 0 or sel <x:
         z=name_list[sel]
         spend = []
    else:
        print("Plaese Enter a Valide Number from the list")  

    while True:
            exp=input("Enter the Amount spend by "+ z + "(or 'q' to exit):-" )
            if exp == 'q':
               break

            exp=float(exp)
            spend.append(exp)
            total=sum(spend)

    


    money_spend.append(total)
    ultra=sum(money_spend)
    
    # Distribution Part
per_person=ultra/x
print("Total Money Spend = ",ultra)
print("Per Person Cost = ",per_person) 
        

        






        
    
        
    
   

   

       