# Solve the following problem:
# Write a function to calculate the number of seconds in a week

# Write code here

def seconds_in_week():
    a = 60 # Secs in minute
    b = 60 * a # secs in an hour
    c = 24 * b # secs in a day
    d = 7 * c # secs in a week
    result = d
    return(result)

print(seconds_in_week())
