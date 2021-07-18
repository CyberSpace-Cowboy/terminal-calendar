# Terminal Calendar

This is a very trivial calendar app that works inside a terminal/command prompt, I wrote it in less than 15 minutes using Python.

## Implementation 

It's implemented in the most trivial way possible:

1. We just import calendar module to access the calendar
2. Also from datetime module we import date to see what day it is today 
3. Then we get to choose the view: 'by year' or 'by month'
4. If we type 'by year' we are asked to type the year of the calendar (yyyy format) and after typing a year we see the full calendar of that year, we also see today's date at the bottom
5. If we type 'by month' we are also asked to type the year of the calendar but after typing a year we are then asked to type the number of the month, and after that we get the calendar for that specific month, and again we also see today's date at the bottom
6. After outputing the calendar, you're always asked if you wanna contrinue - (y/n)
7. If you type 'n' you exit the program, if you type 'y' you get to choose the parameters of the calendar again

To run this stupid little program you should open the terminal at the same directory as your Calendar.py program, and then type:
```
python Calendar.py  
```

It's extremely trivial, but it works.
