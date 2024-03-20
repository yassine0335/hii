
from datetime import datetime, timedelta
import datetime
#fromtimes
def find_next_Monday():
    today=datetime.date.today()
    days_until_Monday = (6 - today.weekday()) % 7
    next_Monday = today + datetime.timedelta(days=days_until_Monday)
    next_Monday_datetime = datetime.datetime.combine(next_Monday, datetime.datetime.min.time())
    next_Monday_stamp=int(next_Monday_datetime.timestamp())

    return next_Monday_stamp

def find_next_Tuesday():
    today=datetime.date.today()
    days_until_Tuesday = (6 - today.weekday()) % 7
    next_Tuesday = today + datetime.timedelta(days=days_until_Tuesday)
    next_Tuesday_datetime = datetime.datetime.combine(next_Tuesday, datetime.datetime.min.time())
    next_Tuesday_stamp=int(next_Tuesday_datetime.timestamp())
    
    return next_Tuesday_stamp

def find_next_Wednesday():
    today=datetime.date.today()
    days_until_Wednesday = (6 - today.weekday()) % 7
    next_Wednesday = today + datetime.timedelta(days=days_until_Wednesday)
    next_Wednesday_datetime = datetime.datetime.combine(next_Wednesday, datetime.datetime.min.time())
    next_Wednesday_stamp=int(next_Wednesday_datetime.timestamp())
    print(next_Wednesday_stamp)
    return next_Wednesday_stamp

def find_next_Thursday():
    today=datetime.date.today()
    days_until_Thursday = (6 - today.weekday()) % 7
    next_Thursday = today + datetime.timedelta(days=days_until_Thursday)
    next_Thursday_datetime = datetime.datetime.combine(next_Thursday, datetime.datetime.min.time())
    next_Thursday_stamp=int(next_Thursday_datetime.timestamp())
    return next_Thursday_stamp


def find_next_Friday():
    today = datetime.date.today()
    days_until_Friday = (6 - today.weekday()) % 7
    next_Friday = today + datetime.timedelta(days=days_until_Friday)
    # Convert next_Friday to a datetime object
    next_Friday_datetime = datetime.datetime.combine(next_Friday, datetime.datetime.min.time())
    next_Friday_stamp=int(next_Friday_datetime.timestamp())
    return next_Friday_stamp

def find_next_Saturday(time=None):
    today = datetime.date.today()
    # Calculate days until next Saturday
    days_until_Saturday = (5 - today.weekday() + 7) % 7
    # Add days to today's date to get next Saturday
    next_Saturday = today + datetime.timedelta(days=days_until_Saturday)

    if time is not None:
        # Parse the time string
        hours, minutes = map(int, time.split(':'))
        # Combine date and time
        next_Saturday = datetime.datetime.combine(next_Saturday, datetime.time(hours, minutes))
    else:
        # If no time provided, set default to midnight
        next_Saturday = datetime.datetime.combine(next_Saturday, datetime.datetime.min.time())

    # Convert next Saturday to timestamp
    next_Saturday_timestamp = int(next_Saturday.timestamp())
    return next_Saturday_timestamp

def find_next_Sunday():
    today = datetime.date.today()
    days_until_sunday = (6 - today.weekday()) % 7
    next_sunday = today + datetime.timedelta(days=days_until_sunday)
    # Convert next_sunday to a datetime object
    next_sunday_datetime = datetime.datetime.combine(next_sunday, datetime.time(5, 0))
    next_sunday_stamp=int(next_sunday_datetime.timestamp())
    return next_sunday_stamp

def find_next_day(day, time=None):
    today = datetime.date.today()
    days_until_next_day = (day - today.weekday() + 7) % 7
    next_day = today + datetime.timedelta(days=days_until_next_day)

    if time is not None:
        hours, minutes = map(int, time.split(':'))
        next_day = datetime.datetime.combine(next_day, datetime.time(hours, minutes))
    else:
        next_day = int(datetime.datetime.combine(next_day, datetime.datetime.min.time()))

    next_day_timestamp = int(next_day.timestamp())
    return next_day_timestamp



