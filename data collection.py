def gravitycalc():
    distanceFromEarth = int(input("what is the distance between the object and the earth"))
    print("collecting data...")

    TheSpeedOfObject= int(input("what is the speed of the Object"))
    print("collecting data...")

    gravity = distanceFromEarth + TheSpeedOfObject
    print(F"so the gravity of the object is {gravity}")

def speedcalc():
    distance = int(input("the distance of the object"))
    print("collecting data...")
    time = int(input("the time of the object"))
    print("collecting data...")
    speed = distance / time
    print(f"the speed is {speed}")
    

q1 = str(input("do you want the speed calc or gravity calc"))


if q1 == "gravity calc":
    gravitycalc()

elif q1 == "speed calc":
    speedcalc()