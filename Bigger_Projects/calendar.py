from time import sleep, strftime
user_name = "Batista Dev"

calendar = {
}

def welcome():
  print "Welcome" + user_name
  print "The calender will open"
  sleep(1)
  print "Today is: " + strftime("%A %B %d, %Y")
  print "The time is: " + strftime("%H : %M : %S")
  sleep(1)
  print "What would you like to do?"

def start_calendar():
  welcome()
  start = True
  while True:
    user_choice = raw_input("Enter A to Add, U to Update, V to View, D to Delete, X to Exit: ")
    user_choice = user_choice.upper()
    if user_choice == "V":
      if len(calendar.keys()) < 1:
        print "Calendar empty"
      else:
        print calendar
    elif user_choice == "U":
      date = raw_input("What date? ")
      update = raw_input("Enter the update: ")
      calendar[date] = update
      print "update was been successful!"
      print calendar
    elif user_choice == "A":
      event = raw_input("Enter event: ")
      date = raw_input("Enter date (MM/DD/YYYY): ")
      if (len(date) > 10 or int(date[6:]) < int(strftime("%Y"))):
        print "That's an invalid date!"
        try_again = raw_input("Try Again? Y for Yes, N for No: ")
        try_again = try_again.upper()
        if try_again == Y:
          continue
        else:
          start = False
      else:
        calendar[date] = event
        print "The event as been successfully added!"
        print calendar
    elif user_choice == "D":
      if len(calendar.keys()) < 1:
        print "The calendar is empty!"
      else:
        event = raw_input("What event? ")
        for date in calendar.keys():
          if event == calendar[date]:
            del calendar[date]
            print "The event was successfully deleted!"
            print calendar
          else:
            print "An incorrecting event was specified!"
    elif user_choice == "X":
      satart = False
      return 0
    else:
      print "You entered an invalid command!"
      return 0
start_calendar()
