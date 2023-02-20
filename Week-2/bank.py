#write a program that calculates 16% tax on income
#ranging between 100k - 150k

#19% tax income is between 150k - 300k
#30% tax income is above 300k
#5% if income is less 100k


#print gross income , net imcome

gross_income = int(input("what is your gross"))
tax_group_A = (gross_income * 0.05)
tax_group_B = (gross_income * 0.16)
tax_group_C = (gross_income * 0.19)
tax_group_D = (gross_income * 0.30)

if gross_income < 100000:
    print("gross_income:",gross_income)
    print("net income",gross_income - tax_group_A)
elif(gross_income >= 100000) & (gross_income < 150000) :
    print("Net income:", gross_income - tax_group_B)
    print("gross_income:",gross_income)

elif(gross_income >=150000) & (gross_income < 300000):
    print("Net income:", gross_income - tax_group_C)
    print("gross_income:",gross_income)
else:
    (gross_income >= 300000)
    print("Net income:", gross_income - tax_group_D)
    print("gross_income:",gross_income)

   
