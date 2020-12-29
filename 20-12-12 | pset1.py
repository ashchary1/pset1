#This program is in relation to MIT OPEN COURSEWARE - PSET 1

#total_cost 
#portion_down_payment = 0.25
#annual return = r
#current_savings*r/12
#annual salary = 150000
#portion_saved = ..20
#monthly salary = (annual salary/12)

print ("Welcome to a program Pset1, this program's f(x) is meant ot help calx down payments onto housing properties" + "Please follow prompts and input data")
annual_salary = int (input ("What is your annual salary")) # requesting user to input annual salary + assigning variable
portion_saved = int (input  ("What is the portion of the salary to be saved as a decimal?")) # requesting user to input portion saved of salary + assigning variable 
total_cost = int (input ("What is the cost of your dream home?")) # requesting user to input cost of dream home + assigning variable
print ("So just to confirm, your annual salary is", annual_salary, "the portion you will save monthly will be ", portion_saved, "and lastly your dream home costs", total_cost)

portion_down_payment = 0.25 # we are assuming that his dream house would req a 25% down pmt
current_savings = 0 # zero is the current savings the user would have 
r = 0.04 #return rate of 4% 

down_payment_amount = int(total_cost) * int(portion_down_payment) #calx Total down payment amount in total reqd for dream house based on inputs
monthly_salary = int(annual_salary)/12 #calx monthly salary based on annual salary input
percentage_monthly_savings = int(monthly_salary) * int(portion_saved) # calx total monthly saving
roi_on_savings = int(percentage_monthly_savings)*(r/12)