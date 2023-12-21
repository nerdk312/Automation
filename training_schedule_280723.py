import re

exercises = {'Monday':['Jump Barbell Back Squat(p)','Barbell Back Squat(s)',
                       'Dumbell jump squat(p)','Barbell Forward Sqiat(s)'
                       'Power Cleam(p)', 'Barbell Hack Squat(s)',
                       'Squat Clean(p)','Reverse Nordic(s)'
                       ]}
#print(exercises['Monday'])



weekly_exercises = {'Week 1':{'Monday':['Jump Barbell Back Squat(p)','Standing Dumbbell Press(s)','Dumbbell Bench Press(p)','Dumbbell Romanian Deadlift(s)','Dumbbell Wrist Flexion(p)','Dumbbell Wrist Curl(p)','One Leg Tibialis Raise(s)', 'Max Two Arm Hang','Two Leg Hops'],
                            
                            'Tuesday':['Peterson Step Up(s)','Two Leg Nordic Hamstring Curl','Iso Barbell Front squat','Iso Behind The Neck Press','Iso Barbell Bench Press','Iso Barbell Romanian Deadlift', 'Iso Barbell Wrist Flexion','Iso Barbell Wrist Curl','Iso Two Leg Dumbbell Tibialis Raise', 'One arm Hang','Max Speed Forward Sprinting'],

                            'Wednesday':['One Leg Reverse Squat(p)','Pull Ups(p)','Dumbbell ATG Split Squat(s)','Cable Pancake(s)','ATG Dumbbell External Rotation(p)','Medium Two Arm Hang','Standing Single Leg Box Jump'],

                            'Thursday':['Dumbbell Cossack Squat(s)','Seated Good Morning(p)', 'Dips(s)','Cable Hip Adduction(p)','Cable Hip Abduction(p)','Neck Upwards','Neck Downwards','Heavy Two Arm Hang','Arm Box Jump'],

                            'Friday':['Iso Peterson Step Up','One Leg Lying Hamstring Curl','Iso Reverse Squat','Iso Dumbbell Pullover','Iso Front Barbell ATG Split Squat','Iso Weighted Butterflys','Iso External Dumbbell Rotation','One Arm Hang','Two Leg Depth Drop'],

                            'Saturday':['One Leg Hip Thrust(p)','Incline Dumbbell Curl(s)','Incline Dumbbell Hammer Curl(p)','Farmer Walk(Single)','QL extension(p)','Lateral Dumbbell Raise(s)','Frontal Dumbbell Raise(p)','Face Pulls(s)','Light Two Arm Hang','Max Incline Backward Sprinting'],

                            'Sunday':['Peterson Step Up(s)','Two Leg Iso Seated Hamstring Curl','Iso Front Barbell Cossack Squat','Iso Barbell Back Row', 'Iso French Press','Iso Hip External and Internal Rotation',
                                       'Iso Two Legged Hip Thrust','Iso Barbell Curl','Iso Landmine Rotation','Iso Trap 3 Raise','Iso Dumbbell Fly','One Arm Hang','Standing Broad Jump']
                            },
                    
                    'Week 2':{'Monday':['Barbell Back Squat(s)','Barbell Push Press(p)','Dumbbell Bench Press(s)','Dumbbell Romanian Deadlift(p)','Dumbbell Wrist Flexion(s)','Dumbbell Wrist Curl(s)','One Leg Tibialis Raise(p)', 'Max Two Arm Hang','Two Legged Box Jump'],
                               
                            'Tuesday':['Peterson Step Up(s)','Single Leg Nordic Hamstring Curl','Iso Hack Squat','Iso Barbell Military Press','Iso Incline Dumbbell Press','Iso Dumbbell Sumo Deadlift', 'Iso Banded neck rotiation','Iso Single Leg Seated Calf Raise', 'One Arm Hang','Max Approach Jumping'],

                            'Wednesday':['One Leg Reverse Squat(s)','Pull Ups(s)','Dumbbell ATG Split Squat(p)','Cable Pancake(p)','ATG Dumbbell External Rotation(s)','Medium Two Arm Hang','Single Leg Hop'],

                            'Thursday':['Dumbbell Cossack Squat(p)','Seated Good Morning(s)', 'Dips(p)','Cable Hip Adduction(s)','Cable Hip Abduction(s)','Neck Upwards','Neck Downwards','Heavy Two Arm Hang','Full Range Arm Box Jump'],

                            'Friday':['Iso Peterson Step Up','Two Leg Iso Lying Hamstring Curl','Iso Hanging Leg Raise','Iso One Arm Dumbbell Row','Iso Back Barbell ATG Split Squat','Iso Weighted Pidgeon','Iso Powel Raise','One Arm Hang','Single Lateral Jump'],

                            'Saturday':['One Leg Hip Thrust(s)','Incline Dumbbell Curl(p)','Incline Dumbbell Hammer Curl(s)','Farmer Walk(Double)','QL extension(s)','Lateral Dumbbell Raise(p)','Frontal Raise(s)','Face Pulls(p)','Light Two Arm Hang','Max Incline Side Sprinting'],

                            'Sunday':['Peterson Step Up','One Leg Iso Seated Hamstring Curl','Iso Back Barbell Cossack Squat','Iso Dumbbell Jefferson Curl', 'Iso Push ups','Iso Hip Adductor Machine','Iso Hip Abduction Machine','Iso Dumbbell Ulnar Deviation','Iso Dumbbell Radial Deviation','One Arm Hang',
                                      'Iso Back Extension One Leg','Iso Reverse Curl','Iso Barbell Preacher Curl','Iso Ab Machine','Iso Dumbbell Shrug','Iso Row Machine', 'One Arm Hang','Bounding']
                            },
                        
                        'Week 3':{'Monday':['Power Clean(p)','Barbell Military Press(s)','Incline Dumbbell Press(p)','Dumbbell Sumo Deadlift(s)', 'Banded neck rotiation(p)','Single Leg Seated Calf Raise(s)', 'Max Two Arm Hang','Sitting Box Jump'],
                            
                            'Tuesday':['Peterson Step Up','Two Leg Iso Nordic Hamstring Curl','Iso Reverse Nordic','Iso Incline Barbell Press','Iso Barbell Deadlift', 'Iso Banded Neck Sides','Iso Single Leg Standing Calf Raise', 'One Arm Hang','Max Speed Backwards Sprinting'],

                            'Wednesday':['Hanging Leg Raise(p)','One Arm Dumbbell Row(p)','Back Barbell ATG Split Squat(s)','Weighted Pidgeon(s)','Powel Raise(p)','Medium Two Arm Hang','Sitting Single Leg Box Jump'],

                            'Thursday':['Back Barbell Cossack Squat(s)','Dumbbell Jefferson Curl(p)', 'Push ups(s)','Hip Adductor Machine(p)','Hip Abduction Machine(p)','Dumbbell Ulnar Deviation(s)','Dumbbell Radial Deviation(s)','Heavy Two Arm Hang','Arm Depth Box Jump'],

                            'Friday':['Iso Peterson Step Up','One Leg Iso Lying Hamstring Curl','Iso Single Leg Monkey Foot','Iso Lat Pull Down Machine','Iso Pistol Squat','Iso 90-90 Hip Push Press','Iso Cable External Rotation','One Arm Hang','Single Leg Depth Drop'],

                            'Saturday':['Back Extension One Leg(p)','Reverse Curl(s)','Barbell Preacher Curl(s)','Overhead Walk(Single)','Ab Machine(s)','Dumbbell Shrug(p)','Row Machine(s)', 'Light Two Arm Hang','Max Incline Forward Sprinting'],

                            'Sunday':['Iso Peterson Step Up','Two Leg Seated Hamstring Curl','Iso Barbell Jefferson Curl', 'Iso Tricep Extension','Iso Back Extension','Iso Chin Ups','Iso Dragon Flag','Iso Dumbbell Shrug','Iso Rear Delt Fly','One Arm Hang','Running Broad Jump']
                            },
                        
                        'Week 4':{'Monday':['Hack Squat(s)','Barbell Split Jerk(p)','Incline Dumbbell Press(s)','Dumbbell Sumo Deadlift(p)', 'Banded Neck Rotation(s)','Single Leg Seated Calf Raise(p)', 'Max Two Arm Hang','Two Leg Depth Jump'],
                            
                            'Tuesday':['Peterson Step Up','One Leg Iso Nordic Hamstring Curl','Iso Barbell Front Squat','Iso Behind The Neck Press','Iso Barbell Bench Press','Iso Barbell Romanian Deadlift', 'Iso Barbell Wrist Flexion','Iso Barbell Wrist Curl','Iso Two Leg Dumbbell Tibialis Raise', 'One arm Hang','Max Speed Side Sprinting'],

                            'Wednesday':['Hanging Leg Raise(s)','One Arm Dumbbell Row(s)','Back Barbell ATG Split Squat(p)','Weighted Pidgeon(p)','Powel Raise(s)','Medium Two Arm Hang','Single Leg Depth Jump'],

                            'Thursday':['Back Barbell Cossack Squat(p)','Dumbbell Jefferson Curl(s)', 'Push ups(p)','Hip Adductor Machine(s)','Hip Abduction Machine(s)','Dumbbell Ulnar Deviation(p)','Dumbbell Radial Deviation(p)','Heavy Two Arm Hang','Single Arm Box Jump'],

                            'Friday':['Iso Peterson Step Up','Two Leg Lying Hamstring Curl','Iso Reverse Squat','Iso Dumbbell Pullover','Iso Front Barbell ATG Split Squat','Iso Weighted Butterflys','Iso External Dumbbell Rotation','One Arm Hang','PJF Lateral Hop'],

                            'Saturday':['Back Extension One Leg(s)','Reverse Curl(p)','Barbell Preacher Curl(p)','Overhead Walk(Double)','Ab Machine(p)','Front Barbell Shrug(s)','Back Barbell Shrug(s)','Row Machine(p)','Light Two Arm Hang','Max Approach Jumping'],

                            'Sunday':['Peterson Step Up','One Leg Seated Hamstring Curl','Iso Back Barbell Cossack Squat','Iso Dumbbell Jefferson Curl', 'Iso Push ups','Iso Hip Adductor Machine','Iso Hip Abduction Machine','Iso Dumbbell Ulnar Deviation','Iso Dumbbell Radial Deviation',
                                      'Iso Back Extension One Leg','Iso Reverse Curl','Iso Barbell Preacher Curl','Iso Ab Machine','Iso Dumbbell Shrug','Iso Row Machine', 'One Arm Hang','Alternate Bounding']
                            },
                        
                        
                        'Week 5':{'Monday':['Dumbbell Jump Squat(p)','Behind The Neck Press(s)','Barbell Bench Press(p)','Barbell Romanian Deadlift(s)', 'Barbell Wrist Flexion(p)','Barbell Wrist Curl(p)','Two Leg Dumbbell Tibialis Raise(s)', 'Heavy Two Arm Hang','Two Leg Hops'],

                            'Tuesday':['Peterson Step Up','Two Leg Nordic Hamstring Curl','Iso Barbell Back Squat','Iso Dumbbell Press','Iso Dumbbell Bench Press','Iso Dumbbell Romanian Deadlift','Iso Dumbbell Wrist Flexion','Iso Dumbbell Wrist Curl','Iso One Leg Tibialis Raise', 'One Arm Hang','Max Speed Forward Sprinting'],

                            'Wednesday':['Two Legged Reverse Squat(p)','Dumbbell Pullover(p)','Front Barbell ATG Split Squat(s)','Weighted Butterflys(s)','External Dumbbell Rotation(p)','Heavy Two Arm Hang','Standing Single Leg Box Jump'],

                            'Thursday':['Front Barbell Cossack Squat(s)','Penlay Row(p)', 'French Press(s)','Hip External and Internal Rotation(p)','Barbell Shoulder Rotation(s)','Heavy Two Arm Hang','Arm Box Jump'],

                            'Friday':['Peterson Step Up','Two Leg Lying Hamstring Curl','Iso One Leg Reverse Squat','Iso Pull Ups','Iso Dumbbell ATG Split Squat','Iso Cable Pancake','Iso ATG Dumbbell External Rotation','One Arm Hang','Two Leg Depth Drop'],

                            'Saturday':['Two Legged Hip Thrust(p)','Barbell Curl(s)','Side Farmer Walk(Single)','Landmine Rotation(s)','Trap 3 Raise(p)','Dumbbell Fly(s)','Heavy Two Arm Hang','Max Incline Backward Sprinting'],

                            'Sunday':['Peterson Step Up','Single Leg Nordic Hamstring Curl','Iso Dumbbell Cossack Squat','Iso Seated Good Morning', 'Iso Dips','Iso Cable Hip Adduction','Iso Cable Hip Abduction','Iso Neck Upwards','Iso Neck Downwards',
                                      'Iso One Leg Hip Thrust','Iso Incline Dumbbell Curl','Iso Incline Dumbbell Hammer Curl','Iso QL extension','Iso Lateral Dumbbell Raise','Iso Frontal Raise','Iso Face Pulls','One Arm Hang','Standing Broad Jump'],
                            },
                        

                        'Week 6':{'Monday':['Barbell Front Squat(s)','Behind The Neck Push Press(p)','Barbell Bench Press(s)','Barbell Romanian Deadlift(p)', 'Barbell Wrist Flexion(s)','Barbell Wrist Flexion(s)','Two Leg Dumbbell Tibialis Raise(p)', 'Heavy Two Arm Hang','Two Legged Box Jump'],

                            'Tuesday':['Peterson Step Up','Two Leg Seated Hamstring Curl','Iso Reverse Nordic','Iso Incline Barbell Press','Iso Barbell Deadlift', 'Iso Banded Neck Sides','Iso Single Leg Standing Calf Raise', 'One Arm Hang','Max Approach Jumping'],

                            'Wednesday':['Two Legged Reverse Squat(s)','Dumbbell Pullover(s)','Front Barbell ATG Split Squat(p)','Weighted Butterflys(p)','External Dumbbell Rotation(s)','Heavy Two Arm Hang','Single Leg Hop'],

                            'Thursday':['Front Barbell Cossack Squat(p)','Barbell Back Row(s)', 'French Press(p)','Hip External and Internal Rotation(s)','Barbell Shoulder Rotation(p)','Heavy Two Arm Hang','Full Range Arm Box Jump'],

                            'Friday':['Peterson Step Up','Two Leg Nordic Hamstring Curl','Iso Single Leg Monkey Foot','Iso Lat Pull Down Machine','Iso Pistol Squat','Iso 90-90 Hip Push Press','Iso Cable External Rotation','One Arm Hang','Single Lateral Jump'],

                            'Saturday':['Two Legged Hip Thrust(s)','Barbell Curl(p)','Side Farmer Walk(Double)','Landmine Rotation(p)','Trap 3 Raise(s)','Dumbbell Fly(p)','Heavy Two Arm Hang','Depth Drop','Max Incline Side Sprinting'],
                            
                            'Sunday':['Peterson Step Up','Iso Peterson Step Up','Single Leg Lying Hamstring Curl','Iso Barbell Jefferson Curl', 'Iso Tricep Extension','Iso Back Extension','Iso Chin Ups','Iso Dragon Flag','Iso Dumbbell Shrug','Iso Rear Delt Fly','One Arm Hang','Bounding']
                            },


                        
                        'Week 7':{'Monday':['Squat Clean(p)','Landmine Split Jerk(p)','Incline Barbell Press(p)','Barbell Deficit Deadlift(s)', 'Banded Neck Sides(p)','Single Leg Standing Calf Raise(s)', 'Heavy Two Arm Hang','Sitting Box Jump'],

                            'Tuesday':['Iso Hack Squat','Single Leg Nordic Hamstring Curl','Iso Barbell Military Press','Iso Incline Dumbbell Press','Iso Dumbbell Sumo Deadlift', 'Iso Banded neck rotiation','Iso Single Leg Seated Calf Raise', 'One Arm Hang','Max Speed Backwards Sprinting'],

                            'Wednesday':['Single Leg Monkey Foot(p)','Lat Pull Down Machine(p)','Pistol Squat(s)','90-90 Hip Push Press(s)','Cable External Rotation(p)','Heavy Two Arm Hang','Sitting Single Leg Box Jump'],

                            'Thursday':['Peterson Step Up(p)','Barbell Jefferson Curl(p)', 'Tricep Extension(s)','Lateral Step Up(p)','Wrist Rotation(s)','Heavy Two Arm Hang','Arm Depth Box Jump'],

                            'Friday':['Peterson Step Up','Single Leg Seated Hamstring Curl','Iso Hanging Leg Raise','Iso One Arm Dumbbell Row','Iso Back Barbell ATG Split Squat','Iso Weighted Pidgeon','Iso Powel Raise','One Arm Hang','Single Leg Depth Drop'],

                            'Saturday':['Back Extension(p)','Chin Ups(s)','Side Overhead Walk(Single)','Dragon Flag(p)','Dumbbell Shrug(p)','Rear Delt Fly(s)','Heavy Two Arm Hang','Max Incline Forward Sprinting'],

                            'Sunday':['Peterson Step Up','Two Leg Nordic Hamstring Curl','Iso Back Barbell Cossack Squat','Iso Dumbbell Jefferson Curl', 'Iso Push ups','Iso Hip Adductor Machine','Iso Hip Abduction Machine','Iso Dumbbell Ulnar Deviation','Iso Dumbbell Radial Deviation',
                                      'Iso Back Extension One Leg','Iso Reverse Curl','Iso Barbell Preacher Curl','Iso Ab Machine','Iso Dumbbell Shrug','Iso Row Machine', 'One Arm Hang','Running Broad Jump']
                            },

                        'Week 8':{'Monday':['Reverse Nordic(s)','Lateral Landmine Split Jerk(p)','Incline Barbell Press(s)','Barbell Deadlift(s)', 'Banded Neck Sides(s)','Single Leg Standing Calf Raise(p)', 'Heavy Two Arm Hang','Depth Jump'],

                            'Tuesday':['Peterson Step Up','Two Leg Lying Hamstring Curl','Iso Barbell Back Squat','Iso Barbell Military Press','Iso Dumbbell Bench Press','Iso Dumbbell Romanian Deadlift','Iso Dumbbell Wrist Flexion','Iso Dumbbell Wrist Curl','Iso One Leg Tibialis Raise', 'One Arm Hang','Max Speed Side Sprinting'],

                            'Wednesday':['Single Leg Monkey Foot(s)','Lat Pull Down Machine(s)','Pistol Squat(p)','90-90 Hip Push Press(p)','Cable External Rotation(s)','Heavy Two Arm Hang','Single Leg Depth Jump'],

                            'Thursday':['Peterson Step Up(s)','Barbell Jefferson Curl(s)', 'Muscle Up(p)','Lateral Step Up(s)','Wrist Rotation(p)','Heavy Two Arm Hang','Single Arm Box Jump'],

                            'Friday':['Peterson Step Up','Single Leg Nordic Hamstring Curl','Iso One Leg Reverse Squat','Iso Pull Ups','Iso Dumbbell ATG Split Squat','Iso Cable Pancake','Iso ATG Dumbbell External Rotation','One Arm Hang','PJF Lateral Hop'],

                            'Saturday':['Back Extension(s)','Chin Ups(p)','Side Overhead Walk(Double)','Dragon Flag(p)','Dumbbell Shrug(s)','Rear Delt Fly(p)','Heavy Two Arm Hang','Max Approach Jumping'],

                            'Sunday':['Peterson Step Up','Two Leg Seated Hamstring Curl','Iso Dumbbell Cossack Squat','Iso Seated Good Morning', 'Iso Dips','Iso Cable Hip Adduction','Iso Cable Hip Abduction','Iso Neck Upwards','Iso Neck Downwards',
                                      'Iso One Leg Hip Thrust','Iso Incline Dumbbell Curl','Iso Incline Dumbbell Hammer Curl','Iso QL extension','Iso Lateral Dumbbell Raise','Iso Frontal Raise','Iso Face Pulls','One Arm Hang','Alternate Bounding'],

                            },
                                                     
                             }



