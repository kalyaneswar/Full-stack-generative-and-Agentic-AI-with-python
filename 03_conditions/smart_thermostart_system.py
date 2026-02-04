device_status = input("is device active or inactive: ").lower()
temperature = int(input("Please enter temp: "))

if device_status == "active":
    if  temperature > 35:
        print("Warn!: High temperature alert")
    else: 
        print("Temperature is Normal")
    
else:
    print("Device is offline")
    

