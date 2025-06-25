# manual_version.py

"""
This function sorts a list of dictionaries by a specified key using a manual bubble sort algorithm.
Written without AI assistance for comparison with GitHub Copilot's version.
"""

def sort_dicts_by_key(data, sort_key):
    """
    Manually sorts a list of dictionaries by the specified key using bubble sort.

    Parameters:
    - data (list): List of dictionaries to be sorted.
    - sort_key (str): The key to sort the dictionaries by.

    Returns:
    - list: Sorted list of dictionaries.
    """
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Use 0 as default if the key is missing
            a = data[j].get(sort_key, 0)
            b = data[j + 1].get(sort_key, 0)
            if a > b:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


# Example usage
if __name__ == "__main__":
    items = [
        {"name": "Jeff", "age": 22},
        {"name": "Lena", "age": 19},
        {"name": "Tom", "age": 25}
    ]

    sorted_items = sort_dicts_by_key(items, "age")
    for item in sorted_items:
        print(item)
