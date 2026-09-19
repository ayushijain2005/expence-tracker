# #expence tracker

# expenseslist=[]
# print("welcome to the expence tracker : kharcha kam kra kro ")

# while True:
#     print("=====menu=====")
#     print("1. Add expense")
#     print("2. View expenses")
#     print("3.view total kharcha")
#     print("4.exit")

#     choice=int(input("Enter your choice (1-4): "))
# #add expences 

#     if(choice==1):
#         date=input("kis date pr kharcha kiya tha??")
#         category=input("kis category me kharcha kiya tha??(food,transport,entertainment,other):")
#         description=input("kharcha ka description likho:")
#         amount=float(input("kharcha ki rakam likho:"))

#         expense={
#             "date":date,
#             "category":category,
#             "description":description,
#             "amount":amount

#         }
#         expenseslist.append(expense)
#         print("\n DONE bro kharcha add ho gya hai \n")

#         #view expences
#     elif(choice==2):
#             if len(expenseslist)==0:
#                 print("koi kharcha nahi hai....jao phale kharcha kro ")
#             else:
#                 print("=====kharcha ki list=====")
#                 count=1
#                 for eachkharcha in expenseslist:
#                     print(f"kharcha number:{count} -> {eachkharcha["date"]}, {eachkharcha["category"]}, {eachkharcha["description"]}, {eachkharcha["amount"]}")

#                     count+=1

#     #view total spending     

#     elif(choice==3):
#         total=0
#         for eachkharcha in expenseslist:
#             total+=eachkharcha["amount"]

# #exit
#     elif(choice==4):
#          print("dhanyabaad apne hamara system use kiya ")
#          break

#     else:
#         print("galat choice bro 1-4 me se choose kro ") PS C:\Users\jaina\OneDrive\Documents\one drive\OneDrive\Attachments\python expence tracker> python -u "c:\Users\jaina\OneDrive\Documents\one drive\OneDrive\Attachments\python expence tracker\main.py" 
expenseslist=[]

print("welcome to the expense tracker : kharcha kam kara kro")

while True:
    print("===== MENU =====")
    print("1. Add expense")
    print("2. View expenses")
    print("3. View total kharcha")
    print("4. Exit")

    choice=int(input("Enter your choice (1-4): "))

    # Add expense
    if choice == 1:
        date=input("Kis date par kharcha kiya tha? ")
        category=input("Kis category me kharcha kiya tha? (food, transport, entertainment, other): ")
        description=input("Kharcha ka description likho: ")
        amount=float(input("Kharcha ki rakam likho: "))

        expense={
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenseslist.append(expense)

        print("\nDONE bro! Kharcha add ho gaya hai.\n")

    # View expenses
    elif choice == 2:
        if len(expenseslist) == 0:
            print("Koi kharcha nahi hai.... jao pehle kharcha karo 😭")
        else:
            print("===== KHARCHA KI LIST =====")

            count=1

            for eachkharcha in expenseslist:
                print(f"Kharcha number: {count} -> {eachkharcha['date']}, {eachkharcha['category']}, {eachkharcha['description']}, ₹{eachkharcha['amount']}")

                count += 1

    # View total spending
    elif choice == 3:
        total=0

        for eachkharcha in expenseslist:
            total += eachkharcha["amount"]

        print(f"Total kharcha = ₹{total}")

    # Exit
    elif choice == 4:
        print("Dhanyabaad! Aapne hamara system use kiya.")
        break

    else:
        print("Galat choice bro! 1-4 me se choose karo.")