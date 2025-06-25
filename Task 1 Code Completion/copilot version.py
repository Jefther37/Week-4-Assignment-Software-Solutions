# copilot_version.py

"""
This function sorts a list of dictionaries by a specified key.
Suggested and refined using GitHub Copilot.
"""

def sort_dicts_by_key(data, sort_key):
    """
    Sorts a list of dictionaries by the specified key.

    Parameters:
    - data (list): List of dictionaries to be sorted.
    - sort_key (str): The key to sort the dictionaries by.

    Returns:
    - list: Sorted list of dictionaries.
    """
    return sorted(data, key=lambda x: x.get(sort_key, ''))


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
