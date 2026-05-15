# Kaitlyn Deschner
# PFA2_STU30035781

import os # Enables interaction with operating system
import random # Allows results to be randomly selected
import KD_Val # Imports custom validation functions

# Global variables for file names
comp_file = "competitors.txt" # Registration file for competitors
event_file = "events.txt" # Registration file for events
result_file = "results.txt" # Registration file for results


# Creates a list of competitors
def create_competitors():
    # Returns list of default dictionaries containing competitor information
    return [
        {"comp_no": 1, "surname": "Phelps", "forename": "Jack", "gender": "Male", "age": "23"},
        {"comp_no": 2, "surname": "Ryder", "forename": "Miles", "gender": "Male", "age": "39"},
        {"comp_no": 3, "surname": "Atherton", "forename": "Trish", "gender": "Female", "age": "55"},
        {"comp_no": 4, "surname": "Wheeler", "forename": "Finn", "gender": "Male", "age": "20"},
        {"comp_no": 5, "surname": "Waters", "forename": "Chase", "gender": "Male", "age": "18"},
        {"comp_no": 6, "surname": "Anderson", "forename": "Connor", "gender": "Male", "age": "28"},
        {"comp_no": 7, "surname": "Thompson", "forename": "Sarah", "gender": "Female", "age": "24"},
        {"comp_no": 8, "surname": "Peterson", "forename": "Dylan", "gender": "Male", "age": "31"},
        {"comp_no": 9, "surname": "McKenzie", "forename": "Hailey", "gender": "Female", "age": "26"},
        {"comp_no": 10, "surname": "Larson", "forename": "Jacob", "gender": "Male", "age": "29"},
        {"comp_no": 11, "surname": "Fisher", "forename": "Ava", "gender": "Female", "age": "22"},
        {"comp_no": 12, "surname": "Schmidt", "forename": "Brandon", "gender": "Male", "age": "27"},
        {"comp_no": 13, "surname": "Wolfe", "forename": "Megan", "gender": "Female", "age": "25"},
        {"comp_no": 14, "surname": "Taylor", "forename": "Liam", "gender": "Male", "age": "23"},
        {"comp_no": 15, "surname": "Johnson", "forename": "Ella", "gender": "Female", "age": "30"},
        {"comp_no": 16, "surname": "Davies", "forename": "Nathan", "gender": "Male", "age": "33"},
        {"comp_no": 17, "surname": "Olson", "forename": "Grace", "gender": "Female", "age": "21"},
        {"comp_no": 18, "surname": "Miller", "forename": "Benjamin", "gender": "Male", "age": "36"},
        {"comp_no": 19, "surname": "Wilson", "forename": "Emma", "gender": "Female", "age": "19"},
        {"comp_no": 20, "surname": "Sullivan", "forename": "James", "gender": "Male", "age": "28"},
        {"comp_no": 21, "surname": "Ross", "forename": "Madison", "gender": "Female", "age": "24"},
        {"comp_no": 22, "surname": "Hughes", "forename": "Evan", "gender": "Male", "age": "32"},
        {"comp_no": 23, "surname": "Benson", "forename": "Charlotte", "gender": "Female", "age": "27"},
        {"comp_no": 24, "surname": "Campbell", "forename": "Logan", "gender": "Male", "age": "20"},
        {"comp_no": 25, "surname": "Reid", "forename": "Zoe", "gender": "Female", "age": "23"},
        {"comp_no": 26, "surname": "Nelson", "forename": "Ryan", "gender": "Male", "age": "34"},
        {"comp_no": 27, "surname": "Brown", "forename": "Mia", "gender": "Female", "age": "26"},
        {"comp_no": 28, "surname": "Harrison", "forename": "Ethan", "gender": "Male", "age": "22"},
        {"comp_no": 29, "surname": "Parker", "forename": "Avery", "gender": "Female", "age": "25"},
        {"comp_no": 30, "surname": "Stewart", "forename": "Lucas", "gender": "Male", "age": "31"}
    ]


# Creates a list of events
def create_events():
    # Returns a list of dictionaries containing event information
    return [
        {"event_no": 100, "event_name": "Southern Sweat, Gears & Tears triathlon"},
        {"event_no": 101, "event_name": "Portadown Endurance Triathlon"},
        {"event_no": 102, "event_name": "Belfast Challenge"}
    ]


# Function to generate random results for events
def random_results(competitors, events):
    global results
    results = []  # Initialize results list
    for competitor in competitors:
        comp_no = competitor["comp_no"]  # Access competitor no
        # Assign each competitor to random events (between 1-3)
        num_events = random.randint(1, 3)
        assigned_events = random.sample(events, num_events)
        for event in assigned_events:
            event_no = event["event_no"]  # Access event no
            # Generate random times
            swim = random.randint(15, 40)  # Swim time between 15-40 min
            cycle = random.randint(30, 120)  # Cycle time between 30-120 min
            run = random.randint(15, 60)  # Run time between 15-60 min
            total = swim + cycle + run # Calculates total time

            # Append the result
            results.append({
                "comp_no": comp_no,
                "event_no": event_no,
                "swim": swim,
                "cycle": cycle,
                "run": run,
                "total": total
            })
    return results


# File operations for competitors
def write_comp_file(competitors):  # Writes competitors to file
    with open(comp_file, 'w') as f:
        for comp in competitors:
            f.write(f"{comp['comp_no']},{comp['surname']},{comp['forename']},{comp['gender']},{comp['age']}\n")