print(weekly_exercises)


# Open the file in read mode
with open('workout_log.txt', 'r') as file:
    content = file.read()  # This reads the entire content of the file

#print(content)
content = content.lower() # Remove capitalization

exercise_day = weekly_exercises['Week 5']['Sunday']
recent_exercises = []
for exercise in exercise_day:
# Define the target string and the regex pattern
    target_string = exercise.lower()
    # Make it so that the () are not taken into account as metacharacers from regex
    target_string = re.escape(target_string) 
    pattern = re.compile(f'{target_string}.*?(?=\n|$)', re.DOTALL | re.MULTILINE)
    # Version of code which enabels to 2 mismatches to occur - Based on chatGPT
    
    # Generate a regex pattern with optional character classes for mismatches


    pattern = re.compile(f'{target_string}.*?(?=\n|$)', re.DOTALL | re.MULTILINE)
    '''
    escaped_target_string = re.escape(target_string)
    fuzzy_pattern = f'{escaped_target_string}{{e<=2}}'
    pattern = re.compile(f'{fuzzy_pattern}.*?(?=\n|$)', re.DOTALL | re.MULTILINE)
    '''
    '''
    pattern = re.compile(
    f'({re.escape(target_string)}){{e<=2}}',
    re.IGNORECASE
)
    '''
    
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