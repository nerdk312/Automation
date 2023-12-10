import datetime

def save_workout(workout_data):
    today = datetime.date.today()
    filename = f"workout_{today}.txt"
    
    with open(filename, "a") as file:
        file.write(workout_data + "\n")
    
    print("Workout saved successfully!")

def update_workout():
    today = datetime.date.today()
    filename = f"workout_{today}.txt"

    try:
        with open(filename, "r") as file:
            workout_lines = file.readlines()
        
        if not workout_lines:
            print("No workout data found for today.")
            return
        
        updated_workout = ""
        
        for line in workout_lines:
            exercise, weight, reps = line.strip().split(",")
            
            new_weight = input(f"Enter new weight for {exercise}: ")
            new_reps = input(f"Enter new reps for {exercise}: ")
            
            updated_line = f"{exercise},{new_weight},{new_reps}\n"
            updated_workout += updated_line
        
        with open(filename, "w") as file:
            file.write(updated_workout)
        
        print("Workout updated successfully!")
    
    except FileNotFoundError:
        print("No workout data found for today.")

# Example usage:
exercise_list = ["Bench Press", "Squats", "Deadlifts"]

workout_data = ""
for exercise in exercise_list:
    weight = input(f"Enter weight for {exercise}: ")
    reps = input(f"Enter reps for {exercise}: ")
    workout_data += f"{exercise},{weight},{reps}\n"

save_workout(workout_data)
update_workout()




''' Version 2 with max values'''
import datetime

def save_workout(workout_data):
    today = datetime.date.today()
    filename = f"workout_{today}.txt"
    
    with open(filename, "a") as file:
        file.write(workout_data + "\n")
    
    print("Workout saved successfully!")

def update_workout():
    today = datetime.date.today()
    filename = f"workout_{today}.txt"

    try:
        with open(filename, "r") as file:
            workout_lines = file.readlines()
        
        if not workout_lines:
            print("No workout data found for today.")
            return
        
        updated_workout = ""
        
        for line in workout_lines:
            exercise, weight, reps = line.strip().split(",")
            
            max_weight, max_reps = get_max_values(exercise)  # Retrieve max values from text file
            
            new_weight = input(f"Enter new weight for {exercise} (Max: {max_weight}): ")
            new_reps = input(f"Enter new reps for {exercise} (Max: {max_reps}): ")
            
            updated_line = f"{exercise},{new_weight},{new_reps}\n"
            updated_workout += updated_line
        
        with open(filename, "w") as file:
            file.write(updated_workout)
        
        print("Workout updated successfully!")
    
    except FileNotFoundError:
        print("No workout data found for today.")

def get_max_values(exercise):
    max_weight = 0
    max_reps = 0
    
    with open("max_values.txt", "r") as file:  # Assuming max values are stored in a file named "max_values.txt"
        for line in file:
            data = line.strip().split(",")
            if data[0] == exercise:
                max_weight = float(data[1])
                max_reps = int(data[2])
                break
    
    return max_weight, max_reps

# Example usage:
exercise_list = ["Bench Press", "Squats", "Deadlifts"]

workout_data = ""
for exercise in exercise_list:
    max_weight, max_reps = get_max_values(exercise)  # Retrieve max values from text file
    
    weight = input(f"Enter weight for {exercise} (Max: {max_weight}): ")
    reps = input(f"Enter reps for {exercise} (Max: {max_reps}): ")
    workout_data += f"{exercise},{weight},{reps}\n"

save_workout(workout_data)
update_workout()




''' Version 3 going in reverse order to get max values '''
import datetime

def save_workout(workout_data):
    today = datetime.date.today()
    filename = f"workout_{today}.txt"
    
    with open(filename, "a") as file:
        file.write(workout_data + "\n")
    
    print("Workout saved successfully!")

def update_workout():
    today = datetime.date.today()
    filename = f"workout_{today}.txt"

    try:
        with open(filename, "r") as file:
            workout_lines = file.readlines()
        
        if not workout_lines:
            print("No workout data found for today.")
            return
        
        updated_workout = ""
        
        for line in workout_lines:
            exercise, weight, reps = line.strip().split(",")
            
            max_weight, max_reps = get_max_values(exercise)  # Retrieve max values from text file
            
            new_weight = input(f"Enter new weight for {exercise} (Max: {max_weight}): ")
            new_reps = input(f"Enter new reps for {exercise} (Max: {max_reps}): ")
            
            updated_line = f"{exercise},{new_weight},{new_reps}\n"
            updated_workout += updated_line
        
        with open(filename, "w") as file:
            file.write(updated_workout)
        
        print("Workout updated successfully!")
    
    except FileNotFoundError:
        print("No workout data found for today.")

def get_max_values(exercise):
    max_weight = 0
    max_reps = 0
    
    with open("workout_history.txt", "r") as file:  # Assuming workout history is stored in a file named "workout_history.txt"
        workout_data = file.readlines()
        workout_data.reverse()  # Reverse the order to find the most recent data first
        
        for line in workout_data:
            data = line.strip().split(",")
            if data[0] == exercise:
                max_weight = float(data[1])
                max_reps = int(data[2])
                break
    
    return max_weight, max_reps

# Example usage:
exercise_list = ["Bench Press", "Squats", "Deadlifts"]

workout_data = ""
for exercise in exercise_list:
    max_weight, max_reps = get_max_values(exercise)  # Retrieve max values from workout history
    
    weight = input(f"Enter weight for {exercise} (Max: {max_weight}): ")
    reps = input(f"Enter reps for {exercise} (Max: {max_reps}): ")
    workout_data += f"{exercise},{weight},{reps}\n"

save_workout(workout_data)
update_workout()





# Tasks

# Make a file to contain all the different data
# Save a data for each workout day
# Each entry should be an exercise, weight x reps (as well as comment)
#
# Forecast function 
# Go through the data in reverse
# Find the max value in a day
# Use that value as a guide to start next days workout (based on the particular exercise)

