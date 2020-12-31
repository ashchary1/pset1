#This program is in relation to MIT OPEN COURSEWARE - PSET 1
import math

#total_cost 
#portion_down_payment = 0.25
#annual return = r
#current_savings*r/12
#annual salary = 150000
#portion_saved = ..20
#monthly salary = (annual salary/12)

print ("Welcome to a program Pset1, this program's f(x) is meant ot help calx down payments onto housing properties" + "Please follow prompts and input data")
annual_salary = float (input ("What is your annual salary")) # requesting user to input annual salary + assigning variable
portion_saved = float (input  ("What is the portion of the salary to be saved as a decimal?")) # requesting user to input portion saved of salary + assigning variable 
total_cost = float (input ("What is the cost of your dream home?")) # requesting user to input cost of dream home + assigning variable
print ("So just to confirm, your annual salary is", annual_salary, "the portion you will save monthly will be ", portion_saved, "and lastly your dream home costs", total_cost)

portion_down_payment = float(0.25) # we are assuming that his dream house would req a 25% down pmt
current_savings = float(0) # zero is the current savings the user would have 
annual_rate = float(0.04) #return rate of 4% 
monthly_interest_rate = annual_rate/12

down_payment_amount = float(total_cost) * portion_down_payment #calx Total down payment amount in total reqd for dream house based on inputs
monthly_salary = float(annual_salary)/12 #calx monthly salary based on annual salary input
amount_saved_monthly = monthly_salary * (portion_saved / 100) # calx total monthly saving

total_month_count = 0

while current_savings <= down_payment_amount:
    total_month_count += 1
    current_savings = (current_savings + amount_saved_monthly) * (1 + monthly_interest_rate)

current_savings = math.floor(current_savings)

print("You will have saved", current_savings, "after", total_month_count, "months")