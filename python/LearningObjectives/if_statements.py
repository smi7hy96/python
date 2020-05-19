import time  # import the time library to use more functions
# IF FUNCTIONS

#  Control flow and outcome of code

# Syntax
# if <condition>:
#   outcome

# weather = "Raining"
# weather = "Sunny"
# weather = "Windy"
# weather = "Cloudy"
weather = input("What is the weather today? \n").lower()
safety_alert = 'red'

if weather == "raining":
    time.sleep(2)  # Delay code execution by 2 seconds
    print("Bring Umbrella")
elif weather == "sunny":
    print("Wear Shorts")
elif weather == "windy" and safety_alert == "red":  # Two conditions to meet
    print("Stay at Home!!!!!")
else:
    print("Don't worry about it!")
