def date_autumn(dates):
    max_timestamp = -1
    max_timestamp_string = None
    for date in dates:
        tmp = int(date[0:1]), int(date[3:4]), int(date[6:])
        ts = tmp[2] * 365 + tmp[1] + tmp[0] * 30
        if ts > max_timestamp:
            max_timestamp = ts
            max_timestamp_string = date

    return max_timestamp_string
