import re
#import ipdb
import datetime
import seaborn as sns
import matplotlib.pyplot
import numpy as np

def fill_exercise_day_info(exercise_day,recent_exercises):
    for exercise in exercise_day:
        # Define the target string and the regex pattern
        target_string = exercise.lower()
        # Make it so that the () are not taken into account as metacharacers from regex
        target_string = re.escape(target_string)
        pattern = re.compile(f'{target_string}.*?(?=\n|$)', re.DOTALL | re.MULTILINE)
        # Version of code which enabels to 2 mismatches to occur - Based on chatGPT

        # Generate a regex pattern with optional character classes for mismatches


        pattern = re.compile(f'{target_string}.*?(?=\n|$)', re.DOTALL | re.MULTILINE)

        # Find all matches using the regex pattern
        matches = pattern.findall(content)
        if len(matches) ==0:
            print(f'{exercise} not found')
        else:
            last_occurence = matches[-1]
            recent_exercises.append(last_occurence)

    result = "\n".join(recent_exercises)
    result+="\n\n"
    return result

#print(exercises['Monday'])

# Week 1 and Week 5 are related
# Week 2 and 3 are related

weekly_exercises = {'Week 1':{'Monday':['Front Sled','Tricep Pushdown','Barbell Back Squat(s)','Standing Dumbbell Press(s)','Two Leg Nordic Hamstring Curl','Two Leg Tibialis Raise(s)', 'Max Two Arm Hang'],

                            'Tuesday':['Side Sled','Tricep Overhead','Peterson Step Up','Iso Barbell Front squat','Iso Behind The Neck Press','Iso Barbell Bench Press','Iso Barbell Romanian Deadlift', 'Iso Barbell Wrist Flexion','Iso Barbell Wrist Curl','Iso Two Leg Dumbbell Tibialis Raise', 'One arm Hang','Standing Broad Jump'],

                            'Wednesday':['Front Sled','Tricep Pushdown','Dumbbell ATG Split Squat(s)','Cable Pancake(s)','Medium Two Arm Hang','Standing Single Leg Box Jump'],

                            'Thursday':['Front Sled','Tricep Pushdown','One Leg Lying Hamstring Curl', 'Dips(s)','Neck Upwards','Neck Downwards','Heavy Two Arm Hang', 'Max Speed Side Sprinting'],

                            'Friday':['Side Sled','Tricep Overhead','Peterson Iso Step Up','Iso Reverse Squat','Iso Dumbbell Pullover','Iso Front Barbell ATG Split Squat','Iso Weighted Butterflys','Iso External Dumbbell Rotation','One Arm Hang','Two Leg Depth Drop'],

                            'Saturday':['Front Sled','Tricep Pushdown','Incline Dumbbell Curl(s)','Farmer Walk(Single)','Lateral Dumbbell Raise(s)','Face Pulls(s)','Light Two Arm Hang','Max Incline Backward Sprinting'],

                            'Sunday':['Tricep Overhead','Two Leg Iso Seated Hamstring Curl','Iso Front Barbell Cossack Squat','Iso One Legged Leg Extension','Iso Barbell Back Row', 'Iso French Press','Iso Hip External and Internal Rotation',
                                       'Iso Two Legged Hip Thrust','Iso Barbell Curl','Iso Landmine Rotation','Iso Trap 3 Raise','Iso Dumbbell Fly']
                            },

                    'Week 2':{'Monday':['Front Sled','Tricep Pushdown','Barbell Front Squat(s)','Barbell Push Press(p)','Dumbbell Bench Press(s)','Dumbbell Wrist Flexion(s)','Dumbbell Wrist Curl(s)', 'Max Two Arm Hang','Two Legged Box Jump'],

                            'Tuesday':['Side Sled','Tricep Overhead','Peterson Step Up','Single Leg Nordic Hamstring Curl','Iso Hack Squat','Iso Barbell Military Press','Iso Incline Dumbbell Press','Iso Dumbbell Sumo Deadlift', 'Iso Banded neck rotiation','Iso Single Leg Seated Calf Raise', 'One Arm Hang','Max Approach Jumping'],

                            'Wednesday':['Front Sled','Tricep Pushdown','One Leg Reverse Squat(s)','Pull Ups(s)','ATG Dumbbell External Rotation(s)','Medium Two Arm Hang','Bounding'],

                            'Thursday':['Front Sled','Tricep Pushdown','Seated Good Morning(s)','Cable Hip Adduction(s)','Cable Hip Abduction(s)','Neck Upwards','Neck Downwards','Heavy Two Arm Hang', 'Max Incline Backwards Sprinting'],

                            'Friday':['Side Sled','Tricep Overhead','Peterson Iso Step Up','Two Leg Iso Lying Hamstring Curl','Iso Hanging Leg Raise','Iso One Arm Dumbbell Row','Iso Back Barbell ATG Split Squat','Iso Weighted Pidgeon','Iso Powel Raise','One Arm Hang','Single Lateral Jump'],

                            'Saturday':['Front Sled','Tricep Pushdown','One Leg Hip Thrust(s)','Incline Dumbbell Hammer Curl(s)','Farmer Walk(Double)','QL extension(s)','Frontal Raise(s)','Light Two Arm Hang','Max Incline Side Sprinting'],

                            'Sunday':['Tricep Overhead','One Leg Iso Seated Hamstring Curl','Iso Back Barbell Cossack Squat','Iso One Legged Leg Press','Iso Dumbbell Jefferson Curl', 'Machine Iso Chest Press','Iso Hip Adductor Machine','Iso Hip Abduction Machine','Iso Dumbbell Ulnar Deviation','Iso Dumbbell Radial Deviation',
                                      'Iso Back Extension One Leg','Iso Barbell Preacher Curl','Iso Ab Machine','Iso Trapbar Shrug','Iso Row Machine']
                            },

                        'Week 3':{'Monday':['Front Sled','Tricep Pushdown','Power Clean(p)','Barbell Military Press(s)','Two Leg Seated Hamstring Curl','Single Leg Seated Calf Raise(s)', 'Max Two Arm Hang','Sitting Box Jump'],

                            'Tuesday':['Side Sled','Tricep Overhead','Peterson Step Up','Two Leg Iso Nordic Hamstring Curl','Iso Reverse Nordic','Iso Incline Barbell Press','Iso Barbell Deadlift', 'Iso Banded Neck Sides','Iso Single Leg Standing Calf Raise', 'One Arm Hang','Max Incline Backwards Sprinting'],

                            'Wednesday':['Front Sled','Tricep Pushdown','One Arm Dumbbell Row(s)','Back Barbell ATG Split Squat(s)','Weighted Pidgeon(s)','Medium Two Arm Hang','Sitting Single Leg Box Jump'],

                            'Thursday':['Front Sled','Tricep Pushdown','Back Barbell Cossack Squat(s)','One Legged Leg Press(s)', 'Machine Chest Press(s)','Dumbbell Ulnar Deviation(s)','Dumbbell Radial Deviation(s)','Heavy Two Arm Hang','Running Broad Jump'],

                            'Friday':['Side Sled','Tricep Overhead','Peterson Iso Step Up','One Leg Iso Lying Hamstring Curl','Iso Single Leg Monkey Foot','Iso Lat Pull Down Machine','Iso Pistol Squat','Iso 90-90 Hip Push Press','Iso Cable External Rotation','One Arm Hang','Single Leg Depth Drop', 'Max Incline Side Sprinting'],

                            'Saturday':['Front Sled','Tricep Pushdown','Reverse Curl(s)','Barbell Preacher Curl(s)','Overhead Walk(Single)','Ab Machine(s)','Row Machine(s)', 'Light Two Arm Hang'],

                            'Sunday':['Tricep Overhead','Iso Reverse Curl','Iso Wrist Rotation','Iso Barbell Jefferson Curl','Iso Two Legged Leg Press', 'Iso Tricep Extension','Iso Back Extension','Iso Chin Ups','Iso Dragon Flag','Iso Trapbar Shrug','Iso Rear Delt Fly']
                            },

                        'Week 4':{'Monday':['Front Sled','Tricep Pushdown','Hack Squat(s)','Barbell Split Jerk(p)','Incline Dumbbell Press(s)', 'Two Leg Dumbbell Tibialis Raise(s)','Banded Neck Rotation(s)', 'Max Two Arm Hang','Two Leg Depth Jump'],

                            'Tuesday':['Side Sled','Tricep Overhead','Peterson Step Up','One Leg Iso Nordic Hamstring Curl','Iso Barbell Front Squat','Iso Behind The Neck Press','Iso Barbell Bench Press','Iso Barbell Romanian Deadlift', 'Iso Barbell Wrist Flexion','Iso Barbell Wrist Curl','Iso Two Leg Dumbbell Tibialis Raise', 'One arm Hang','Max Speed Side Sprinting'],

                            'Wednesday':['Front Sled','Tricep Pushdown','Hanging Leg Raise(s)','Powel Raise(s)','Two Leg Lying Hamstring Curl','Medium Two Arm Hang','Single Leg Depth Jump'],

                            'Thursday':['Front Sled','Tricep Pushdown','Barbell Jefferson Curl(s)','Two legged Leg extension(s)','Hip Adductor Machine(s)','Hip Abduction Machine(s)','Heavy Two Arm Hang', 'Max Incline Backwards Sprinting'],

                            'Friday':['Side Sled','Tricep Overhead','Iso Peterson Step Up','Iso Reverse Squat','Iso Dumbbell Pullover','Iso Front Barbell ATG Split Squat','Iso Weighted Butterflys','Iso External Dumbbell Rotation','One Arm Hang','PJF Lateral Hop'],

                            'Saturday':['Front Sled','Tricep Pushdown','Back Extension One Leg(s)','Overhead Walk(Double)','Front Barbell Shrug(s)','Back Barbell Shrug(s)','Light Two Arm Hang','Alternate Bounding'],

                            'Sunday':['Tricep Overhead','One Leg Seated Hamstring Curl','Iso Back Barbell Cossack Squat','Iso One Legged Leg Extension','Iso Dumbbell Jefferson Curl', 'Machine Iso Chest Press','Iso Hip Adductor Machine','Iso Hip Abduction Machine','Iso Dumbbell Ulnar Deviation','Iso Dumbbell Radial Deviation',
                                      'Iso Back Extension One Leg','Iso Barbell Preacher Curl','Iso Ab Machine','Iso Trapbar Shrug','Iso Row Machine']
                            },


                        'Week 5':{'Monday':['Front Sled','Tricep Pushdown','Barbell Back Squat(s)','Behind The Neck Press(s)','Barbell Romanian Deadlift(s)','Two Leg Standing Calf Raise(s)', 'Max Two Arm Hang','Standing Broad Jump'],

                            'Tuesday':['Side Sled','Tricep Overhead','Peterson Step Up','Two Leg Nordic Hamstring Curl','Iso Barbell Back Squat','Iso Dumbbell Press','Iso Dumbbell Bench Press','Iso Dumbbell Romanian Deadlift','Iso Dumbbell Wrist Flexion','Iso Dumbbell Wrist Curl','Iso One Leg Tibialis Raise', 'One Arm Hang'],

                            'Wednesday':['Front Sled','Tricep Pushdown','Front Barbell ATG Split Squat(s)','Weighted Butterflys(s)','Medium Two Arm Hang','Standing Single Leg Box Jump'],

                            'Thursday':['Front Sled','Tricep Pushdown','Front Barbell Cossack Squat(s)','Penlay Row(p)', 'French Press(s)','Barbell Shoulder Rotation(s)','Heavy Two Arm Hang','Max Speed Side Sprinting'],

                            'Friday':['Side Sled','Tricep Overhead','Peterson Step Up','One Leg Lying Hamstring Curl','Iso One Leg Reverse Squat','Iso Pull Ups','Iso Dumbbell ATG Split Squat','Iso Cable Pancake','Iso ATG Dumbbell External Rotation','One Arm Hang','Two Leg Depth Drop'],

                            'Saturday':['Front Sled','Tricep Pushdown','Barbell Curl(s)','Side Farmer Walk(Single)','Landmine Rotation(s)','Dumbbell Fly(s)','Light Two Arm Hang','Max Incline Backward Sprinting'],

                            'Sunday':['Tricep Overhead','Two Leg Iso Seated Hamstring Curl','Iso Dumbbell Cossack Squat','Iso Two legged Leg extension','Iso Seated Good Morning', 'Iso Dips','Iso Cable Hip Adduction','Iso Cable Hip Abduction','Iso Neck Upwards','Iso Neck Downwards',
                                      'Iso One Leg Hip Thrust','Iso Incline Dumbbell Curl','Iso QL extension','Iso Lateral Dumbbell Raise','Iso Face Pulls'],
                            },


                        'Week 6':{'Monday':['Front Sled','Tricep Pushdown','Barbell Front Squat(s)','Behind The Neck Push Press(p)','Barbell Bench Press(s)', 'Barbell Wrist Flexion(s)','Barbell Wrist Curl(s)', 'Max Two Arm Hang','Two Legged Box Jump'],

                            'Tuesday':['Side Sled','Tricep Overhead','Peterson Step Up','One Leg Nordic Hamstring Curl','Iso Reverse Nordic','Iso Incline Barbell Press','Iso Barbell Deadlift', 'Iso Banded Neck Sides','Iso Single Leg Standing Calf Raise', 'One Arm Hang','Max Approach Jumping'],

                            'Wednesday':['Front Sled','Tricep Pushdown','Two Legged Reverse Squat(s)','Dumbbell Pullover(s)','External Dumbbell Rotation(s)','One Leg Nordic Hamstring Curl','Medium Two Arm Hang','Bounding'],

                            'Thursday':['Front Sled','Tricep Pushdown','Two Legged Leg Press(s)','Barbell Back Row(s)' ,'Hip External and Internal Rotation(s)','Barbell Shoulder Rotation(s)','Heavy Two Arm Hang','Max Incline Backwards Sprinting'],

                            'Friday':['Side Sled','Tricep Overhead','Peterson Iso Step Up','Two Leg Iso Lying Hamstring Curl','Iso Single Leg Monkey Foot','Iso Lat Pull Down Machine','Iso Pistol Squat','Iso 90-90 Hip Push Press','Iso Cable External Rotation','One Arm Hang','Single Lateral Jump'],

                            'Saturday':['Front Sled','Tricep Pushdown','Two Legged Hip Thrust(s)','Cable Hammer Curl(s)','Side Farmer Walk(Double)','Trap 3 Raise(s)','Light Two Arm Hang','Depth Drop','Max Incline Side Sprinting'],

                            'Sunday':['Tricep Overhead','Iso Two Legged Leg Press','Iso Reverse Curl','Iso Wrist Rotation','One Leg Iso Seated Hamstring Curl','Iso Barbell Jefferson Curl', 'Iso Tricep Extension','Iso Back Extension','Iso Chin Ups','Iso Dragon Flag','Iso Trapbar Shrug','Iso Rear Delt Fly']
                            },



                        'Week 7':{'Monday':['Front Sled','Tricep Pushdown','Squat Clean(p)','Barbell Deficit Deadlift(s)', 'Banded Neck Sides(p)','Single Leg Standing Calf Raise(s)', 'Max Two Arm Hang','Sitting Box Jump'],

                            'Tuesday':['Side Sled','Tricep Overhead','Iso Hack Squat','Two Leg Iso Nordic Hamstring Curl','Iso Barbell Military Press','Iso Incline Dumbbell Press','Iso Dumbbell Sumo Deadlift', 'Iso Banded neck rotiation','Iso Single Leg Seated Calf Raise', 'One Arm Hang','Max Incline Backwards Sprinting'],

                            'Wednesday':['Front Sled','Tricep Pushdown','Pistol Squat(s)','90-90 Hip Push Press(s)','Two Leg Seated Hamstring Curl','Medium Two Arm Hang','Sitting Single Leg Box Jump'],

                            'Thursday':['Front Sled','Tricep Pushdown', 'Back Barbell Cossack Squat(s)','Tricep Extension(s)','Wrist Rotation(s)','Heavy Two Arm Hang','Max Incline Side Sprinting'],

                            'Friday':['Side Sled','Tricep Overhead','Peterson Iso Step Up','One Leg Iso Lying Hamstring Curl','Iso Hanging Leg Raise','Iso One Arm Dumbbell Row','Iso Back Barbell ATG Split Squat','Iso Weighted Pidgeon','Iso Powel Raise','One Arm Hang','Single Leg Depth Drop'],

                            'Saturday':['Front Sled','Tricep Pushdown','Chin Ups(s)','Side Overhead Walk(Single)','Rear Delt Fly(s)','Light Two Arm Hang'],

                            'Sunday':['Tricep Overhead','Iso Back Barbell Cossack Squat','Iso One Legged Leg Press','Iso Dumbbell Jefferson Curl', 'Machine Iso Chest Press','Iso Hip Adductor Machine','Iso Hip Abduction Machine','Iso Dumbbell Ulnar Deviation','Iso Dumbbell Radial Deviation',
                                      'Iso Back Extension One Leg','Iso Barbell Preacher Curl','Iso Ab Machine','Iso Trapbar Shrug','Iso Row Machine']
                            },

                        'Week 8':{'Monday':['Front Sled','Tricep Pushdown','Landmine Split Jerk(p)','Incline Barbell Press(s)','Barbell Deadlift(s)', 'Banded Neck Sides(s)', 'Max Two Arm Hang','Depth Jump'],

                            'Tuesday':['Side Sled','Tricep Overhead','Peterson Step Up','One Leg Iso Nordic Hamstring Curl','Iso Barbell Back Squat','Iso Barbell Military Press','Iso Dumbbell Bench Press','Iso Dumbbell Romanian Deadlift','Iso Dumbbell Wrist Flexion','Iso Dumbbell Wrist Curl','Iso One Leg Tibialis Raise', 'One Arm Hang','Max Speed Side Sprinting'],

                            'Wednesday':['Front Sled','Tricep Pushdown','Single Leg Monkey Foot(s)','Lat Pull Down Machine(s)','Cable External Rotation(s)','One Leg Seated Hamstring Curl','Medium Two Arm Hang','Single Leg Depth Jump'],

                            'Thursday':['Front Sled','Tricep Pushdown','Barbell Jefferson Curl(s)','One Legged Leg Extension(s)', 'Muscle Up(p)','Two Leg Lying Hamstring Curl','Heavy Two Arm Hang','Max Incline Backwards Sprinting'],

                            'Friday':['Side Sled','Tricep Overhead','Peterson Iso Step Up','Iso One Leg Reverse Squat','Iso Pull Ups','Iso Dumbbell ATG Split Squat','Iso Cable Pancake','Iso ATG Dumbbell External Rotation','One Arm Hang','PJF Lateral Hop'],

                            'Saturday':['Front Sled','Tricep Pushdown','Back Extension Two Leg(s)','Side Overhead Walk(Double)','Trapbar Shrug(s)','Light Two Arm Hang','Max Approach Jumping'],

                            'Sunday':['Tricep Overhead','Iso Dumbbell Cossack Squat','Iso Two legged Leg Extension','Iso Seated Good Morning', 'Iso Dips','Iso Cable Hip Adduction','Iso Cable Hip Abduction','Iso Neck Upwards','Iso Neck Downwards',
                                      'Iso One Leg Hip Thrust','Iso Incline Dumbbell Hammer Curl','Iso QL extension','Iso Frontal Raise','Iso Face Pulls'],

                            },
                            # Deload week
                         'Week Deload1':{'Monday':['Front Sled','Tricep Pushdown','Reverse Nordic(s)','Seated Dumbbell Press(s)','Cable Chest Fly(s)', 'Max Two Arm Hang'],

                            'Tuesday':['Side Sled','Tricep Overhead','Iso Hack Squat','Iso Cable Rear Flys','One Arm Hang'],

                            'Wednesday':['Front Sled','Tricep Pushdown','Cable Lateral Raise(s)','Landmine Split Squat(s)','Medium Two Arm Hang'],

                            'Thursday':['Front Sled','Tricep Pushdown','Standing Good Morning(s)','Front Barbell Horsestance Squat(s)','Heavy Two Arm Hang'],

                            'Friday':['Side Sled','Tricep Overhead','Iso Bulgarian Split Squat(s)','Iso Cable Frontal Raise','One Arm Hang'],

                            'Saturday':['Front Sled','Tricep Pushdown','Cable Reverse Curl(s)','Cable Frontal Raise(s)','Two Legged Nordic Hamstring Curl(s)','Light Two Arm Hang'],

                            'Sunday':['Side Sled','Tricep Overhead','Iso Cable Row','Iso Back Barbell Horsestance Squat','Iso Cable Bicep Curl','Iso Two Legged Back Extension'],

                            },
                        # Deload week
                        'Week Deload2':{'Monday':['Front Sled','Tricep Pushdown','Hack Squat(s)','Cable Rear Fly(s)' 'Max Two Arm Hang','Max Two Arm Hang'],

                            'Tuesday':['Side Sled','Tricep Overhead','Iso Reverse Nordic','Iso Seated Dumbbell Press','Iso Cable Chest Fly','One Arm Hang'],

                            'Wednesday':['Front Sled','Tricep Pushdown','Cable Frontal Raise(s)','Bulgarian Split Squat(s)'],

                            'Thursday':['Front Sled','Tricep Pushdown','Cable Row(s)','Back Barbell Horsestance Squat(s)','Heavy Two Arm Hang','Max Incline Backwards Sprinting'],

                            'Friday':['Side Sled','Tricep Overhead','Iso Cable Lateral Raise','Iso Landmine Split Squat(s)'],

                            'Saturday':['Front Sled','Tricep Pushdown','Cable Bicep Curl(s)','Two Legged Back Extension(s)','Light Two Arm Hang'],
                            'Sunday':['Iso Standing Good Morning','Iso Front Barbell Horsestance Squat(s)','Iso Cable Reverse Curl(s)','Iso Cable Frontal Raise','Two Leg Iso Nordic Hamstring Curl'],

                            },

                             }



