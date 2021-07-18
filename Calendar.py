#Python Terminal Calendar
import calendar
from datetime import date


print("				    Basic Terminal Calendar")

def Show_Calendars():
	while(True):
		print("""
				Choose the View:

			To view by year type in: by year
			To view by month type in: by month
		""")
		view = input(" Type in the view: ").lower()

		if view == "by year":
			year = int(input("\n Type the year of the calendar: "))
			print(calendar.calendar(year))

		elif view == "by month":
			year = int(input("\n Type the year of the calendar: "))
			month = int(input("\n Type a number of the month: "))
			print("\n" + calendar.month(year, month))

		#TODAY
		today = date.today()
		d = today.strftime("%B %d, %Y")
		print("Today is", d)

		#Continue?
		ask = input("\n Wanna Continue? (y/n): ")
		if ask == "y":
			continue
		elif ask == "n":
			exit()
		

if __name__ == '__main__':
      
    # main method for executing
    # the functions
    Show_Calendars()