def read_comp_file():  # Reads competitors from file
    competitors = []
    if os.path.exists(comp_file):
        with open(comp_file, 'r') as f:
            for line in f:
                comp_no, surname, forename, gender, age = line.strip().split(',')
                competitors.append({
                    "comp_no": int(comp_no),
                    "surname": surname.strip(),
                    "forename": forename.strip(),
                    "gender": gender.strip(),
                    "age": int(age)
                })
    return competitors


# File operations for events
def write_event_file(events): # Writes events to file
    with open(event_file, 'w') as f:
        for event in events:
            f.write(f"{event['event_no']},{event['event_name']}\n")


def read_event_file(): # Reads events from file
    events = []
    if os.path.exists(event_file):
        with open(event_file, 'r') as f:
            for line in f:
                event_no, event_name = line.strip().split(',', 1)
                events.append({
                    "event_no": int(event_no),
                    "event_name": event_name
                })
    return events


# File operations for results
def write_result_file(results): # Writes results to file
    with open(result_file, 'w') as f:
        for result in results:
            f.write(
                f"{result['comp_no']} {result['event_no']} {result['swim']} {result['cycle']} {result['run']} {result['total']}\n")


def read_result_file(): # Reads results from file
    results = []
    if os.path.exists(result_file):
        with open(result_file, 'r') as f:
            for line in f:
                comp_no, event_no, swim, cycle, run, total = map(int, line.strip().split())
                results.append({
                    "comp_no": comp_no,
                    "event_no": event_no,
                    "swim": swim,
                    "cycle": cycle,
                    "run": run,
                    "total": total
                })
    return results


# Function to displays all competitors
def display_comp():
    competitors = read_comp_file()
    if not competitors:
        print("\n\tSorry - No competitors found") # Displays error message if no competitors in system
        return # Returns to previous session
    print(f"\n\n\t{'Competitor No':<15} {'Forename':<20} {'Surname':<20} {'Gender':<10} {'Age':<5}") # Displays Titles
    print("\t" + "-" * 70) # Prints divider line
    for comp in competitors:
        print(f"\t{comp['comp_no']:<15} {comp['forename']:<20} {comp['surname']:<20} {comp['gender']:<10} {comp['age']:<5}") # Displays competitor information


# Function to display all events
def display_events():
    events = read_event_file()
    if not events:
        # Prints error message if no events registered
        print("\n\tSorry - No events found")
        return # Returns to previous session

    print("\n\n\tNo.  Event Name") # Prints titles
    print("\t----------------------------------------") # prints divider line
    for event in events:
        # Displays all events in system
        print(f"\t{event['event_no']:<5}{event['event_name']}")


# Function to display all results
def display_results():
    results = read_result_file()
    competitors = read_comp_file()
    events = read_event_file()

    if not results:
        print("\n\tSorry - No results found") # Prints error message if no results in system
        return # Returns to previous session

    print("\n\n\tComp No.  Event No.  Swim  Cycle  Run   Total") # print titles
    print("\t---------------------------------------------") # prints divider line
    for result in results:
        # Displays all results in system
        print(
            f"\t{result['comp_no']:<10}{result['event_no']:<11}{result['swim']:<6}{result['cycle']:<7}{result['run']:<6}{result['total']}")


# Function to add new competitors
def add_comp():
    print("\n\t--- Add Competitor ---") # Prints title
    competitors = read_comp_file() # Load all competitors from competitor file into a list

    while True:
        forename = KD_Val.val_forename() # Prompts user for input
        surname = KD_Val.val_surname() # Prompts user for input

        if any(c['forename'].lower() == forename.lower() and c['surname'].lower() == surname.lower() for c in competitors): # Checks for duplicate competitors
            print("\n\tA competitor with this name already exists. Please enter a different name.") # prints error message if duplicate competitor
        else:
            break

    gender = KD_Val.val_gender() # Prompts user for input
    age = KD_Val.val_age(18, 150) # Prompts user for input

    comp_no = max([c['comp_no'] for c in competitors], default=1) + 1 # Automatically assigned competitor no, finding max competitor no and incrementing by 1

    new_competitor = {
        "comp_no": comp_no,
        "surname": surname,
        "forename": forename,
        "gender": gender,
        "age": age
    }

    competitors.append(new_competitor) # Adds new competitor to list of competitors
    write_comp_file(competitors) # Saves updated competitors list to file

    print(f"\n\tCompetitor: {forename} {surname} (Competitor No: {comp_no}) added successfully") # prints message if new competitor has been added successfully

# Function to add new events
def add_event():
    print("\n\t--- Add Event ---") # prints title

    events = read_event_file() # Load all events from storage file into a list

    while True:
        # Prompts user for event details
        event_name = KD_Val.val_event_name("\n\tPlease enter event name: ").strip()

        # Check if an event with the same name already exists
        if any(event['event_name'].lower() == event_name.lower() for event in events):
            print("\n\tAn event with this name already exists. Please enter a different name.") # prints error message if duplicate event exists
        else:
            break

    # Generates new event number (finds max event number and increments by 1)
    event_no = max([e['event_no'] for e in events], default=100) + 1

    new_event = {
        "event_no": event_no,
        "event_name": event_name
    }

    events.append(new_event) # Add new event to the list of all events
    write_event_file(events) # Saves updated events list to the storage file
    print(f"\n\tEvent: {event_name} (Event No: {event_no}) added successfully") # prints success message if new event created