#AU 2X Trio/AU 3X Quad/EU 2X Solo/EU 2X Max 5/EU 3X Solo/EU 3X Trio/EU 3X Trio/EU 5X Quad/US 2X Solo/US 2X Max 5
March21_5am=1711036800
March21_3pm=1711029600
March21_4pm=1711033200
March21_7pm=1711044000
March21_8pm=1711047600
#  AU 3X Trio/EU 2X Trio/EU 3X Duo/EU 3X Quad/EU 5X Trio/EU 5X NoBPs/US 2X Trio/US 3X Trio/US 3X Quad/US 5X Trio/US 10X NoBPs/
March19_5am=1710820800
March19_3pm=1710856800
March19_4pm=1710860400
March19_7pm=1710871200
March19_8pm=1710874800
#EU 2X Duo/EU 2X Quad/////////////
March22_3pm=1711116000
March22_7pm=1711130400
March22_4pm=1711119600
March22_7am=1711087200
#Vanilla Trio///
March23_3pm=1711202400
#US 2X Duo/US 2X Quad/US 3X Solo/US 3X Duo/US 3X Max 5/US 5X Quad/US 5X NoBPs
March18_7pm=1710784800
March18_8pm=1710788400
March18_5pm=1710777600
March18_6pm=1710738000
#
March20_4pm=1710946800
March20_3pm=1710943200
#
March22_6pm=1711083600

given_timestamp = 1711036800

given_datetime = datetime.datetime.fromtimestamp(given_timestamp)


current_datetime = datetime.datetime.now()
timestamp_now = current_datetime.timestamp()

from datetime import datetime, timedelta
import datetime

def Add_3days(given_timestamp):

    timestamp_now = datetime.datetime.now().timestamp()
    given_datetime = datetime.datetime.fromtimestamp(given_timestamp)

    while timestamp_now > given_timestamp:
        given_datetime += timedelta(days=3)
        given_timestamp = int(given_datetime.timestamp())
        return given_timestamp
    return given_timestamp
def Add_4days(given_timestamp):

    timestamp_now = datetime.datetime.now().timestamp()
    given_datetime = datetime.datetime.fromtimestamp(given_timestamp)
    
    while timestamp_now > given_timestamp:
        given_datetime += timedelta(days=4)
        given_timestamp = int(given_datetime.timestamp())
        return given_timestamp
    return given_timestamp


from datetime import datetime, timedelta
import datetime
today_timestamp = datetime.datetime.now().timestamp()


next_Monday_timestamp=find_next_Monday()
next_Tuesday_timestamp = find_next_Tuesday()
next_Wednesday_timestamp=find_next_Wednesday()
next_Thursday_timestamp=find_next_Thursday()
next_Friday_timestamp=find_next_Friday()
next_Saturday_timestamp=find_next_Saturday()
next_Sunday_timestamp = find_next_Sunday()

days_until_next_Monday = (next_Monday_timestamp - today_timestamp) / (3600 * 24)
days_until_next_Tuesday = (next_Tuesday_timestamp - today_timestamp) / (3600 * 24)
days_until_next_Wednesday = (next_Wednesday_timestamp - today_timestamp) / (3600 * 24)
days_until_next_Thursday = (next_Thursday_timestamp - today_timestamp) / (3600 * 24)
days_until_next_Friday = (next_Friday_timestamp - today_timestamp) / (3600 * 24)
days_until_next_Saturday = (next_Saturday_timestamp - today_timestamp) / (3600 * 24)
days_until_next_Sunday = (next_Sunday_timestamp - today_timestamp) / (3600 * 24)

if days_until_next_Sunday < days_until_next_Tuesday:
    print("Sunday is near")
    
else:
    print("Tuesday is near")


