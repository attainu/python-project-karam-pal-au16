# imorting function and class from differnt directories to use them in the main
from driver_info_provider import Driver
from location_finder import distance
from welcoming import Booking
from rider_info_provider import Rider
from endTrip import destination

# this is a process to access all the given code
if __name__ == "__main__":
    pilot = Driver()
    sawari = Rider()  # instances to access

   # gathering information of drivers
    numDriver = int(input("Enter no of Drivers: "))
    for _ in range(numDriver):
        name = input("Please Add your Name:   ")
        cabno = input("Please add your Cab no:   ")
        contact = input("Provide Your 10digit Mobile Number:  ")
        available = input("Press <yes> if you are Available else <no>:  ")

    # taking drivers location and storing all the information in array
        print("Provide Your Location Coordinate:  ")
        x1 = int(input("Type Your x Cordinate:  "))
        y1 = int(input("Type Your y Cordinate:  "))
        drivers = pilot.driver_info(
            name, cabno, contact, available, x1, y1)  # storing in dict
        print("Your Details Are", drivers)

    # taking and storing information from rider for booking
    name = input("Type Your Rider Here:   ")
    location = input("Whats is your city:   ")
    phone_no = input("Your Mobile Number Please:   ")
    booking = input("Type <yes> if you want to book a ride:  ")
    x2 = int(input("Type your x Cordinate:  "))
    y2 = int(input("Type your y Cordinate:  "))
    rider = sawari.register_rider(
        name, location, phone_no, booking, x2, y2)  # storing into dict
    print("Your Details:", rider)

    # history of both rider and driver for making data of history to display
    alldrivers = pilot.getDriverslist()
    allriders = sawari.historyofrides()

    while True:  # for implement function infinite times

        # prints are for information for next steps
        print("If you want to see the list of all Drivers and Riders type <check>:   ")
        print("If you want exit Write <EXIT>:   ")
        print("If you want to Book a Cab type <bookme>:   ")

        # to take the rider input
        entry = input("Provide Your Input here:::   ")

        if entry == "check":  # for list data of drivers
            print(alldrivers, allriders)

        if entry == "EXIT":  # for exit we using this function
            continue

        if entry == "bookme":  # to know if the rider wants to book or not
            print(" THANKS!!   For Booking with us , Please provide your destination:")
            d1 = int(input("please enter x Coordinate:  "))
            d2 = int(input("please enter y Coordinate:  "))
        
           # to calculate the distance between driver and rider
            distanceArr = 100000000000000000000000
            selctedCab = None
            for i in range(len(alldrivers)):
                d = distance(alldrivers[i]["x1"], alldrivers[i]
                             ["x2"], allriders[0]["y1"], allriders[0]["y2"])
                print("These are the Available  DRIVERS  ",
                      alldrivers[i]['name'], "at a Distance of ", d,"km")
                if d < distanceArr:
                    distanceArr = d
                    selctedCab = alldrivers[i]
            print(" so this cab ", selctedCab, "is coming to PICK YOU UP ! ")
        
            print("HAPPY JOURNEY")

            #to calculate the fare of the trip
            price_per_km = 9
            for j in range(len(allriders)):
                l = destination(allriders[0]["y1"], allriders[0]['y2'],d1, d2)
                print("Please Pay the Driver",price_per_km*l,"RUPEES")
            break

        
