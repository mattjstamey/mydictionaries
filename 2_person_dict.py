person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)

print(f"The name of the second child is {person['children'][1]}")

for i in person['children']:
    print(i)

for i, j in person['pets'].items():
    print(f"Type of pet:{i} name of pet: {j}")