def tuesday_Saturday(tuesday_time="05:00", saturday_time="05:00"):
    today = datetime.datetime.today()
    current_weekday = today.weekday()
    
    # Calculate the next Tuesday and Saturday
    if current_weekday <= 1:  # If today is Monday or Tuesday
        next_Tuesday = today + datetime.timedelta(days=(1 - current_weekday))
    else:
        next_Tuesday = today + datetime.timedelta(days=(8 - current_weekday))
    
    if current_weekday <= 5:  # If today is Tuesday to Saturday
        next_Saturday = today + datetime.timedelta(days=(5 - current_weekday))
    else:
        next_Saturday = today + datetime.timedelta(days=(12 - current_weekday))
    
    # Check if times are provided
    tuesday_hours, tuesday_minutes = map(int, tuesday_time.split(':'))
    saturday_hours, saturday_minutes = map(int, saturday_time.split(':'))

    # Calculate the timestamps of the next Tuesday and Saturday with the provided times
    next_Tuesday_with_time = datetime.datetime.combine(next_Tuesday.date(), datetime.time(tuesday_hours, tuesday_minutes))
    next_Saturday_with_time = datetime.datetime.combine(next_Saturday.date(), datetime.time(saturday_hours, saturday_minutes))

    # Calculate the differences between the target time and both next Tuesday and next Saturday
    target_time = datetime.datetime(today.year, today.month, today.day, tuesday_hours, tuesday_minutes)
    delta_tuesday = abs((target_time - next_Tuesday_with_time).total_seconds())
    
    target_time = datetime.datetime(today.year, today.month, today.day, saturday_hours, saturday_minutes)
    delta_saturday = abs((target_time - next_Saturday_with_time).total_seconds())
    
    # Compare the differences and return the closest timestamp
    if delta_tuesday < delta_saturday:
        return int(next_Tuesday_with_time.timestamp())
    else:
        return int(next_Saturday_with_time.timestamp())


def monday_friday(monday_time="05:00", friday_time="05:00"):
    today = datetime.datetime.today()
    current_weekday = today.weekday()
    
    # Calculate the next Monday and Friday
    if current_weekday <= 0:  # If today is Monday
        next_Monday = today + datetime.timedelta(days=(7 - current_weekday))
    else:
        next_Monday = today + datetime.timedelta(days=(7 - current_weekday) + 7)
    
    if current_weekday <= 3:  # If today is Monday to Thursday
        next_Friday = today + datetime.timedelta(days=(4 - current_weekday))
    else:
        next_Friday = today + datetime.timedelta(days=(4 - current_weekday) + 7)
    
    # Check if times are provided
    monday_hours, monday_minutes = map(int, monday_time.split(':'))
    friday_hours, friday_minutes = map(int, friday_time.split(':'))

    # Calculate the timestamps of the next Monday and Friday with the provided times
    next_Monday_with_time = datetime.datetime.combine(next_Monday.date(), datetime.time(monday_hours, monday_minutes))
    next_Friday_with_time = datetime.datetime.combine(next_Friday.date(), datetime.time(friday_hours, friday_minutes))

    # Calculate the differences between the current day and both next Monday and next Friday
    delta_monday = next_Monday - today
    delta_friday = next_Friday - today
    
    # Compare the differences and return the closest timestamp
    if delta_monday < delta_friday:
        return int(next_Monday_with_time.timestamp())
    else:
        return int(next_Friday_with_time.timestamp())


def tuesday_friday(tuesday_time="05:00", friday_time="05:00"):
    today = datetime.datetime.today()
    current_weekday = today.weekday()
    
    # Calculate the next Tuesday and Friday
    if current_weekday <= 1:  # If today is Monday or Tuesday
        next_Tuesday = today + datetime.timedelta(days=(1 - current_weekday))
    else:
        next_Tuesday = today + datetime.timedelta(days=(8 - current_weekday))
    
    if current_weekday <= 4:  # If today is Tuesday to Friday
        next_Friday = today + datetime.timedelta(days=(4 - current_weekday))
    else:
        next_Friday = today + datetime.timedelta(days=(11 - current_weekday))
    
    # Check if times are provided
    tuesday_hours, tuesday_minutes = map(int, tuesday_time.split(':'))
    friday_hours, friday_minutes = map(int, friday_time.split(':'))

    # Calculate the timestamps of the next Tuesday and Friday with the provided times
    next_Tuesday_with_time = datetime.datetime.combine(next_Tuesday.date(), datetime.time(tuesday_hours, tuesday_minutes))
    next_Friday_with_time = datetime.datetime.combine(next_Friday.date(), datetime.time(friday_hours, friday_minutes))

    # Calculate the differences between the current day and both next Tuesday and next Friday
    delta_tuesday = next_Tuesday - today
    delta_friday = next_Friday - today
    
    # Compare the differences and return the closest timestamp
    if delta_tuesday < delta_friday:
        return int(next_Tuesday_with_time.timestamp())
    else:
        return int(next_Friday_with_time.timestamp())

