speed = 60 
car_location = 90

RADAR_1 = 60
LOCATION_2 = 100
RADAR_RANGER = 1

speed_car = speed > RADAR_1 
fined = car_location >= (LOCATION_2 - RADAR_RANGER) and car_location<= (LOCATION_2 + RADAR_RANGER)
if speed_car:
    print ("print radar")

if fined and speed_car:
    print("car speed")
