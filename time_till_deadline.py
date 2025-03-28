from _datetime import datetime

user_input = input("Enter your project name and future deadline in mm/dd/yyyy format separated by : \n")

if ":" in user_input:
    input_list = user_input.split(":")
    if len(input_list) == 2:  # Ensure valid input structure
        project_name = input_list[0].strip()
        deadline = input_list[1].strip()
        try:
            deadline_date = datetime.strptime(deadline, "%m/%d/%Y")
            today_date = datetime.today()
            if deadline_date < today_date:
                print("Deadline has already passed.Please select another project with a future deadline.")
            else:
                difference = deadline_date - today_date
                print(f"The time till deadline is {difference.days}")
        except ValueError:
            print("Invalid date format. Please use mm/dd/yyyy format.")
    else:
        print("Provide valid input")
    #print(f"Project name: {project_name}","\n", f"Deadline: {deadline}")

else:
    print("Invalid input format. Please follow the instructions & data should be separated by a colon (:).\n")