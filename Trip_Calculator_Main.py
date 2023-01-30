name_list=[]
 
while True:
    name=input("Enter the names (or 'q' to quit):-")
    if name == "q":
        break
    name_list.append(name)

x=len(name_list)

n=print(name_list)
for i in range(x):
    while True:
        z=int(input("Enter the Person Number you want to Select:-"))
        print(name_list[z])






money=float(input("Enter the total amount of money spend:-"))
if money<0:
    print("Please Enter Valide Amount")
else:
    total=money/x
    print("Per person cost=",total)
