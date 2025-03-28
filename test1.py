
calculate_to_units = 24 * 60 * 60
unit = "seconds"
#calculate_to_units = 24
#unit = "hours"

def days_to_unit(num_of_days):
    if num_of_days > 0:
        return print(f"{num_of_days} days have {num_of_days * calculate_to_units} {unit}")
    else:
        return print("You entered a non-positive number of days!")
    #print(custom_message)
    

#my_value = days_to_unit(20)
#print(my_value)
days = int(input("Hey user, Enter the number of days and I will convert it to seconds!\n"))
days_to_unit(days)


#def scope_check():
#    print(unit)
#    print(num_of_days)

#scope_check()  