print(weekly_exercises)


# Open the file in read mode
with open('workout_log.txt', 'r') as file:
    content = file.read()  # This reads the entire content of the file

#print(content)
content = content.lower() # Remove capitalization

day = 'Sunday'
week = 'Week 1'
start_date = '2024-02-17'
weekly=True
'''
start_date = datetime.date.fromisoformat('2019-12-04')
todays_date = datetime.date.today()
datetime.date.timedelta(days=specific_day)
Desired_Date_Formatted = todays_date.strftime ('%d%m%Y') # format the date to ddmmyyyy
'''
if weekly:
    week_results = []
    days = weekly_exercises[week]
    for index,day in enumerate(days.keys()):

        specific_date = datetime.date.fromisoformat(start_date)+datetime.timedelta(days=index)
        Desired_Date_Formatted = specific_date.strftime ('%d-%m-%Y')
        #print(Desired_Date_Formatted)
        first_entry = "-".join([week,day,Desired_Date_Formatted])
        recent_exercises = [first_entry]

        exercise_day = days[day]
        day_result = fill_exercise_day_info(exercise_day,recent_exercises)
        week_results.append(day_result)
    final_week_result = "\n".join(week_results)
    print(final_week_result)
else:
    specific_date = datetime.date.fromisoformat(start_date)
    Desired_Date_Formatted = specific_date.strftime ('%d-%m-%Y')
    first_entry = "-".join([week,day,Desired_Date_Formatted])
    exercise_day = weekly_exercises[week][day]
    recent_exercises = [first_entry]
    day_result = fill_exercise_day_info(exercise_day,recent_exercises)
    print(day_result)

