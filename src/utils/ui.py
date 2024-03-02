def create_list(items: list, title: str) -> int:
    """Create a list of items and returns the index of the item in the list. selected by the user."""
    from itertools import zip_longest

    print(f"\n{title}")
    items_with_indices = [f"{i + 1}. {item}" for i, item in enumerate(items)]
    max_length = max(len(item) for item in items_with_indices)
    items_with_indices = [item.ljust(max_length) for item in items_with_indices]
    items_in_rows = list(zip_longest(*[iter(items_with_indices)]*3, fillvalue=''))
    for row in items_in_rows:
        print('   '.join(row))
    print(f"0. Cancel")
    while True:
        try:
            choice = int(input("Select an option: "))
            if choice < 0 or choice > len(items):
                raise ValueError
            return choice
        except ValueError:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # Test the function
    items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6", "Item 7", "Item 8", "Item 9", "Item 10"]
    title = "Test List"
    c = create_list(items, title)
    if c == 0: print("Cancelled")
    else:  print(items[create_list(items, title) - 1])