# Function to record results/times for an event
def add_results():
    print("\n\t--- Add Results ---") # prints title

    competitors = read_comp_file() # Loads all competitors from the storage file into a list
    events = read_event_file() # Loads all events from the storage file into a list
    results = read_result_file() # Loads all results form the storage file into a list

    # Gather min and max ranges from competitors and events files
    comp_numbers = [c['comp_no'] for c in competitors]
    event_numbers = [e['event_no'] for e in events]
    min_comp, max_comp = KD_Val.val_range(comp_numbers)
    min_event, max_event = KD_Val.val_range(event_numbers)

    # Display all competitors
    display_comp()

    # Prompt user for competitor number
    while True:
        comp_no = KD_Val.val_int_message("\n\tPlease enter competitor number: ", min_comp, max_comp)
        comp = next((c for c in competitors if c['comp_no'] == comp_no), None)
        if comp:
            break
        print(f"\n\tCompetitor Number must be between {min_comp} - {max_comp}. Please re-enter.") # print error message if input out of range

    print(f"\n\tSelected competitor: {comp['forename']} {comp['surname']} (Competitor No: {comp_no})") # prints message confirming competitor selected

    # Display all events
    display_events()

    # Prompt user for event number
    while True:
        event_no = KD_Val.val_int_message("\n\tPlease enter event number: ", min_event, max_event)
        event = next((e for e in events if e['event_no'] == event_no), None)
        if event:
            break
        print(f"\n\tEvent number must be between {min_event} - {max_event}. Please re-enter.") # prints error message if input outside range

    print(f"\n\tSelected event: {event['event_name']} (Event No: {event_no})") # prints message confirming event selected

    # Check for duplicate entry using validation function (val_dup_entry)
    if KD_Val.val_dup_entry(comp_no, event_no, results):
        print(f"\n\tResult already exists for {comp['forename']} {comp['surname']} in {event['event_name']}") # prints error message if result already exists
        return # Return to previous operation

    # Get event times using val_result
    print(f"\n\tRecording times for {comp['forename']} {comp['surname']} in {event['event_name']}")
    swim = KD_Val.val_result('swim')
    cycle = KD_Val.val_result('cycle')
    run = KD_Val.val_result('run')
    total = swim + cycle + run

    # Add new result
    results.append({
        "comp_no": comp_no,
        "event_no": event_no,
        "swim": swim,
        "cycle": cycle,
        "run": run,
        "total": total
    })

    write_result_file(results) # Saves the updated result to the list of all results
    print(f"\n\tResult recorded successfully for {comp['forename']} {comp['surname']} in {event['event_name']}") # prints message confirming new result has been added


# Function to update competitor details
def update_comp():
    print("\n\t--- Update Competitor ---") # prints title
    display_comp() # displays all competitors
    comp_no = KD_Val.val_int_message("\n\tPlease enter competitor number: ", 1, 999) # prompts user for input

    competitors = read_comp_file() # Loads all competitors from storage file into a list
    comp = next((c for c in competitors if c['comp_no'] == comp_no), None)
    if not comp:
        print("\n\tSorry - Competitor not found") # prints error message if competitor not found
        return # returns to previous operation

    print(f"\n\tUpdating competitor {comp['forename']} {comp['surname']} (Competitor No: {comp['comp_no']})") # prints message confirming which competitor selected

    # Prompt user for new competitor details
    forename_input = input("\tNew forename (or Enter to keep current): ").strip()
    forename = KD_Val.val_letters("\tConfirm forename: ") if forename_input else comp['forename']

    surname_input = input("\tNew surname (or Enter to keep current): ").strip()
    surname = KD_Val.val_letters("\tConfirm surname: ") if surname_input else comp['surname']

    while True:
        gender_input = input("\tNew gender (Male/Female) (or Enter to keep current): ").strip()

        if not gender_input:
            gender = comp['gender']
            break

        try:
            gender = KD_Val.val_gender()
            break
        except Exception:
            print("\n\tError: Please enter either 'Male' or 'Female'") # prints error message if input invalid

    while True:
        age_input = input("\tNew age (or Enter to keep current): ").strip() # prompt user for input

        if not age_input:
            age = int(comp['age'])
            break

        try:
            age = int(age_input)
            if 18 <= age <= 150:
                break
            else:
                print(f"\n\tError: The age range for competitions is 18 - 150. Please re-enter.") # prints error message if input out of range
        except ValueError:
            print("\n\tError: Please enter a numeric value.") # prints error message if input not an integer

    comp.update({
        'forename': forename,
        'surname': surname,
        'gender': gender,
        'age': str(age)
    })

    write_comp_file(competitors) # Saves the updated competitors list to the storage file
    print(f"\n\tCompetitor {forename} {surname} (Competitor No: {comp['comp_no']}) updated successfully") # prints message confirming competitor has been updated


# Updates event details
def update_event():
    print("\n\t--- Update Event ---") # prints title
    display_events() # displays all events
    event_no = KD_Val.val_int_message("\n\tPlease enter Event Number to update: ", 100, 999) # prompts user for input

    events = read_event_file() # loads all events from storage file into a list
    event = next((e for e in events if e['event_no'] == event_no), None)
    if not event:
        print("\n\tSorry - Event not found") # prints error message if event not found
        return # returns to previous operation

    print(f"\n\tUpdating Event: {event['event_name']} (Event No: {event['event_no']})") # prints message confirming which event selected

    # Prompt user for new event details
    updated_event = input("\tNew Event Name (or Enter to keep current): ").strip()
    if updated_event:
        event_name = KD_Val.val_event_name("\tConfirm Event Name: ")
    else:
        event_name = event['event_name']

    event['event_name'] = event_name

    write_event_file(events) # saves updated event list to the storage file
    print(f"\n\tEvent: {event_name} (Event No: {event_no}) updated successfully") # prints message confirming event has been updated


