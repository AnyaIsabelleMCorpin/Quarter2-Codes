 #Function for basic charge

def calculate_bill(kWh):
    basic_charge = 50

#Determin rate per kWh
    if kWh <=100:
        rate = 5
        surcharge = 0
    elif kWh >=101 and kWh <=200:
        rate = 7
        surcharge = 0
    elif kWh >=201 and kWh <=500:
        rate = 10
        surcharge = 0
    else:
        rate = 12
        surcharge = 500

#Calculate total bill
    total = (kWh * rate) + basic_charge + surcharge
    return total

#Ask for inputs
kWh_used = float(input("Enter the number of kilowatt hours used: "))
bill = calculate_bill(kWh_used)

#Display output
print(f"Total Electricty Bill: ₱{bill:.2f}")