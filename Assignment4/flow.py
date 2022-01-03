import csv

base = []

value = 5

for i in range(21):
    base.insert(i, value)
    value -= .5

all_x = []
all_y = []

index = 0
for num1 in base:
    for num2 in base:
        all_x.insert(index,  num1)
        all_y.insert(index, (num1 * (-1 * num2)))

x_positions = []
y_positions = []
for i in range(21):
    for j in range(21):
        x_positions.insert(j + (i * 21), (i * 46) + 40)
        y_positions.insert(j + (i * 21), (j * 46) + 40)

list_of_dics = []
for i in range(441):
    new_dict = {}
    new_dict["x"] = all_x[i]
    new_dict["y"] = all_y[i]
    new_dict["xpos"] = x_positions[i]
    new_dict["ypos"] = y_positions[i]
    list_of_dics.insert(i, new_dict)

for row in list_of_dics:
    print(row)

keys = list_of_dics[0].keys()

with open('country.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(list_of_dics)
