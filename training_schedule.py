import datetime
# Get todays date
#print(datetime.datetime.today().strftime('%Y-%m-%d'))
#How to obtain current date and time - https://stackoverflow.com/questions/32490629/getting-todays-date-in-yyyy-mm-dd-in-python
#print(datetime.datetime.today().strftime('%d-%m-%Y'))


#How to get the date for later in time - https://datatofish.com/get-previous-current-and-next-day-system-dates-in-python/


mappings = {'0':'Train','1':'Rest'}
total_days =365
counter = 0 
#for specific_day in range(total_days,0,-1):
for specific_day in range(total_days):
    Desired_Date = datetime.datetime.today() + datetime.timedelta(days=specific_day)
    Desired_Date_Formatted = Desired_Date.strftime ('%d%m%Y') # format the date to ddmmyyyy
    counter += 1

    first = counter%2
    desired_text = str(Desired_Date_Formatted) + f'-{mappings[str(first)]}'
    print(desired_text)
    