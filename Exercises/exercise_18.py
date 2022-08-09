sec=int(input("Enter a number of seconds for you to know the days, hours, minutes and seconds that correspond to that number: "))
def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%d:%02d:%02d" % (hour, minutes, seconds)
      
# Driver program
print(convert(sec))
