parcel_code =  ["damaged", "stop", "continue"]

for i in parcel_code:
    if i == "damaged":
        print("Skipped damaged parcel")
        continue
    # if i == "stop":
    #     print("Critical error: stopping scan")
    #     breakx
    if i == "continue":
        print(f"scanned parcel {i}")
else:
    print("All parcels scanned successfully")

