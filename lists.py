# Your code below:
first_names = ["Ainsley", "Ben", "Chani", "Depak"]

preferred_size = ["Small", "Large", "Medium"]
preferred_size.append("Medium")
print(preferred_size)

customer_data = [["Ainsley", "Small", True], ["Ben", "Large", False], [
    "Chani", "Medium", True], ["Depak", "Medium", False]]
print(customer_data)

customer_data[2][2] = False
print(customer_data)

customer_data[1].remove(False)
print(customer_data)

customer_data_final = customer_data + \
    [["Amit", "Large", True], ["Karim", "X-Large", False]]
print(customer_data_final)

temperatures = [1, 2, 3, 4, 5, 6]
temperatures_adjusted = [temp + 20 for temp in temperatures]

temperatures = [1, 2, 3, 4, 5, 6]
temperatures_adjusted = [(temp - 32) * 5/9 for temp in temperatures]

xy = [[1, 3], [2, 4], [3, 3], [4, 2]]
z = [x * y for (x, y) in xy]
print(z)

# exercise

capitals = ["Santiago", "Paris", "Copenhagen"]
countries = ["Chile", "France", "Denmark"]

combined = zip(capitals, countries)
locations = [capital + ", " + countries for (capital, countries) in combined]
print(locations)