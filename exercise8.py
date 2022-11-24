#schedule greeting 

time = input ( "enter the timer")

try:
    time_int = int(time)

    if time_int >= 0 and time_int <= 11:
        print("Good Morning")
    elif time_int >= 11 and time_int <=17:
        print("Good Efternoon")
    elif time_int >=18 and time_int <=22 :
        print("Good Ninght") 
    else:
        print("I don't know this time")

except:
    print("enter an integer")