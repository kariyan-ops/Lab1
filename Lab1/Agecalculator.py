import datetime

def calculate_age():
    try:
    	birth_date = int(input("Please enter your birth year: "))
    	current_year = datetime.datetime.now().year
    	age = current_year - birth_date
    	print("Your age is:", age)
    except TypeError:
        print("Please enter an integer.")

def helloWorld():
    print('Hello World')


helloWorld()

