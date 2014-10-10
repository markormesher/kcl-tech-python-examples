# three string inputs
num_people = raw_input("How many people are at the event? ")
num_pizzas = raw_input("How many pizzas did you order? ");
slices_per_pizza = raw_input("How many slices does each pizza have? ")

# convert to numbers and calculate
total_slices = int(num_pizzas) * int(slices_per_pizza)
slices_each = total_slices / float(num_people)

# output
print("Each person should get " + str(slices_each) + " slice(s) of pizza.")
