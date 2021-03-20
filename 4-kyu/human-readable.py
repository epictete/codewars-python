def format(res):
    if len(res) == 0:
        return "now"
    elif len(res) == 1:
        return res[0]
    elif len(res) == 2:
        return " and ".join(res)
    else:
        return ", ".join(res[:-2]) + ", " + " and ".join(res[-2:])

def format_duration(seconds):
    years, seconds = divmod(seconds, 60**2*24*365)
    days, seconds = divmod(seconds, 60**2*24)
    hours, seconds = divmod(seconds, 60**2)
    minutes, seconds = divmod(seconds, 60)

    units = [
        [years, "year"],
        [days, "day"],
        [hours, "hour"],
        [minutes, "minute"],
        [seconds, "second"],
    ]

    res = []

    for unit in units:
        if unit[0] == 1:
            res += [f"{unit[0]} {unit[1]}"]
        elif unit[0] > 1:
            res += [f"{unit[0]} {unit[1]}s"]
    
    return format(res)



print(format_duration(1), "1 second")
print(format_duration(62), "1 minute and 2 seconds")
print(format_duration(120), "2 minutes")
print(format_duration(3600), "1 hour")
print(format_duration(3662), "1 hour, 1 minute and 2 seconds")