def wednesday_saturday(wednesday_time="05:00", saturday_time="05:00"):
    today = datetime.datetime.today()
    current_weekday = today.weekday()
    
    # Calculate the next Wednesday and Saturday
    if current_weekday <= 2:  # If today is Monday to Wednesday
        next_Wednesday = today + datetime.timedelta(days=(2 - current_weekday))
    else:
        next_Wednesday = today + datetime.timedelta(days=(9 - current_weekday))
    
    if current_weekday <= 5:  # If today is Monday to Saturday
        next_Saturday = today + datetime.timedelta(days=(5 - current_weekday))
    else:
        next_Saturday = today + datetime.timedelta(days=(12 - current_weekday))
    
    # Check if times are provided
    wednesday_hours, wednesday_minutes = map(int, wednesday_time.split(':'))
    saturday_hours, saturday_minutes = map(int, saturday_time.split(':'))

    # Calculate the timestamps of the next Wednesday and Saturday with the provided times
    next_Wednesday_with_time = datetime.datetime.combine(next_Wednesday.date(), datetime.time(wednesday_hours, wednesday_minutes))
    next_Saturday_with_time = datetime.datetime.combine(next_Saturday.date(), datetime.time(saturday_hours, saturday_minutes))

    # Calculate the differences between the current day and both next Wednesday and next Saturday
    delta_wednesday = next_Wednesday - today
    delta_saturday = next_Saturday - today
    
    # Compare the differences and return the closest timestamp
    if delta_wednesday < delta_saturday:
        return int(next_Wednesday_with_time.timestamp())
    else:
        return int(next_Saturday_with_time.timestamp())

def thursday_sunday(thursday_time="05:00", sunday_time="05:00"):
    today = datetime.datetime.today()
    current_weekday = today.weekday()
    
    # Calculate the next Thursday and Sunday
    if current_weekday <= 3:  # If today is Monday to Thursday
        next_Thursday = today + datetime.timedelta(days=(3 - current_weekday))
    else:
        next_Thursday = today + datetime.timedelta(days=(10 - current_weekday))
    
    if current_weekday <= 6:  # If today is Monday to Sunday
        next_Sunday = today + datetime.timedelta(days=(6 - current_weekday))
    else:
        next_Sunday = today + datetime.timedelta(days=(13 - current_weekday))
    
    # Check if times are provided
    thursday_hours, thursday_minutes = map(int, thursday_time.split(':'))
    sunday_hours, sunday_minutes = map(int, sunday_time.split(':'))

    # Calculate the timestamps of the next Thursday and Sunday with the provided times
    next_Thursday_with_time = datetime.datetime.combine(next_Thursday.date(), datetime.time(thursday_hours, thursday_minutes))
    next_Sunday_with_time = datetime.datetime.combine(next_Sunday.date(), datetime.time(sunday_hours, sunday_minutes))

    # Calculate the differences between the current day and both next Thursday and next Sunday
    delta_thursday = next_Thursday - today
    delta_sunday = next_Sunday - today
    
    # Compare the differences and return the closest timestamp
    if delta_thursday < delta_sunday:
        return int(next_Thursday_with_time.timestamp())
    else:
        return int(next_Sunday_with_time.timestamp())
