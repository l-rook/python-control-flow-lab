# Exercise 1: Vowel or Consonant
def check_letter():
    letter = input("Enter a letter: ").lower()
    if letter.isalpha() and len(letter) == 1:
        if letter in "aeiou":
            print(f"The letter {letter} is a vowel.")
        else:
            print(f"The letter {letter} is a consonant.")
    else:
        print("Invalid input. Please enter a single alphabetical letter.")

# Call the function
check_letter()

# Exercise 2: Old enough to vote?
def check_voting_eligibility():
    try:
        age = int(input("Please enter your age: "))
        if age < 0:
            print("Age cannot be negative.")
        else:
            voting_age = 18
            if age >= voting_age:
                print("You are eligible to vote.")
            else:
                print("You are not eligible to vote.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Call the function
check_voting_eligibility()

# Exercise 3: Calculate Dog Years
def calculate_dog_years():
    try:
        age = int(input("Input a dog's age: "))
        if age < 0:
            print("Age cannot be negative.")
        elif age == 1:
            dog_years = 10
        elif age == 2:
            dog_years = 20
        else:
            dog_years = 20 + (age - 2) * 7
        print(f"The dog's age in dog years is {dog_years}.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Call the function
calculate_dog_years()

# Exercise 4: Weather Advice
def weather_advice():
    is_cold = input("Is it cold? (yes/no): ").strip().lower()
    is_raining = input("Is it raining? (yes/no): ").strip().lower()

    if is_cold == "yes" and is_raining == "yes":
        print("Wear a waterproof coat.")
    elif is_cold == "yes" and is_raining == "no":
        print("Wear a warm coat.")
    elif is_cold == "no" and is_raining == "yes":
        print("Carry an umbrella.")
    elif is_cold == "no" and is_raining == "no":
        print("Wear light clothing.")
    else:
        print("Invalid input. Please answer 'yes' or 'no'.")

# Call the function
weather_advice()

# Exercise 5: What's the Season?
def determine_season():
    month = input("Enter the month of the year (Jan - Dec): ").capitalize()
    try:
        day = int(input("Enter the day of the month: "))
        
        if month in ("Dec", "Jan", "Feb", "Mar"):
            if (month == "Dec" and day >= 21) or (month == "Mar" and day <= 19) or month in ("Jan", "Feb"):
                season = "Winter"
        if month in ("Mar", "Apr", "May", "Jun"):
            if (month == "Mar" and day >= 20) or (month == "Jun" and day <= 20) or month in ("Apr", "May"):
                season = "Spring"
        if month in ("Jun", "Jul", "Aug", "Sep"):
            if (month == "Jun" and day >= 21) or (month == "Sep" and day <= 21) or month in ("Jul", "Aug"):
                season = "Summer"
        if month in ("Sep", "Oct", "Nov", "Dec"):
            if (month == "Sep" and day >= 22) or (month == "Dec" and day <= 20) or month in ("Oct", "Nov"):
                season = "Fall"

        print(f"{month} {day} is in {season}.")
        
    except ValueError:
        print("Invalid input. Please enter a valid day.")

# Call the function
determine_season()