# Function to update results/times
def update_result():
    print("\n\t--- Update Result ---") # prints title
    display_comp()  # Displays all competitors

    # Validate competitor number
    competitors = read_comp_file()
    comp_numbers = [c['comp_no'] for c in competitors]
    min_comp = min(comp_numbers)
    max_comp = max(comp_numbers)

    while True:
        comp_no = KD_Val.val_int_message(f"\n\tPlease enter competitor number ({min_comp}-{max_comp}): ", min_comp, max_comp) # prompts user for input
        if comp_no in comp_numbers:
            break

    display_events()  # Displays all events

    # Validate event number
    events = read_event_file()
    event_numbers = [e['event_no'] for e in events]
    min_event = min(event_numbers)
    max_event = max(event_numbers)

    while True:
        event_no = KD_Val.val_int_message(f"\n\tPlease enter event number ({min_event}-{max_event}): ", min_event, max_event) # prompts user for input
        if event_no in event_numbers:
            break

    results = read_result_file() # loads all results form storage file into a list
    result = next((r for r in results if r['comp_no'] == comp_no and r['event_no'] == event_no), None)

    if not result:
        print("\n\tSorry - Result not found for this competitor in this event") # prints error message if not found
        return # returns to previous operation

    print("\n\t--- Updating Result ---") # prints title

    # Get confirmation before proceeding
    comp = next((c for c in competitors if c['comp_no'] == comp_no), None)
    event = next((e for e in events if e['event_no'] == event_no), None)

    print(f"\n\tCurrent results for {comp['forename']} {comp['surname']} in {event['event_name']}:")
    print(f"\tCurrent Swim Time: {result['swim']} min")
    print(f"\tCurrent Cycle Time: {result['cycle']} min")
    print(f"\tCurrent Run Time: {result['run']} min")

    # Use existing validation functions for result updates
    swim = KD_Val.val_update_result(
        f"\n\tNew swim time (current: {result['swim']} min, or Enter to keep current): ",
        result['swim'],
        60
    )

    cycle = KD_Val.val_update_result(
        f"\tNew cycle time (current: {result['cycle']} min, or Enter to keep current): ",
        result['cycle'],
        120
    )

    run = KD_Val.val_update_result(
        f"\tNew run time (current: {result['run']} min, or Enter to keep current): ",
        result['run'],
        90
    )

    result.update({
        'swim': swim,
        'cycle': cycle,
        'run': run,
        'total': swim + cycle + run
    })

    write_result_file(results) # saves updated results list to storage file
    print("\n\tResult updated successfully") # prints message confirming result has been updated

    # Confirmation of updated times
    print(f"\n\tUpdated results for {comp['forename']} {comp['surname']} in {event['event_name']}:")
    print(f"\tSwim: {swim} min")
    print(f"\tCycle: {cycle} min")
    print(f"\tRun: {run} min")
    print(f"\tTotal: {swim + cycle + run} min")


# Delete Functions
# Function to delete competitors
def delete_comp():
    print("\n\t--- Delete Competitor ---") # prints title
    display_comp() # displays all competitors
    comp_no = KD_Val.val_int_message("\n\tPlease enter competitor number: ", 1, 999) # prompts user for input

    competitors = read_comp_file() # loads all competitors from storage file into a list
    comp = next((c for c in competitors if c['comp_no'] == comp_no), None)
    if not comp:
        print("\n\tSorry - Competitor not found") # prints error message if not found
        return # returns to previous operation

    confirm = input(f"\tPlease confirm deletion of {comp['forename']} {comp['surname']} (y/n): ").lower() # prompts user for input
    if confirm != 'y':
        return # returns to previous operation

    competitors = [c for c in competitors if c['comp_no'] != comp_no]
    write_comp_file(competitors) # saves updated competitors list to storage file
    print(f"\n\tCompetitor Number {comp_no} deleted successfully") # prints success message


# Function to delete events
def delete_event():
    print("\n\t--- Delete Event ---") # prints title
    display_events() # displays all events
    event_no = KD_Val.val_int_message("\n\tPlease enter event number: ", 100, 999) # prompts user for input

    events = read_event_file() # loads all events from storage file into a list
    event = next((e for e in events if e['event_no'] == event_no), None)
    if not event:
        print("\n\tSorry - Event not found") # prints error message if event not found
        return

    confirm = input(f"\tPlease confirm deletion of {event['event_name']} (y/n): ").lower() # prompts user for input
    if confirm != 'y':
        return # return to previous operation

    events = [e for e in events if e['event_no'] != event_no]
    write_event_file(events) # saves updated events list to storage file
    print(f"\n\tEvent Number {event_no} deleted successfully") # prints success message


# Function to delete results
def delete_result():
    print("\n\t--- Delete Result ---") # prints title
    display_results() # displays all results

    # Validate competitor number
    competitors = read_comp_file() # loads all competitors from storage file into a list
    comp_numbers = [c['comp_no'] for c in competitors]
    min_comp = min(comp_numbers) # finds min competitor number
    max_comp = max(comp_numbers) # finds max competitor number

    while True:
        comp_no = KD_Val.val_int_message(f"\n\tPlease enter competitor number ({min_comp} - {max_comp}): ", min_comp, max_comp) # prompts user for input
        if comp_no in comp_numbers:
            break

    # Validate event number
    events = read_event_file() # loads all events from storage file into a list
    event_numbers = [e['event_no'] for e in events]
    min_event = min(event_numbers) # finds min event number
    max_event = max(event_numbers) # finds max event number

    while True:
        event_no = KD_Val.val_int_message(f"\n\tPlease enter event number ({min_event}-{max_event}): ", min_event, max_event) # prompts user for input
        if event_no in event_numbers:
            break

    # Check if the result exists
    results = read_result_file() # loads all results from storage file into a list
    result = next((r for r in results if r['comp_no'] == comp_no and r['event_no'] == event_no), None)
    if not result:
        print("\n\tSorry - Result not found") # prints error message if result not found
        return # returns to previous operation

    # Confirm deletion
    confirm = input("\tConfirm deletion of this result (y/n): ").lower() # prompts user for input
    if confirm != 'y':
        return # return to previous operation

    # Delete the result
    results = [r for r in results if not (r['comp_no'] == comp_no and r['event_no'] == event_no)]
    write_result_file(results) # saves updated result list to storage file
    print("\n\tResult deleted successfully") # prints success message


