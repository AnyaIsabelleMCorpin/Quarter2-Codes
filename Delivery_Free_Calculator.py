#Define function for delivery fee

def calculate_delivery_fee(distance, rate):
    total_fee = distance*rate
    return total_fee

#Ask for inputs
distance = float(input("Enter distance in kilometers: "))
rate = float(input("Enter rate per kilometer (₱): "))

#Calculate total delivery fee
fee = calculate_delivery_fee(distance, rate)

#Show results
print(f"Total Delivery Fee: {fee:.2}")