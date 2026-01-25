## 6.100A PSet 1: Part C
## Name:
## Time Spent:
## Collaborators:

##############################################
## Get user input for initial_deposit below ##
##############################################

initial_deposit = float(input("Enter the initial deposit: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

portion_down_payment = 0.25
years = 3
months = 12 * years
high = 1
low = 0
r = ( high + low) / 2
steps = 1
amount_saved = initial_deposit * (1 + r/12) ** months
down_payment = 800000 * portion_down_payment
##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################

while  abs(amount_saved - down_payment) > 100 :
    steps += 1
    if  amount_saved - down_payment > 100 :
        high = r
    elif  amount_saved - down_payment < -100 :
        low = r
    r = ( high + low ) / 2
    amount_saved = initial_deposit * (1 + r/12) ** months
print(f"Best savings rate: {r}")   
print(f"Steps in bisection search: {steps}")