from driver_registration import Driver
from thegapsin_between import distance
from welcoming import Greetings
from rider_registration import Rider
from tripconclusion import desired_location

# this is a process to access all the given code
if __name__ == "__main__":
    karam = Driver()
    ginger = Rider()  # instances to access
   # to register the drivers

    Driverbhai = int(input("Enter no of Drivers: "))

    for k in range(Driverbhai):

        name = input("Please Add your Name:   ")

        cabno = input("Please add your Cab no:   ")

        contact = input("enter Your  Mobile Number:  ")

        available = input("Press <yes> if you are Available else <no>:  ")

        print("enter Your Location Coordinate:  ")

        x1 = int(input("Type Your x Cordinate:  "))

        x2 = int(input("Type Your y Cordinate:  "))

        drivers = karam.driver_info(
            name, cabno, contact, available, x1, x2) 

        print("Your Details Are", drivers)

    # taking and storing information from rider for booking

    name = input("Type Your Name Here(rider):   ")

    location = input("Whats is your city:   ")

    phone_no = input("Your Mobile Number Please:   ")

    booking = input("Type <yes> if you want to book a ride:  ")

    if available == "no":
        print("sorry driver is not avaialble for booking")

    y1 = int(input("Type your x Cordinate:  "))

    y2 = int(input("Type your y Cordinate:  "))

    rider = ginger.register_rider(
        name, location, phone_no, booking, y1, y2)  # storing into dict
    print("Your Details:", rider)

    # history of both rider and driver for making data of history to display
    alldrivers = karam.getDriverslist()
    allriders = ginger.historyofrides()

    print("If you want to Book a Cab type <modi>:   ")

    # to take the rider input
    entry = input("Provide Your Input here:::   ")

    if entry == "check":  # for list data of drivers
        print(alldrivers, allriders)

    if entry == "modi":  # to know if the rider wants to book or not
        print(" THANKS!!   For Booking with us , Please enter your the location you want to go:")
        d1 = int(input("please enter x Coordinate:  "))
        d2 = int(input("please enter y Coordinate:  "))

        # to calculate the distance between driver and rider
        distanceArr = 99999999999999999
        assigned_Cab = None
        for i in range(len(alldrivers)):
            d = distance(alldrivers[i]["x1"], alldrivers[i]
                         ["x2"], allriders[0]["y1"], allriders[0]["y2"])
            print("This driver ", alldrivers[i]
                  ['name'], "is", d, "KM from you")
            if d < distanceArr:
                distanceArr = d
                assigned_Cab = alldrivers[i]
        print(" as this driver is close so ", assigned_Cab,
              "will reach your location   shortly to pick you up ")
        print("have a safe journey!!")

        # code for calculating the cost of trip
        ppk = 2
        for j in range(len(allriders)):
            l = desired_location(
                allriders[0]["y1"], allriders[0]['y2'], d1, d2)
            print("your destination has arrived!!")

            print("please pay Rs.", l*ppk)
    while True:  # for implement function infinite times
        # prints are for information for next steps

        print("If you want to see the history of all your Rides type <check>:   ")
        print("If you want exit Write <EXIT>:   ")
    

        # to take the rider input
        entry = input("Provide Your Input here:::   ")

        if entry == "check":  # for list data of drivers
            print(allriders)

        if entry == "EXIT":  # for exit we using this function
            print("hope you had a pleasant journey, visit again!!")
            break