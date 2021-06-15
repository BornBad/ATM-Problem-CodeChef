def atm(withdrawl_amount, total_amount):
    if((withdrawl_amount or total_amount)<=2000):
        if(withdrawl_amount%5==0 and withdrawl_amount<total_amount):
            closing_amount=total_amount-(withdrawl_amount+0.50)
            print('%.3f'%closing_amount)
        elif(withdrawl_amount%5!=0 or withdrawl_amount>=total_amount):
            print('%.3f'%total_amount)
    else:
        print("You can not operate as you are exceeding the limit")
    return withdrawl_amount,total_amount

a,b=(input("Enter the amounts:")).split()
a=int(a)
b=float(b)
atm(a,b)

