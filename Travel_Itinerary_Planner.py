destinations = []

print("Please enter your 5 travel destinations: ")

for i in range(5):
    place = input(f"Destination {i + 1}: ")
    destinations.append(place)

print("Original Travel itinerary: ")

for i in range(len(destinations)):
    print(f"{i + 1}. {destinations[i]}")

while True:
    redo = input("Would you like to replace another destination? (Yes/No): ").lower()

    if redo == "no":
        break
    elif redo == "yes":
        choice = int(input("\nWhich destination number would you like to replace? "))
    
        if 1 <= choice <=5:
            new_place = input ("Enter new destination: ")
            destinations[choice -1] = new_place
        else:
            print("Error! Please choose number from 1 to 5.")
    else:
        print("Please enter Yes or No. ")

print("\nUpdated Travel Itinerary: ")
for i in range(len(destinations)):
    print(f"{i + 1}. {destinations[i]}")