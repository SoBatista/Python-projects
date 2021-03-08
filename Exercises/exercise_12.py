
def days_months(arg):
    if arg == "jan" or arg == "mar" or arg == "may" or arg == "jul" or arg == "aug" or arg == "oct" or arg == "dec":
        print 31
    elif arg == "apr" or arg == "jun" or arg == "sep" or arg == "nov":
        print 30
    elif arg == "feb":
        print 28
    else:
        print "Value Error"


arg = raw_input("Give me a month: ")
days_months(arg)
    
    
