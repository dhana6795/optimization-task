import math
hours = 0
capacity = 0
units = {
    'l':10,
    'xl':20,
    '2xl':40,
    '4xl':80,
    '8xl':160,
    '10xl':320
}

location_cost = {
    
    'new_york': {
        'l':120,
        'xl':230,
        '2xl':450,
        '4xl':774,
        '8xl':1400,
        '10xl':2820
    },
    'india': {
        'l':140,
        '2xl':413,
        '4xl':890,
        '8xl':1300,
        '10xl':2970
    },
    'china': {
        'l':110,
        'xl':200,
        '4xl':670,
        '8xl':1180
    }
}

def find_low_cost_machine(unit_price,cost_per_unit,desired_capacity):
    min_cost_per_unit = min(cost_per_unit.values())
    min_machine = (cost_per_unit.keys()[cost_per_unit.values().index(min_cost_per_unit)])
    number_of_min_machine_needed = desired_capacity / units[min_machine]
    if(number_of_min_machine_needed is 0):
        cost_per_unit.pop(min_machine)
        return find_low_cost_machine(unit_price,cost_per_unit,desired_capacity)
    else:
        return number_of_min_machine_needed, min_machine, number_of_min_machine_needed * units[min_machine]

def roundup(x):
    return int(math.ceil(x / 10.0)) * 10

def main():
    print "Hello There Welcome!!! please give the inputs of the capacity and time for the machines to find out the feasible solution"
    capacity = input("Enter the Capacity\n")
    hours = input("Enter the number of Hours\n")
    capacity = capacity / hours
    capacity = roundup(capacity) # to fit into machine units rounding the capacity
    output = []
    try:
        for location in location_cost:
            location_price = location_cost[location]
            cost_per_unit = dict([(x,float(y)/units[x]) for x,y in location_price.items()])
            achieved_capacity = 0
            remaning_capacity = capacity
            machines = []
            price = 0
            
            while(achieved_capacity < capacity):
                number_of_min_machine_needed, min_machine,achieved_capacity_now = find_low_cost_machine(location_price,cost_per_unit,remaning_capacity)
                machines.append((min_machine, number_of_min_machine_needed))
                remaning_capacity -= achieved_capacity_now
                achieved_capacity += achieved_capacity_now
                price += number_of_min_machine_needed * location_price[min_machine]
            
            output.append({'region':location,
                'total_cost': '$'+ str(price),
                'machines': machines
                })
        print "Here is the Solution:" 
        print output
        return output
    except Exception as e:
        print "something went wrong!"
        print "Please Tell the author you got the exception also make sure you given the input in the Number"
        print e

    
if __name__ == "__main__":
    main()

    
    