# Function to reset competitors to the default list
def reset_comp():
    print("\n\t--- Reset Competitors ---") # prints title
    if KD_Val.val_yes_no("\n\tAre you sure you want to reset all competitors to the default list? (y/n): "): # prompts usr for input
        default_competitors = create_competitors()  # return a list of competitor dictionaries
        write_comp_file(default_competitors)  # saves updated competitor list to storage file
        print("\n\tCompetitors list has been reset to the default list.") # prints success message
    else:
        print("\n\tReset cancelled.") # prints message confirming operation cancellation


# Function to reset events to the default list
def reset_events():
    print("\n\t--- Reset Events ---") # prints title
    if KD_Val.val_yes_no("\n\tAre you sure you want to reset all events to the default list? (y/n): "): # prompts user for input
        default_events = create_events()  # Returns list of event dictionaries
        write_event_file(default_events)  # Saves the updated events list to storage file
        print("\n\tEvents list has been reset to the default list.") # prints success message
    else:
        print("\n\tReset cancelled.") # prints message confirming cancellation


# Function to reset results to a random list
def reset_results():
    print("\n\t--- Reset Results ---") # prints title
    if KD_Val.val_yes_no("\n\tAre you sure you want to reset all results? (y/n): "): # prompts user for input
        competitors = read_comp_file()
        events = read_event_file()
        results = random_results(competitors, events)

        # Write the updated results to the file
        write_result_file(results)
        print("\n\tResults list has been reset.") # print success message
    else:
        print("\n\tReset cancelled.") # print message confirming reset has been cancelled


# Function to register competitor for an event
def reg_comp_event():
    competitors = read_comp_file()
    events = read_event_file()
    results = read_result_file()

    if not competitors:
        print("\n\tNo competitors found. Please add competitors first.") # prints error message if no competitors in system
        return # return to previous operation
    if not events:
        print("\n\tNo events found. Please add events first.") # prints error message if no events in system
        return # return to previous operation

    print("\n\t--- Register Competitor ---") # print title

    # Display all events
    display_events()

    # Select event
    event_numbers = [e['event_no'] for e in events]
    min_event, max_event = min(event_numbers), max(event_numbers) # finds min/max event numbers
    while True:
        event_no = KD_Val.val_int_message(f"\n\tPlease enter event number ({min_event}-{max_event}): ", min_event, max_event) # prompts user for input
        event = next((e for e in events if e['event_no'] == event_no), None)
        if event:
            break
        print(f"\n\tSorry - Event not found.") # prints error message if event not found

    while True:
        # Display all competitors
        display_comp()

        # Select competitor
        comp_numbers = [c['comp_no'] for c in competitors]
        min_comp, max_comp = min(comp_numbers), max(comp_numbers) # finds min/max competitor numbers
        while True:
            comp_no = KD_Val.val_int_message(f"\n\tPlease enter competitor number ({min_comp}-{max_comp}): ", min_comp, # promps user for input
                                             max_comp)
            competitor = next((c for c in competitors if c['comp_no'] == comp_no), None)
            if competitor:
                break
            print(f"\n\tSorry - Competitor not found.") # prints error message if competitor not found

        # Check if already registered
        if any(r['comp_no'] == comp_no and r['event_no'] == event_no for r in results):
            print(
                f"\n\t{competitor['forename']} {competitor['surname']} is already registered for {event['event_name']}.") # prints error message if competitor already registered
        else:
            # Register competitor for event (create a result entry with no times yet)
            new_result = {
                "comp_no": comp_no,
                "event_no": event_no,
                "swim": 0,
                "cycle": 0,
                "run": 0,
                "total": 0
            }
            results.append(new_result)
            write_result_file(results) # saves updated result list to storage file
            print(
                f"\n\t{competitor['forename']} {competitor['surname']} has been successfully registered for {event['event_name']}.") # prints success message

        # Ask if user wants to register another competitor
        if not KD_Val.val_yes_no("\n\tDo you wish to register another competitor? (y/n): "): # prompts user for input
            break

    print("\n\tRegistration complete.") # confirms registration is complete


# Search function to search competitor by either competitor number or name
def search_comp():
    print("\n\t--- Search Competitors ---") # prints title
    print("\t1. Search by Competitor Number")
    print("\t2. Search by Competitor Name")
    choice = KD_Val.val_int_message("\n\tPlease enter choice: ", 1, 2) # prompts user for input

    competitors = read_comp_file() # load all competitors from storage file into a list
    found = False

    if choice == 1:
        comp_no = KD_Val.val_int_message("\n\tPlease enter competitor number: ", 1, 999) # prompt user for input
        for comp in competitors:
            if comp['comp_no'] == comp_no:
                print(f"\n\tCompetitor found:")
                print(f"\t{comp['comp_no']}: {comp['forename']} {comp['surname']} ({comp['gender']}, {comp['age']})")
                found = True
                break
    else:
        name = KD_Val.val_letters("\n\tPLease enter competitor name: ").lower() # prompt user for input
        for comp in competitors:
            if name in f"{comp['forename']} {comp['surname']}".lower():
                print(f"\n\tCompetitor found:")
                print(f"\t{comp['comp_no']}: {comp['forename']} {comp['surname']} ({comp['gender']}, {comp['age']})")
                found = True

    if not found:
        print("\n\tSorry - No competitors found") # print error message if competitor not found


