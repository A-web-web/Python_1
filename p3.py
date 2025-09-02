# The sorted list to search within
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# The element to search for
target_element = 1

# Initialize the search boundaries
low = 0
high = len(a) - 1
found = False
index = -1

# Perform the binary search
while low <= high:
    mid = (low + high) // 2  # Calculate the middle index

    if a[mid] == target_element:
        found = True
        index = mid
        break  # Element found, exit the loop
    elif a[mid] < target_element:
        low = mid + 1  # Search in the right half
    else:
        high = mid - 1  # Search in the left half

# Output the result
if found:
    print(f"Element {target_element} found at index {index}.")
else:
    print(f"Element {target_element} not found in the list.")
  
print("Good luck")