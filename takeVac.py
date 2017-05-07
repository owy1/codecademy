
#write a trip expenditure in Python

def hotel_cost(nights):
    return 140 * nights
    
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    if city == "Tampa":
        return 220
    if city == "Pittsburgh":
        return 222
    if city == "Los Angeles":
        return 475

def rental_car_cost(days):
    rental_cost = 40 * days
    if days >= 7:
	    rental_cost -=50
    elif days >= 3:
		rental_cost -= 20
    return rental_cost

def trip_cost(city, days, spending_money):
    return hotel_cost(days) + spending_money + \
    plane_ride_cost(city) + rental_car_cost(days)

print trip_cost("Los Angeles", 5, 600)