def wednesday_sunday(wednesday_time="05:00", sunday_time="05:00"):
    today = datetime.datetime.today()
    current_time = datetime.datetime.now().time()
    current_weekday = today.weekday()

    # Calculate the next Wednesday and Sunday
    if current_weekday <= 2:  # If today is Monday to Wednesday
        next_Wednesday = today + datetime.timedelta(days=(2 - current_weekday))
    else:
        next_Wednesday = today + datetime.timedelta(days=(9 - current_weekday))

    if current_weekday <= 6:  # If today is Monday to Sunday
        next_Sunday = today + datetime.timedelta(days=(6 - current_weekday))
    else:
        next_Sunday = today + datetime.timedelta(days=(13 - current_weekday))

    # Check if times are provided
    wednesday_hours, wednesday_minutes = map(int, wednesday_time.split(':'))
    sunday_hours, sunday_minutes = map(int, sunday_time.split(':'))

    # Calculate the timestamps of the next Wednesday and Sunday with the provided times
    next_Wednesday_with_time = datetime.datetime.combine(next_Wednesday.date(), datetime.time(wednesday_hours, wednesday_minutes))
    next_Sunday_with_time = datetime.datetime.combine(next_Sunday.date(), datetime.time(sunday_hours, sunday_minutes))

    # Calculate the differences between the current time and both next Wednesday and next Sunday
    delta_wednesday = (next_Wednesday_with_time - datetime.datetime.combine(today.date(), current_time)).total_seconds()
    delta_sunday = (next_Sunday_with_time - datetime.datetime.combine(today.date(), current_time)).total_seconds()

    # Compare the differences and return the closest timestamp
    if delta_wednesday < 0:
        delta_wednesday += 7 * 24 * 3600  # Add a week if it's in the past
    if delta_sunday < 0:
        delta_sunday += 7 * 24 * 3600  # Add a week if it's in the past

    if delta_wednesday < delta_sunday:
        return int(next_Wednesday_with_time.timestamp())
    else:
        return int(next_Sunday_with_time.timestamp())


def monday_thursday(monday_time="05:00", thursday_time="05:00"):
    today = datetime.datetime.today()
    current_weekday = today.weekday()
    
    # Calculate the next Monday and Thursday
    if current_weekday == 0:  # If today is Monday
        next_Monday = today + datetime.timedelta(days=7)
    else:
        next_Monday = today + datetime.timedelta(days=(7 - current_weekday))
    
    if current_weekday <= 3:  # If today is Monday to Thursday
        next_Thursday = today + datetime.timedelta(days=(3 - current_weekday))
    else:
        next_Thursday = today + datetime.timedelta(days=(10 - current_weekday))
    
    # Check if times are provided
    monday_hours, monday_minutes = map(int, monday_time.split(':'))
    thursday_hours, thursday_minutes = map(int, thursday_time.split(':'))

    # Calculate the timestamps of the next Monday and Thursday with the provided times
    next_Monday_with_time = datetime.datetime.combine(next_Monday.date(), datetime.time(monday_hours, monday_minutes))
    next_Thursday_with_time = datetime.datetime.combine(next_Thursday.date(), datetime.time(thursday_hours, thursday_minutes))

    # Calculate the differences between the current day and both next Monday and next Thursday
    delta_monday = next_Monday - today
    delta_thursday = next_Thursday - today
    
    # Compare the differences and return the closest timestamp
    if delta_monday < delta_thursday:
        return int(next_Monday_with_time.timestamp())
    else:
        return int(next_Thursday_with_time.timestamp())

def first_thursday_of_next_month(time="00:00"):
    today = datetime.datetime.now()
    first_day_of_next_month = datetime.datetime(today.year if today.month < 12 else today.year + 1,
                                                today.month + 1 if today.month < 12 else 1,
                                                1,
                                                hour=int(time.split(":")[0]),
                                                minute=int(time.split(":")[1]))
    days_until_thursday = (3 - first_day_of_next_month.weekday() + 7) % 7
    first_thursday = first_day_of_next_month + datetime.timedelta(days=days_until_thursday)
    return int(first_thursday.timestamp())




def be_weekly_thurs(time_str):
    # Starting date: 21st March
    start_date = datetime.datetime(year=2024, month=3, day=21)

    # Get today's date
    today = datetime.datetime.now().date()

    # Convert the time string to datetime object
    time_obj = datetime.datetime.strptime(time_str, '%H:%M')

    # Set the time on the start date
    start_date = start_date.replace(hour=time_obj.hour, minute=time_obj.minute)

    # Add two weeks until the date is greater than today
    while start_date.date() <= today:
        start_date += timedelta(weeks=2)

    # Return the timestamp of the resulting date and time
    return int(start_date.timestamp())

# Example usage:

