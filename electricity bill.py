n=int(input("Please enter your bill money  "))
b=0
if (n<=50):
    b=n*0.50
    print(b)
elif (n>50 and n<=150):
    n=n-50
    b=(50*0.50)+(n*0.75)
    print("Total bill payment is",b)
elif (n>150 and n<=250):
    n=n-150
    b=(50*0.50)+(100*0.75)+(n*1.20)
    print("Total bill payment is",b)
elif (n>250):
    n=n-250
    b=(50*0.50)+(100*0.75)+(100*1.20)+(n*1.50)
    print("Total bill payment is",b)
tax= (b/100)*20
total_bill= b+tax
print("TOTAL TAX BY THE ELECTRICITY DEPARTMENT OF INDIA",total_bill)
    
exit()
