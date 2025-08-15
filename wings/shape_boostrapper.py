import os
import re
import numpy as np
import random

shape_folder = "Shapes"
out_folder = "Shapes/Shapes_bootstrap"
clones = 100
noise_range = (-10, 10)

#create output folder
os.makedirs(out_folder, exist_ok = True)

#helper function, randomizes point placement
def noisemaker(line):
    #make sure we modify the right lines
    parts = line.strip().split()
    if len(parts) != 3:
        return line
    #extract each landmark
    try:
        landmark = int(parts[0])
        x_pixel = int(parts[1])
        y_pixel = int(parts[2])
    #add random noise to simulate digitization error
        x_pixel += random.randint(*noise_range)
        y_pixel += random.randint(*noise_range)
        return f"{landmark}\t{x_pixel}\t{y_pixel}"
    #skip lines that aren't numeric
    except ValueError:
        return line
    
#grab existing shapefiles, modify them
for filename in os.listdir(shape_folder):
    if not filename.endswith(".txt"):
        continue
    path = os.path.join(shape_folder, filename)

    with open(path, "r") as f:
        original_lines = f.readlines()

    for i in range(clones):
        new_lines = []
        for line in original_lines:
            if not line.strip().startswith("<") and line.strip():
                new_line = noisemaker(line)
                new_lines.append(new_line + "\n")
            else:
                new_lines.append(line)

        base_name = os.path.splitext(filename)[0]
        out_name = f"{base_name}_clone{i+1:02d}.txt"
        out_path = os.path.join(out_folder, out_name)

        with open(out_path, "w") as out_file:
            out_file.writelines(new_lines)

print(f"Bootstrapped {clones} versions of each wing!")