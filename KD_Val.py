# Kaitlyn Deschner
# Custom Validation Functions

# Ensures input is an integer with a minimum and maximum value. No custom message.
def val_int_no_message(min, max):
    while True:
        try:
            num = int(input(f"\tPlease enter number: ")) # Prompts user for input
            if num < min or num > max:
                print(f"\n\tError: Range is {min:2d} - {max:2d}. Please re-enter.") # Prints error message if input outside min/max range
            else:
                return num
        except ValueError:
            print("\n\tError: Illegal character(s) in input - Please re-enter.") # Prints error message is input not an integer


# Ensures input is an integer with a minimum and maximum value. Custom message.
def val_int_message(msg, min, max):
    while True:
        try:
            num = int(input(msg)) # Prompts user for input, allows for custom message
            if num < min or num > max:
                print(f"\n\tError: Range is {min} - {max:}. Please re-enter.") # Prints error message if input outside min/max range
            else:
                return num
        except ValueError:
            print("\n\tError: Illegal character(s) in input - Please re-enter.") # Prints error message if input not an integer


# Ensures input is an integer. Displays custom message.
def val_int_no_range(msg):
    while True:
        try:
            num = int(input(msg)) # Prompts user for input, allows for custom message
            return num
        except ValueError:
            print("\n\tError: Illegal character(s) in input - Please re-enter.") # Prints error message if input not an integer


# Ensure input contains letters only
def val_forename():
    while True:
        forename = input("\n\tPlease enter the competitor's forename: ").strip() # Prompts user for input
        if all(c.isalpha() or c.isspace() for c in forename) and any(c.isalpha() for c in forename): # Ensures input contains letters only
            return forename # Returns input if it only contains letters
        print("\n\tError: Please enter letters only.") # Prints error message if input contains special characters or numeric values


# Ensure input contains letters only
def val_surname():
    while True:
        surname = input("\tPlease enter the competitor's surname: ").strip() # Prompts user for input
        if all(c.isalpha() or c.isspace() for c in surname) and any(c.isalpha() for c in surname): # Ensures input contains letters only
            return surname # returns input if it only contains letters
        print("\n\tError: Please enter letters only.")  # Prints error message if input contains special characters or numeric values


# Ensure input contains letters only
def val_letters(msg):
    while True:
        letters = input(msg).strip() # Prompts user for input
        if all(c.isalpha() or c.isspace() for c in letters) and any(c.isalpha() for c in letters): # Ensures input contains letters only
            return letters # returns input if it only contains letters
        print("\n\tError: Please enter letters only.")  # Prints error message if input contains special characters or numeric values


# Ensures input is either 'Male' or 'Female'
def val_gender():
    while True:
        gender = input("\tPlease enter the competitor's gender (Male/Female): ").strip().capitalize() # Prompts user for input
        if gender in ["Male", "Female"]: # Checks if input is 'Male' or 'Female'
            return gender # returns input if true
        print("\n\tPlease enter either 'Male' or 'Female'") # Prints error message if input is not 'Male' or 'Female'


# Ensures the competitors age is between min and max values
def val_age(min, max):
    while True:
        try:
            age = int(input("\tPlease enter the competitor's age: ")) # Prompts user for input (integer only)
            if min <= age <= max: # Checks if input is between min and max range
                return age # Returns input if true
            print(f"\n\tError: The age range for competitions is {min} - {max}. Please re-enter.") # Displays error message if input not in custom range
        except ValueError:
            print("\n\tError: Please enter a numeric value.") # Displays error message if input not an integer


# Ensures event name does not contain numbers
def val_event_name(msg):
    while True:
        event_name = input(msg).strip() # Prompts user for input
        if any(c.isalpha() for c in event_name) and not any(c.isdigit() for c in event_name): # Checks input does not contain numbers
            return event_name # Returns input if true
        print("\n\tEvent name cannot contain numbers. Please re-enter.") # Displays error message if input contains numeric values


# Validates event times
def val_result(type_of_time):
    max_times = {
        'swim': 60,
        'cycle': 120,
        'run': 90
    } # Sets maximum values for individual times

    while True:
        try:
            time = int(input(f"\tPlease enter {type_of_time} time (minutes, max {max_times[type_of_time]}): ")) # Prompts user for input
            if 0 <= time <= max_times[type_of_time]: # Checks times are below maximum times
                return time # Return times if true
            print(f"\n\tError: Time must be between 0 and {max_times[type_of_time]} minutes. Please re-enter.") # Displays error message if inputted time is outside range
        except ValueError:
            print("\n\tError: Please enter a valid number.") # Displays error message if input not an integer


# Validation function to update results
def val_update_result(prompt, current_value, max_value):
    while True:
        new_time = input(prompt).strip() # prompts user for input
        if not new_time:
            return current_value # Keeps current value if no change
        try:
            new_time = int(new_time)
            if 0 <= new_time <= max_value: # Checks time is within custom range
                return new_time # returns updated time if true
            else:
                print(f"\tError: Time must be between 0 and {max_value} minutes.") # Displays error message if time is outside specified range
        except ValueError:
            print("\tError: Please enter a valid number or press Enter to keep the current time.") # Displays error message if input not an integer


# Check for duplicate entries
def val_dup_entry(comp_no, event_no, results):
    return any(r['comp_no'] == comp_no and r['event_no'] == event_no for r in results) # Checks for duplication in results


# Validate yes/no input
def val_yes_no(msg):
    while True:
        response = input(msg).strip().lower() # Prompts user for input
        if response in ['y', 'yes']:
            return True # Continues operation if 'yes' selected
        if response in ['n', 'no']:
            return False # Cancels operation if 'no' selected
        print("\n\tError: Please enter 'yes' or 'no'") # Displays error message if invalid input


# Validation for updating existing values
def val_update(msg, current_value):
    new_value = input(msg).strip() # Prompts user for input
    return new_value if new_value else current_value # Updates value if changes made, otherwise keeps the same value

# Validation for ranges based on current data
def val_range(num):
    if not num:
        return 1, 999  # Default range if no numbers exist
    return min(num), max(num)