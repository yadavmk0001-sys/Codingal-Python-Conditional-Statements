AC = float(input("Please enter the Actual Product : "))
SC = float(input("Please enter the seling price : "))

if (SC > AC):
    amount = SC - AC
    print("Total profit = ", amount)
else:
    print("No Profit")