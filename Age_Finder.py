# **************************** Birthdate Predictor ************************888

# Importing Library
from datetime import datetime

# This will track all the activities in the record.txt file
def login(msg):
    global name
    with open("record.txt", "a") as f:
        f.write(f"{name.capitalize()} has {msg} on {datetime.now()}\n")

# This will find the future birthdate
def age():
    future_age = 2021 - int(age_birth) + user_input
    print(f"\n{name} will be {user_input} year old in the year {str(future_age)}")

# This will validate whether any restriction is crossing or everything is fine
def birth():
    row = age_birth[-4:]
    if int(row) < 2021 and int(row) >= 1900:
        if int(age_birth[0:2]) < 32 and int(age_birth[2:4]) < 13:
            future_age = int(row) + user_input
            print(f"\n{name} will be {user_input} year old on {age_birth[0:2]}/{age_birth[2:4]}/{str(future_age)}")
        else:
            print("\nSorry...! Invalid birth date Input Occur...! Please try again...!")
    else:
        print("\nSorry ...! Your age can't be greater than 150 and lesser than and 0...!")
        exit()

if __name__ == '__main__':
    
    try:
        name = str(input("\nEnter your name:"))
        age_birth = str(input(f"\n{name} enter your age (EX. 18) or date of birth (19092002):"))
        user_input = int(input(f"\n{name} enter the years to see your birth date in future (EX. 100):"))
        
        if len(age_birth) <= 3:
            if int(age_birth) > 0 and int(age_birth) < 150:
                age()
            else:
                print(f"Sorry ...! {name} age can't be greater than 150 and lesser than and 0...!")
                exit()
    
        elif len(age_birth) == 8:
            birth()
    
        else:
            print("Invalid input...! Please try again with a valid input...!")
    
        login("Login in the age finder software")
    
    except Exception as E:
        print('Something wents wrong: ', E)
    
    finally:
        print(f'Thank You {name} for your valuable time, meet you soon...!')
