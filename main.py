from turtle import Screen
from group import Group
from member import Member

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Group Generator")

group = Group()

# List of all attendees
list_of_names = []

# List of all member-objects
list_of_members = []

generator_is_on = True

while generator_is_on:
    name = screen.textinput(title="Group Generator", prompt="Enter a name, or 'done' when finished").title()
    if name == 'Done':
        generator_is_on = False
    else:
        list_of_names.append(name)
    # print(list_of_names)


# Number of names
number_of_names = len(list_of_names)
# print(number_of_names)

# Ask the user to set the size of a groups
size_of_groups = screen.numinput(title="Define groups", prompt="Enter the size of groups")
# print(number_of_groups)

# Calculate the number of groups
number_of_groups = round(number_of_names / size_of_groups)
print(number_of_groups)
print(number_of_names)

# Generate as many groups as the user wants
for _ in range(0, number_of_groups):
    new_group = Group()
    print(new_group)

# Generate as many members as names in list_of_names
for name in list_of_names:
    new_member = Member(name)
    list_of_members.append(new_member)
    print(new_member)

# print(list_of_members)


screen.exitonclick()
