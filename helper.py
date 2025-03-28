def days_to_units(days_and_units_dictionary):
    if days_and_units_dictionary["unit"] == "hours":
        return f"{days_and_units_dictionary['days']} days are {int(days_and_units_dictionary['days']) * 24} hours"
    elif days_and_units_dictionary["unit"] == "minutes":
        return f"{days_and_units_dictionary['days']} days are {int(days_and_units_dictionary['days']) * 24 * 60} minutes"
    else:
        return "Invalid unit entered"


def validate_and_execute(days_and_units_dictionary):
    try:
        user_input_number = int(days_and_units_dictionary["days"])

        # we want to do conversion only for positive integers
        if user_input_number > 0:
            calculated_value = days_to_units(days_and_units_dictionary)
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered a 0, please enter a valid positive number")
        else:
            print("you entered a negative number, no conversion for you!")
    except ValueError:
        print("your input is not a valid number. Don't ruin my program!")

user_input_message = "Hey user, enter number of days and corresponding unit for the conversion\n"