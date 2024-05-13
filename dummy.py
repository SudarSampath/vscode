
"""Sort_lines = set(a_lines)

print(Sort_lines)

y = len(Sort_lines)

print (y)"""


# Define your coordinates
coordinates = [(3, 4), (1, 2), (5, 6), (3, 8), (5, 9)]

# Sort the coordinates based on x-values and get the indices
sorted_indices = sorted(range(len(coordinates)), key=lambda i: coordinates[i][0])

# Now, sorted_indices contains the indices of the coordinates after sorting
print("Indices after sorting:")
for index, coord_index in enumerate(sorted_indices):
    print(f"Index {index} corresponds to coordinate {coordinates[coord_index]}")