# Function to search for events by either event number or name
def search_event():
    print("\n\t--- Search Event ---") # print title
    print("\t1. Search by Event Number")
    print("\t2. Search by Event Name")
    choice = KD_Val.val_int_message("\n\tPlease enter choice: ", 1, 2) # prompt user for input

    events = read_event_file() # load all events from storage file into a list
    found = False

    if choice == 1:
        event_numbers = [e['event_no'] for e in events]
        min_event = min(event_numbers) # finds min/max event numbers
        max_event = max(event_numbers)

        while not found:
            event_no = KD_Val.val_int_message(f"\n\tPlease enter event number ({min_event}-{max_event}): ", min=min_event, max=max_event) # prompts user for input
            for event in events:
                if event['event_no'] == event_no:
                    print(f"\n\tEvent found:") # prints success message if event found
                    print(f"\t{event['event_no']}: {event['event_name']}")
                    found = True
                    break
            if not found:
                print(f"\n\tSorry - No event found with event number {event_no}.") # prints error message if event not found
                retry = input("\tWould you like to try again? (y/n): ").lower() # prompt user for input
                if retry != 'y':
                    break
    else:
        name = KD_Val.val_event_name("\n\tPlease enter event name: ").lower() # prompts user for input
        for event in events:
            if name in event['event_name'].lower():
                print(f"\t{event['event_no']}: {event['event_name']}")
                found = True

    if not found:
        print("\n\tSorry - No matches found") # prints error message if no matches found


# Function to search results by either competitor or event
def search_results():
    print("\n\t--- Search Results ---") # prints title
    print("\t1. Search by Competitor")
    print("\t2. Search by Event")
    choice = KD_Val.val_int_message("\n\tPlease enter choice: ", 1, 2) # prompt user for input

    # Loads data from storage file into a list
    results = read_result_file()
    competitors = read_comp_file()
    events = read_event_file()
    found = False

    comp_numbers = [c['comp_no'] for c in competitors]
    event_numbers = [e['event_no'] for e in events]
    min_comp, max_comp = min(comp_numbers), max(comp_numbers) # Finds min/max competitor numbers
    min_event, max_event = min(event_numbers), max(event_numbers) # Finds min/max event numbers

    if choice == 1:
        display_comp() # displays all competitors
        while True:
            comp_no = KD_Val.val_int_message(f"\n\tPlease enter competitor number ({min_comp}-{max_comp}): ", min_comp, max_comp) # prompts user for input
            if comp_no in comp_numbers:
                break
            print(f"\n\tSorry - No competitor found with number {comp_no}.") #prints error message if competitor not found

        for result in results:
            if result['comp_no'] == comp_no:
                comp = next((c for c in competitors if c['comp_no'] == comp_no), None)
                event = next((e for e in events if e['event_no'] == result['event_no']), None)
                print(f"\n\tResults for {comp['forename']} {comp['surname']}:")
                print(f"\tEvent: {event['event_name']}")
                print(f"\tSwim: {result['swim']} min")
                print(f"\tCycle: {result['cycle']} min")
                print(f"\tRun: {result['run']} min")
                print(f"\tTotal: {result['total']} min")
                found = True
    else:
        display_events() # displays all events
        while True:
            event_no = KD_Val.val_int_message(f"\n\tPlease enter event number ({min_event}-{max_event}): ", min_event, max_event) # prompts user for input
            if event_no in event_numbers:
                break
            print(f"\n\tSorry - No event found with number {event_no}.") # prints error message if event not found

        event = next((e for e in events if e['event_no'] == event_no), None)
        if event:
            print(f"\n\n\tResults for {event['event_name']}:")
            print("\n\t{:<10} {:<15} {:<15} {:<15} {:<10} {:<8} {:<8} {:<8}".format(
                "Position", "Competitor No", "Forename", "Surname", "Total", "Swim", "Cycle", "Run"))
            print("\t" + "-" * 95)

            event_results = [r for r in results if r['event_no'] == event_no] # Filter results to include only those matching event number
            event_results.sort(key=lambda x: x['total']) # sort filtered results based on total time (ascending order)

            for position, result in enumerate(event_results, 1): # loops through event results with potision starting at 1
                comp = next((c for c in competitors if c['comp_no'] == result['comp_no']), None) # find details matching competitor no in result - returns none if no match found
                print("\t{:<10} {:<15} {:<15} {:<15} {:<10} {:<8} {:<8} {:<8}".format( # prints results
                    position,
                    comp['comp_no'],
                    comp['forename'],
                    comp['surname'],
                    f"{result['total']} min",
                    f"{result['swim']} min",
                    f"{result['cycle']} min",
                    f"{result['run']} min"
                ))
            found = True

    if not found:
        print("\n\tSorry - No results found") # prints error message if results not found


