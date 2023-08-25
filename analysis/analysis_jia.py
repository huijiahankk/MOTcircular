from psychopy import data
import numpy as np

# Load the data
filename = '/Users/huijiajia/Documents/matlab/MOTcircular/dataRaw/hjh_15Aug2023_22-14.tsv'  # Path to the text file
all_data = data.importConditions(filename)

# Extract 'orderCorrect' column
order_correct_values = [trial['orderCorrect'] for trial in all_data]

# Calculate the percentage of values that are '3'
percentage = np.mean([value == 3 for value in order_correct_values]) * 100

print(f"The percentage of '3' values in the 'orderCorrect' column is: {percentage:.2f}%")
