import datetime

# Get todays date
#print(datetime.datetime.today().strftime('%Y-%m-%d'))
#How to obtain current date and time - https://stackoverflow.com/questions/32490629/getting-todays-date-in-yyyy-mm-dd-in-python
#print(datetime.datetime.today().strftime('%d-%m-%Y'))


#How to get the date for later in time - https://datatofish.com/get-previous-current-and-next-day-system-dates-in-python/

#mapping = {'Side':0,'Hairline':1,'Scalp':2}

mappings = {'0':'Hairline','1':'Side','2':'Scalp'}
total_days =30
counter = 0 
for specific_day in range(total_days,0,-1):
#for specific_day in range(total_days):
    Desired_Date = datetime.datetime.today() + datetime.timedelta(days=specific_day)
    Desired_Date_Formatted = Desired_Date.strftime ('%d%m%Y') # format the date to ddmmyyyy
    first = counter%3
    counter += 1
    second = counter%3
    counter += 1
    print(str(Desired_Date_Formatted) + f'-{mappings[str(first)]} and {mappings[str(second)]}')

# Make a map for the specific massage
# Need to make it so that it iterates through the different schedules
# Need to go through 2 values per day
# Need to reset to 0 after going to 2