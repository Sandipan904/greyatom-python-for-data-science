# --------------
# Code starts here

# Create the lists 
class_1 = ['Geoffrey Hinton' , 'Andrew Ng' , 'Sebastian Raschka' ,'Yoshua Bengio']
class_2 = ['Hilary Mason' , 'Carla Gentry' , 'Corinna Cortes']
print(class_1)
print(class_2)
# Concatenate both the strings
new_class = class_1 + class_2
print(new_class)

# Append the list
new_class.append('Peter Warden')
print(new_class)

# Remove the element from the list
new_class.remove('Carla Gentry')
# Print the list
print(new_class)


# Create the Dictionary
courses = {"Math" :65 ,"English" :70 ,"History" : 80 ,"French" : 70 , "Science": 60}
print(courses)
mathematics = {'Geoffrey Hinton' : 78,'Andrew Ng' : 95 , 'Sebastian Raschka' : 65 , 'Yoshua Benjio' : 50, 'Hilary Mason' : 70 ,'Corinna Cortes' : 66 , 'Peter Warden': 75}
print(mathematics)


# Slice the dict and stores  the all subjects marks in variable
values = courses.values()
total = sum(values)
print(total)
# Store the all the subject in one variable `Total`

# Print the total
print(total)
# Insert percentage formula
percentage = 345 / 500 * 100
# Print the percentage
print(percentage)



# Create the Dictionary
topper = max(courses, key = courses.get)
print(topper)



# Given string


# Create variable first_name 
first_name = "Andrew"
print(first_name)
# Create variable Last_name and store last two element in the list
Last_name = "NG"
print(Last_name)
# Concatenate the string
full_name = Last_name + " " + first_name
# print the full_name
print(full_name)

# print the name in upper case
certificate_name = full_name.upper()
print(certificate_name)
# Code ends here


