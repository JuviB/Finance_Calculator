# Import math module used for when calculating simple and compound interest

import math

# Display the investment and bond definitions as specified in the requirements using print() command

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

# Request the user to enter their preffered calculation type, whether it be investment or bond, added the .lower() function incase the user were to enter their input in capital letters
 
calc_type = input("Enter either 'investment or 'bond' from the menu above to proceed:").lower()

# 'if' statement triggered when the 'investment' string is entered
# Request user to enter the deposit amount (p)(saved as float data type), interest rate (r)(saved as float data type) and number of years of investment (n)(saved as integer data type)
# Request user to enter whether they want the 'simple' or 'compound' interest type, of which an 'if' statement will trigger the simple interest formula, and the 'else' statement will trigger the compound interest formula

if calc_type == "investment":
    p = float(input("Please enter the amount of money you will be depositing:"))
    r = float(input("Please enter the interest rate:"))/100
    t = int(input("Please enter the number of years you plan on investing for:"))
    interest = input("Please enter whether you want to use 'simple' or 'compound' interest:")
    
    if interest == "simple":
        a = p*(1 + r*t)
        
    else:
        a = p*math.pow((1 + r),t)
        
    # Priints a sentence displaying the users input for the various categories as well as displays the accumulated amount using the 'f string' method
 
    print(f"Your accumulated amount based on the 'investment' type, using {interest} interest at an interest rate of {r} for {t} number of years, your accumulated amount is R{a}.")

# 'elif' statement used for when the user inputs neither 'investment' or 'bond' or nothing at all when requested in calc_type variable above, an appropriate error message will also be displayed 
# The 'or' boolean was used to integrate the various incorrect options that could be entered
   
elif calc_type == None or calc_type != "investment" and calc_type != "bond" or calc_type == " ":
    print("You have not entered a valid calculation type, please enter either 'investment' or 'bond'")
    
# 'else' statement is triggered when the 'bond' string is entered
# Request user to enter the present value of the house (p)(saved as float data type), interest rate (i)(saved as float data type)(calculated at a monthly rate) and number of months to repay the bond (n)(saved as integer data type)
# The 'repayment' variable is created to store the formula used for repayment
           
else:
    p = float(input("Please enter the present value of the house:"))
    i = float(input("Please enter the interest rate:"))/100/12
    n = int(input("Please enter the number of months you plan to take to repay the bond:"))
    
    # The 'repayment' variable is created to store the formula used for repayment of the bond
    
    repayment = (i*p)/(1-(1+i)**(-n))
    
    # Priints a sentence displaying the users input for the various categories as well as displays the accumulated repayment using the 'f string' method
    
    print(f"Your monthly repayment based on the 'bond' type at an interest rate of {i} for {n} months, your accumulated amount is R{repayment}.")
        
    

    
