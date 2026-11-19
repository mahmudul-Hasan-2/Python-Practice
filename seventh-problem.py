# List of grades across multiple subjects
grades = [85, 90, 78, 92, 88]

total = 0
count = 0

# Iteration and aggregation logic
for grade in grades:
    total += grade
    count += 1

# Calculate average
average = total / count

print("Total Marks:", total)
print("Average Grade:", average)