'''
for exercise in exercise_day:
# Define the target string and the regex pattern
    target_string = exercise.lower()
    # Make it so that the () are not taken into account as metacharacers from regex
    target_string = re.escape(target_string)
    pattern = re.compile(f'{target_string}.*?(?=\n|$)', re.DOTALL | re.MULTILINE)
    # Version of code which enabels to 2 mismatches to occur - Based on chatGPT

    # Generate a regex pattern with optional character classes for mismatches


    pattern = re.compile(f'{target_string}.*?(?=\n|$)', re.DOTALL | re.MULTILINE)

    # Find all matches using the regex pattern
    matches = pattern.findall(content)
    if len(matches) ==0:
        print(f'{exercise} not found')
    else:
        last_occurence = matches[-1]
        recent_exercises.append(last_occurence)

#print(recent_exercises)


# Using join to concatenate the strings with newline character
result = "\n".join(recent_exercises)

# Printing the result
print(result)
'''


'''
Microdosing
- L-sit
- One leg/ Two legs Hyperarch hop
- Two/One leg Tibialis raise
- Finger Pushup
- Ankle inversions
- One arm pushups
- Pistol Squat

Stretching
- Couch Stretch
- Standing pancake
- Elephant walk 
- Butterfly stretch
- Side splits
- Middle splits
- Tricep stretch


Monday
Breakfast Side splits, One leg HH
Lunch Elephant walk One arm pushups
Dinner Overheads Tricep stretch, One leg Tibialis

Tuesday
Breakfast Butterfly stretch, Two leg HH
Lunch Standing pancake Finger Pushup
Dinner Chest Tricep stretch, Two leg Tibialis

Wednesday
Breakfast Middle splits, Pistol Squat
Lunch Couch Stretch, L-sit
Dinner Side Tricep stretch, Ankle inversions

Thursday
Breakfast Side splits, One leg HH
Lunch Elephant walk, One arm pushups
Dinner Overheads Tricep stretch, One leg Tibialis

Friday
Breakfast Butterfly stretch, Two leg HH
Lunch Standing pancake, Finger Pushup
Dinner Chest Tricep stretch, Two leg Tibialis

Saturday
Breakfast Middle splits, Pistol Squat
Lunch Couch Stretch, L-sit
Dinner Side Tricep stretch, Ankle inversions

'''

'''
import pickle

# Opening and loading a Pickle file
with open('my_dict.pkl', 'rb') as f:
    loaded_dict = pickle.load(f)

print(loaded_dict)
'''