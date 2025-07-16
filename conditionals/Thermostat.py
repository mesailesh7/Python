device_status = "active"

temperature = 38

if device_status == "active":
    if temperature > 35:
        print("High temperature alert!")
    else:
        print("temperate is normal")
else:
    print("device is offline")
