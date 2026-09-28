from lru_cache import LRUCache
capacity = int(input("Enter cache capacity: "))
cache = LRUCache(capacity)
while True:
    print("\n===== LRU CACHE =====")
    print("1. Put")
    print("2. Get")
    print("3. Display Cache")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        key = int(input("Enter key: "))
        value = int(input("Enter value: "))
        cache.put(key, value)
        print("Value added successfully!")
    elif choice == "2":
        key = int(input("Enter key: "))
        value = cache.get(key)
        if value == -1:
            print("Cache Miss!")
        else:
            print("Value:", value)
    elif choice == "3":
        cache.display()
    elif choice == "4":
        print("Exiting LRU Cache...")
        break
    else:
        print("Invalid choice!")