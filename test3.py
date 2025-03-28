#import helper  #here we are importing entire module
from helper import validate_and_execute, user_input_message  #here we are not importing entire module, just importing required function
#import helper as h

user_input = ""
while user_input.lower() != "exit":
    user_input = input(user_input_message)
    if ":" in user_input:
        days_and_units = user_input.split(":")
        if len(days_and_units) == 2:
            days_and_units_dictionary = {"days":days_and_units[0], "unit":days_and_units[1]}
            validate_and_execute(days_and_units_dictionary)
        else:
            print("Invalid input format. Please enter in 'days:unit' format (e.g., 5:hours).")
    else:
        print("Invalid input. Please enter days and unit separated by a colon (e.g., 5:hours).")