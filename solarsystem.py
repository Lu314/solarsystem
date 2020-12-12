import sys
sun_Distance = float(93000000)
moon_Distance = float(238900)
iss_Distance = float(250)

distanceSun2Moon = sun_Distance - moon_Distance
distanceIss2Moon = moon_Distance - iss_Distance
def Solarsystemfunction():
    user_FirstAnswer = input(
        "Would you like to know how far the Earth is to the Sun?").lower()
    if user_FirstAnswer == "yes":
        print("The distance is", sun_Distance,
              "million miles from planet Earth!")
    elif user_FirstAnswer == "no":
        print("no more questions, have a nice day") sys.exit(status)
    else:
        print("please enter yes or no")
Solarsystemfunction()
user_SecondAnswer = input(
    "Do you want to know the distance in Kilometers and Meters?").lower()
if user_SecondAnswer == "yes":
    print("The distance of the Sun in Kilometers is", sun_Distance * 1.6,
          "and", sun_Distance * 1609, "in Meters")
elif user_SecondAnswer == "no":
    print("no more questions, have a nice day")
else:
    print("please enter yes or no??")
user_ThirdAnswer = input(
    "Do you want to know the distance of the International Space Station?"
).lower()
if user_ThirdAnswer == "yes":
    print("The distance of the ISS is", iss_Distance, "Miles")
elif user_ThirdAnswer == "no":
    print("no more questions, have a nice day")
else:
    print("please enter yes or no")
user_FourthAnswer = input(
    "Do you want to know the distance between the ISS and the Moon in feet?"
).lower()
if user_FourthAnswer == "yes":
    print("The distance is", (moon_Distance - iss_Distance) * 5280, "feet.")
elif user_FourthAnswer == "no":
    print("no more questions, have a nice day")
else:
    print("please enter yes or no")
user_FithAnswer = input(
    "Do you want to know the distance between the ISS and the Sun").lower()
if user_FithAnswer == "yes":
    print("The distance between the Sun and the ISS is",
          sun_Distance - iss_Distance, "million Miles")
elif user_FithAnswer == "no":
    print("no more questions, have a nice day")
else:
    print("please enter yes or no")
user_SixthAnswer = input(
    "Do you want to know the distance between the ISS and the Sun in inches??"
).lower()
if user_SixthAnswer == "yes":
    print("The distance between the ISS and the Sun in inches is",
          sun_Distance - iss_Distance * 63360, "inches")
elif user_SixthAnswer == "no":
    print("no more questions, have a nice day")
else:
    print("please enter yes or no")