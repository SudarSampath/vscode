import re

a_lines = []
x_y_z_lists = []
y_coordinates = []
index_no = []
y_value=[]
indices_under_10 = []
Output_list = []
coordinates_as_int = []
Final_coor = []
original_index_asc=[]

input("Press Enter If pasted the MOVL points generated from sprutcam into the input.txt file : ")


# Open the file in read mode
with open('output.txt', 'r') as file:
    # Loop through each line in the file
    for line in file:
        
        stripped_line = line.strip()

        a_lines.append(stripped_line)
        
x=(len(a_lines))

for i in range(x):
 txt = a_lines[i]
 
 y_txt = re.findall(r'\[.*?\]', txt)[0]


 y_txt_cleaned = y_txt.replace('[', '').replace(']', '')


 y_coordinates = y_txt_cleaned.split(',')

 x_y_z_lists.append(y_coordinates)



coordinates = x_y_z_lists

for coord in coordinates:
    y_coordinates.append(coord[0])

del y_coordinates[0:3]



coordinates_as_int = [float(coord) for coord in y_coordinates]
coordinates_as_int = [int(coord) for coord in coordinates_as_int]




coordinates = coordinates_as_int



original_indices = {coord: index for index, coord in enumerate(coordinates)}

print(original_indices)

sorted_coordinates = set(coordinates)



for index, coord in enumerate(sorted_coordinates):
    original_index = original_indices[coord]
    original_index_asc.append(original_index)


original_index_asc = sorted(original_index_asc)
print(original_index_asc)


for z in original_index_asc:
       result = [a_lines[z]]
       Output_list.append(result)

length = len(Output_list)

with open("output_final_sorted.txt", "w") as file:
     for i in range(length):
       
       current_var = Output_list[i]
       
       char_to_remove_ = "'"
       
       current_var = str(current_var)

       modified_string = current_var.replace(char_to_remove_, "")

       modified_string = modified_string[1:]

       file.write(str(modified_string) + "\n")
    



