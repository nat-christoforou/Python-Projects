"""A Time Calculator."""


def hours_and_minutes(time):
    """Split string formatted time to hours and minutes."""
    if len(time) <= 6:
        hours, minutes = time.split(':')
        return int(hours), int(minutes)
    time, am_pm = time.split()
    hours, minutes = time.split(':')
    return int(hours), int(minutes), am_pm


def hour12_to_hour24(hour, am_pm):
    """Convert hour from 21-hour format to 24-hour format."""
    if am_pm == 'PM' and hour < 12:
        hour += 12
    elif am_pm == 'AM' and hour == 12:
        hour = 0
    return hour


def hour24_to_hour12(hour):
    """Convert hour from 24-hour format to 12-hour format."""
    if hour == 0:
        return str(12), ' AM'
    if hour < 12:
        return str(hour), ' AM'
    if hour == 12:
        return str(hour), ' PM'
    if hour < 24:
        return str(hour % 12), ' PM'
    return hour24_to_hour12(hour - 24)


def minutes_to_str(minutes):
    """Format the minutes properly."""
    if minutes < 10:
        return ':0' + str(minutes)
    return ':' + str(minutes)


def calculate_days_after(hour):
    """Calculate the number of days passed after adding the duration."""
    days_after = 0
    if hour < 24:
        return 0
    while hour >= 24:
        days_after += 1
        hour -= 24
    return days_after


def add_time(start, duration, day=None):
    """Add duration to time and return the result in an appropriate format."""
    # split hours, minutes and am/pm for start time and duration
    start_h, start_m, start_am_pm = hours_and_minutes(start)
    duration_h, duration_m = hours_and_minutes(duration)

    # convert start hour from 12-Hour to 24-Hour Format
    start_h = hour12_to_hour24(start_h, start_am_pm)

    # add duration to start time
    result_h = start_h + duration_h
    result_m = start_m + duration_m

    # check if result minutes are more than 60
    if result_m > 60:
        result_m -= 60
        result_h += 1

    # convert minutes to appropriate string format
    final_result_minutes = minutes_to_str(result_m)

    # calculate how many days after
    days_after = calculate_days_after(result_h)

    # convert result hour from 24-hour to 12-hour format and to string
    final_result_hour, final_ampm = hour24_to_hour12(result_h)

    if day:
        weekdays = {'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3,
                    'friday': 4, 'saturday': 5, 'sunday': 6}
        result_day = (weekdays[day.lower()] + days_after) % 7
        final_result_day = list(weekdays.keys())[list(weekdays.values()).index(result_day)]. \
            capitalize()

        if days_after == 1:
            new_time = final_result_hour + final_result_minutes + \
                       final_ampm + ', ' + final_result_day + ' (next day)'
        elif days_after > 1:
            new_time = final_result_hour + final_result_minutes + \
                       final_ampm + ', ' + final_result_day + \
                       ' (' + str(days_after) + ' days later)'
        else:
            new_time = final_result_hour + final_result_minutes + \
                       final_ampm + ', ' + final_result_day

    else:
        if days_after == 1:
            new_time = final_result_hour + final_result_minutes + \
                       final_ampm + ' (next day)'
        elif days_after > 1:
            new_time = final_result_hour + final_result_minutes + \
                       final_ampm + ' (' + str(days_after) + ' days later)'
        else:
            new_time = final_result_hour + final_result_minutes + final_ampm

    return new_time