# Function that provides list of registered competitors for a specific event
def reg_comp():
    events = read_event_file() # Loads events from storage file into a list
    if not events:
        print("\n\tSorry - No events found") # prints error message if no events found
        return # returns to previous operation

    event_numbers = [e['event_no'] for e in events]
    min_event, max_event = min(event_numbers), max(event_numbers) # finds min/max event numbers

    display_events()  # Displays all events
    event_no = KD_Val.val_int_message(f"\n\tEnter event number ({min_event}-{max_event}): ", min_event, max_event) # prompts user for input

    # loads data from storage file into a list
    results = read_result_file()
    competitors = read_comp_file()

    event = next((e for e in events if e['event_no'] == event_no), None) # find details matching competitor no in event - returns none if no match found
    if not event:
        print("\n\tSorry - Event not found") # prints error message if event not found
        return # returns to previous operation

    event_results = [r for r in results if r['event_no'] == event_no] # find details matching event no in result - returns none if no match found
    if not event_results:
        print("\n\tNo competitors registered for this event") # print error message if competitor not found
        return # return to previous operation

    print(f"\n\tCompetitors registered for {event['event_name']}:")
    print(f"\n\t{'Comp No':<10} {'Forename':<15} {'Surname':<15} {'Gender':<10} {'Age':<5}")
    print("\t" + "-" * 60)
    for result in event_results:
        comp = next((c for c in competitors if c['comp_no'] == result['comp_no']), None)
        if comp:
            print(f"\t{comp['comp_no']:<10} {comp['forename']:<15} {comp['surname']:<15} {comp['gender']:<10} {comp['age']:<5}")
        else:
            print(f"\t{result['comp_no']:<10} {'Unknown':<15} {'Competitor':<15} {'N/A':<10} {'N/A':<5}")


# Function that provides a list of all events, sorted alphabetically
def event_list_abc():
    events = read_event_file() # loads events from storage file into a list
    if not events:
        print("\n\tSorry - No events found") # prints error message if event not found
        return # returns to previous operation

    print("\n\tEvents (sorted alphabetically):") # prints title
    for event in sorted(events, key=lambda x: x['event_name']): # sorts events in alphabetical order
        print(f"\t{event['event_no']}: {event['event_name']}") # prints events in alphabetical order


# Function that provides detailed event results, sorted by finishing position
def event_result_details():
    display_events() # displays all events

    # Validate event number with min and max range
    events = read_event_file()
    event_numbers = [e['event_no'] for e in events]
    min_event = min(event_numbers)
    max_event = max(event_numbers)

    while True:
        event_no = KD_Val.val_int_message(f"\n\tPlease enter event number ({min_event}-{max_event}): ", min_event, max_event) # prompts user for input
        event = next((e for e in events if e['event_no'] == event_no), None) # find details matching event no in events - returns none if no match found
        if event:
            break # exits loop

    # loads data from storage files into lists
    results = read_result_file()
    competitors = read_comp_file()

    event_results = [r for r in results if r['event_no'] == event_no]
    if not event_results:
        print("\n\tSorry - No results found for this event") # prints error message if results not found
        return # Returns to previous operation

    # Calculates gender statistics
    comp_in_event = [next(c for c in competitors if c['comp_no'] == r['comp_no'])
                     for r in event_results]
    male_count = sum(1 for c in comp_in_event if c['gender'] == 'Male')
    female_count = len(comp_in_event) - male_count

    # prints title and gender statistics
    print(f"\n\tEvent: {event['event_name']}")
    print(f"\tTotal Participants: {len(event_results)}")
    print(f"\tMale: {male_count} ({(male_count / len(comp_in_event)) * 100:.1f}%)")
    print(f"\tFemale: {female_count} ({(female_count / len(comp_in_event)) * 100:.1f}%)")

    # Sort and display results by finishing position
    event_results.sort(key=lambda x: x['total'])
    print("\tPosition  Forename    Surname     Total   Swim    Cycle   Run")
    print("\t-------------------------------------------------------------")
    for pos, result in enumerate(event_results, 1):
        comp = next(c for c in competitors if c['comp_no'] == result['comp_no'])
        print(
            f"\t{pos:<10}{comp['forename']:<12}{comp['surname']:<12}{result['total']:<8}{result['swim']:<8}{result['cycle']:<8}{result['run']:<8}")


# Registration Menu
def reg_menu():
    choice = 0
    while choice != 5:
        print("\n\n\t--- Registration Menu ---") # prints title
        print("\t1. Competitors")
        print("\t2. Events")
        print("\t3. Register Competitor for Event")
        print("\t4. Return to Main Menu")
        print("\t5. Exit Program")
        choice = KD_Val.val_int_message("\n\tPlease enter choice (1-5): ", 1, 5) # prompts user for input

        if choice == 1:
            comp_menu() # call competitor menu
        elif choice == 2:
            event_menu() # call event menu
        elif choice == 3:
            reg_comp_event() # call reg_comp_event function
        elif choice == 4:
            return # return to previous operation
        elif choice == 5:
            print("\n\tThank you - Exiting Program...")  # Prints message when exiting program
            exit() # exits program
        else:
            print("\n\tError: Please enter a value between 1-4.") # Prints error message if user does not input number between 1-4


# Results Menu
def results_menu():
    choice = 0
    while choice != 7:
        print("\n\n\t--- Results Menu ---") # prints title
        print("\t1. Add Result")
        print("\t2. Update Result")
        print("\t3. Delete Result")
        print("\t4. Reset Results")
        print("\t5. Display All Results")
        print("\t6. Return to Main Menu")
        print("\t7. Exit Program")
        choice = KD_Val.val_int_message("\n\tPlease enter choice (1-7): ", 1, 7) # prompts user for input

        if choice == 1:
            add_results() # call add_results function
        elif choice == 2:
            update_result() # call update_results function
        elif choice == 3:
            delete_result() # call delete_results function
        elif choice == 4:
            reset_results() # call reset_results function
        elif choice == 5:
            display_results() # call display_results function
        elif choice == 6:
            main_menu() # call main menu
        elif choice == 7:
            print("\n\tThank you - Exiting Program...")  # Prints message when exiting program
            exit() # Exits the program
        else:
            print("\n\tError: Please enter a value between 1-6.") # Prints error message if user does not input number between 1-6


