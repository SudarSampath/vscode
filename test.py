import re

a_lines = []
x_y_z_lists = []
y_coordinates = []
index_no = []
y_value=[]
indices_under_10 = []
Output_list = []

input("Press Enter If pasted the MOVL points generated from sprutcam into the input.txt file : ")


# Open the file in read mode
with open('input.txt', 'r') as file:
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


#print(x_y_z_lists)

coordinates = x_y_z_lists

for coord in coordinates:
    y_coordinates.append(coord[1])

del y_coordinates[0:3]


   
print(y_coordinates)

for i, value in enumerate(y_coordinates):
    if -40 <= float(value) <= 40:
        indices_under_10.append(i)


To_ava_points = len(indices_under_10)




if To_ava_points == 0:
   print("There is no Y coordinate under the given filename")


if To_ava_points > 0:
      for z in indices_under_10:
       result = [a_lines[z]]
       Output_list.append(result)

      #print("Elements from the other list:", result)


#print(Output_list)
out_nos = len(Output_list)


with open("output.txt", "w") as file:
     for i in range(out_nos):
       
       current_var = Output_list[i]
       
       char_to_remove_ = "'"
       
       current_var = str(current_var)

       modified_string = current_var.replace(char_to_remove_, "")

       modified_string = modified_string[1:]

       file.write(str(modified_string) + "\n")
    


print("Total no of points sorted: ",out_nos)
print("Pls find the sorted MOVL points in the output.txt")