def binary_search(arr, target):
    """
    Searches for an element in the array using Binary Search.

    Args:
        arr (list): The list of elements to search.
        target: The value to search for.

    Returns:
        int: The index of the element if found, otherwise -1.
    """

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        # If target is present at the mid
        if arr[mid] == target:
            return mid

        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1

        # if target is smaller, ignore right half
        else:
            right = mid - 1

    # if we reach here, then element was not present
    return -1


# Example usage:

arr = range(2, 200, 2)
target = input("Enter a number between 2 and 200: ")
target = int(target)
index = binary_search(arr, target)

if index != -1:
    print(f"{target} was found at index {index}.")
else:
    print(f"{target} was not found in the array.")