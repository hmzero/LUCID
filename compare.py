import os
import sys
from analyze import analyze 
import re
import time

# Path to the folder containing the files
folder_path = sys.argv[1]

# Get a list of all files in the folder
files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# Initilize catagories list
catList = ["advantages", "approach", "materials", "metrics", "problem", "processes"]

# Initialize the grid as a nested dictionary
results_grid = {cat:{file1: {file2: float for file2 in files} for file1 in files} for cat in catList} 
results_tracker = {}

# Populate the grid with the results of compare_files
for file1 in files:
    for file2 in files:
        if file1 != file2 and (file2,file1) not in results_tracker:
            results_tracker[(file2,file1)] = 1
            result = analyze(os.path.join(folder_path, file1), os.path.join(folder_path, file2))
            pattern = r"(\w+):\s([0-9]+)"
            matches = re.findall(pattern, result)
            print(result)
            print(matches)
            for cat, value in matches:
                if cat in catList:
                    results_grid[cat][file1][file2] = int(value)*0.01
                    results_grid[cat][file2][file1] = int(value)*0.01
            time.sleep(32)
        elif file1 == file2:
            for cat in catList:
                results_grid[cat][file2][file1] = 1


# Print the grid in a readable format
print("Comparison Results Grid:")
header = "\t" + "\t".join(files)

for cat in catList:
    print(cat)
    print(header)
    for file1 in files:
        row = [results_grid[cat][file1][file2] for file2 in files]
        print(f"{file1}\t" + "\t".join(map(str, row)))

# Save results to a file (optional)
with open("comparison_results.txt", "w") as f:
    for cat in catList:
        f.write(cat+"\n")
        f.write(header+"\n")
        for file1 in files:
            row = [results_grid[cat][file1][file2] for file2 in files]
            f.write(f"{file1}\t" + "\t".join(map(str, row))+"\n")