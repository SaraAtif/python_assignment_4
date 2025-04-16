def access_element(lst, index):
    """Access an element in the list by index."""
    try:
        return lst[index]
    except IndexError:
        return "Index out of range"

def modify_element(lst, index, value):
    """Modify an element in the list at the given index."""
    try:
        lst[index] = value
        return lst
    except IndexError:
        return "Index out of range"

def slice_list(lst, start, end):
    """Return a slice of the list from start to end index."""
    try:
        return lst[start:end]
    except IndexError:
        return "Index out of range"                



def main():
    lst = ["1", "2", "3", "4", "5"]	
    print("Original list:", lst)
    print("Choose an operation: access, modify, slice")
    operation = input("Enter operation: ")


    if operation == "access":
        index = int(input("Enter index to access: "))
        result = access_element(lst, index)
        print(f"Accessed element: {result}")

    elif operation == "modify":
        index = int(input("Enter index to modify: "))
        value = input("Enter new value: ")
        result = modify_element(lst, index, value)
        print(f"Modified list: {result}")

    elif operation == "slice":
        start = int(input("Enter start index: "))
        end = int(input("Enter end index: "))
        result = slice_list(lst, start, end)
        print(f"Sliced list: {result}")
    else:
        print("Invalid operation. Please choose 'access', 'modify', or 'slice'.")

if __name__ == "__main__":
    main()