# Reports Menu
def reports_menu():
    choice = 0
    while choice != 5:
        print("\n\n\t--- Reports Menu ---") # Prints Reports Menu display
        print("\t1. View Registered Competitors for Event")
        print("\t2. View Events by Alphabetical Order")
        print("\t3. View Results by Finishing Position")
        print("\t4. Return to Main Menu")
        print("\t5. Exit Program")

        choice = KD_Val.val_int_message("\n\tEnter choice (1-5): ", 1, 5) # Prompts user for input

        if choice == 1:
            reg_comp() # Redirects to reg_comp function
        elif choice == 2:
            event_list_abc() # Redirects to event_list_abc function
        elif choice == 3:
            event_result_details() # Redirects to event_result_details function
        elif choice == 4:
            return # Returns to Main Menu
        elif choice == 5:
            print("\n\tThank you - Exiting Program...")  # Prints message when exiting program
            exit() # Exits the program
        else:
            print("\n\tError: Please enter choice (1-4).") # Prints error message if user does not input number between 1-4


# Competitor Menu
def comp_menu():
    choice = 0
    while choice != 7:
        print("\n\n\t--- Competitor Menu ---") # Prints Competitor Menu display
        print("\t1. Add Competitor")
        print("\t2. Update Competitor")
        print("\t3. Delete Competitor")
        print("\t4. Reset Competitors")
        print("\t5. Display All Competitors")
        print("\t6. Return to Main Menu")
        print("\t7. Exit Program")
        choice = KD_Val.val_int_message("\n\tPlease enter choice (1-7): ", 1, 7) # promps user for input

        if choice == 1:
            add_comp() # calls add_comp function
        elif choice == 2:
            update_comp() # calls update_comp function
        elif choice == 3:
            delete_comp() # calls delete_comp function
        elif choice == 4:
            reset_comp() # calls reset_comp function
        elif choice == 5:
            display_comp() # calls display_comp function
        elif choice == 6:
            main_menu() # calls Main Menu
        elif choice == 7:
            print("\n\tThank you - Exiting Program...")  # Prints message when exiting program
            exit() # exits program
        else:
            print("\n\tError: Please enter choice (1-7).") # Prints error message if user does not input number between 1-7


# Events Menu
def event_menu():
    choice = 0
    while choice != 7:
        print("\n\n\t--- Event Menu ---") # prints event menu display
        print("\t1. Add Event")
        print("\t2. Update Event")
        print("\t3. Delete Event")
        print("\t4. Reset Events")
        print("\t5. Display All Events")
        print("\t6. Return to Main Menu")
        print("\t7. Exit Program")
        choice = KD_Val.val_int_message("\n\tPlease enter choice (1-7): ", 1, 7) # prompts user for input

        if choice == 1:
            add_event() # calls add_event function
        elif choice == 2:
            update_event() # calls update_event function
        elif choice == 3:
            delete_event() # calls delete_event function
        elif choice == 4:
            reset_events() # calls reset_events function
        elif choice == 5:
            display_events() # calls display_events function
        elif choice == 6:
            main_menu() # calls Main menu
        elif choice == 7:
            print("\n\tThank you - Exiting Program...")  # Prints message when exiting program
            exit() # exits program
        else:
            print("\n\tError: Please enter choice (1-7).") # Prints error message if user does not input number between 1-7


# Search Menu
def search_menu():
    choice = 0
    while choice != 5:
        print("\n\n\t--- Search Menu ---") # prints search menu display
        print("\t1. Search Competitors")
        print("\t2. Search Events")
        print("\t3. Search Results")
        print("\t4. Return to Main Menu")
        print("\t5. Exit Program")

        choice = KD_Val.val_int_message("\n\tEnter choice (1-5): ", 1, 5) # prompts user for input

        if choice == 1:
            search_comp() # calls search_comp function
        elif choice == 2:
            search_event() # calls search_event function
        elif choice == 3:
            search_results() # calls search_results function
        elif choice == 4:
            return # returns to main menu
        elif choice == 5:
            print("\n\tThank you - Exiting Program...")  # Prints message when exiting program
            exit() # Exits the program
        else:
            print("\n\tError: Please enter choice (1-4).") # Prints error message if user does not input number between 1-4


# Main Menu
def main_menu():
    choice = 0
    while choice != 5:
        print("\n\n\t--- Main Menu ---") # prints main menu display
        print("\t1. Registration")
        print("\t2. Record Results")
        print("\t3. Generate Reports")
        print("\t4. Search")
        print("\t5. Exit Program")

        choice = KD_Val.val_int_message("\n\tPlease enter choice (1-5): ", 1, 5) # prompts user for input

        if choice == 1:
            reg_menu() # redirects to registration menu
        elif choice == 2:
            results_menu() # redirects to results menu
        elif choice == 3:
            reports_menu() # redirects to reports menu
        elif choice == 4:
            search_menu() # redirects to search menu
        elif choice == 5:
            print("\n\tThank you - Exiting Program...") # Displays message when exiting program
            exit() # Exits the program
        else:
            print("\n\tError: Please enter choice (1-5).") # Prints error message if user does not input number between 1-5


if __name__ == "__main__":
    # Create files if they do not exist
    if not os.path.exists(comp_file):
        competitors = create_competitors()
        write_comp_file(competitors)

    if not os.path.exists(event_file):
        events = create_events()
        write_event_file(events)

    if not os.path.exists(result_file):
        competitors = read_comp_file()
        events = read_event_file()
        results = random_results(competitors, events)
        write_result_file(results)


    # Prints welcome message when program is run
    print("\n\n------------------------------\n\tT R I - T R A C K E R\n         S Y S T E M\n------------------------------")

    # Calls main menu immediately when program is run
    main_menu()