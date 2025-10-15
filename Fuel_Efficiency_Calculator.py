#Define fucntion for fuel efficiency

def calculate_fuel_efficiency(distance, fuel):
    output = distance/fuel
    return output

#Ask for inputs
distance = float(input("Enter distance traveled (in kilometers): "))
fuel = float(input("Enter fuel consumed (in liters): "))

#Calculate fuel efficiency
total = calculate_fuel_efficiency(distance, fuel)

#Show results
print(f"Fuel Efficiency: {total:.2f} km/L")