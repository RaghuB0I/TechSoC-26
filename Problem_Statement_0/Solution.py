C = 0
N = 0
W_Total = 0
weights = []

def process_ship():
    global C, N, W_Total, weights
    C = float(input("Enter the capacity of the port: "))
    N = int(input("Enter the number of containers: "))
    W_Total = 0
    weights = []

    for i in range(N):
        w = float(input(f"Enter the weight of container {i+1}: "))
        weights.append(w)
        W_Total += w
    print()

choice = input("Level 1 or Level 2? (Enter 1 or 2): ")

if choice == "1":
    process_ship()
    print(f"Total shipment weight: {W_Total}")
    print(f"Average container weight: {W_Total / N if N > 0 else 0}")
    print(f"Heaviest container: {max(weights)}")
    print(f"Lightest container: {min(weights)}")
    print(f"Classification: {'heavy' if W_Total >= 200 else 'light'}")
    print(f"Port capacity: {C}")
    if W_Total <= C:
        print("The shipment can be unloaded.")
    else:
        print("The shipment exceeds port capacity.")

elif choice == "2" :
    process_ship()
    while True:
        print("The following features are available:")
        print("1. Sorted Display")
        print("2. Multi-Ship Processing")
        print("3. Bar Chart")
        print("4. Save Report")
        print("5. Read from File")
        print("6. Search")
        print("7. Kth Heaviest")
        print("8. Exit")
        print()

        choice = int(input("Enter your choice (1-8): "))

        if choice == 1:
            weights.sort()
            for i in range(len(weights)):
                print(f"Container {i+1}: {weights[i]}")  
            print()

        if choice == 2:
            while True:
                ch = input("Do you want to process another ship? (y/n): ")
                if ch == 'y':
                    process_ship()
                elif ch == 'n':
                    break
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")

        if choice == 3:
            for i in range(len(weights)):
                print(f"Container {i+1}:{'*' * (int(weights[i] // 5))}")
            print()
            print("Each '*' represents 5 units.")
            print()

        if choice == 4:
            ch = input("Do you want to save the report to a file? (y/n): ")
            if ch == 'y':
                name = input("Enter the filename to save the report: ")
                with open(name,'w') as f:
                    f.write(f"Total shipment weight: {W_Total}\n")
                    f.write(f"Average container weight: {W_Total / N if N > 0 else 0}\n")
                    f.write(f"Heaviest container: {max(weights)}\n")
                    f.write(f"Lightest container: {min(weights)}\n")
                    f.write(f"Classification: {'heavy' if W_Total >= 200 else 'light'}\n")
                    if W_Total <= C:
                        f.write("The shipment can be unloaded.\n")
                    else:
                        f.write("The shipment exceeds port capacity.\n")
                print(f"Report saved to {name}.")
                print()
            else:
                print("Report not saved.")
                print()

        if choice == 5:
            name = input("Enter the filename to read the report from: ")
            try:
                with open(name,'r') as f:
                    text = f.read()
            except FileNotFoundError:
                print(f"File {name} not found.")

            weights_new = text.split('\n')[1:]
            num = int(text.split('\n')[0])
            print(f"Total shipment weight: {W_Total}")
            print(f"Average container weight: {sum(weights_new) / num if num > 0 else 0}")
            print(f"Heaviest container: {max(weights_new)}")
            print(f"Lightest container: {min(weights_new)}")
            print(f"Classification: {'heavy' if sum(weights_new) >= 200 else 'light'}")
            print()


        if choice == 6:
            search_weight = float(input("Enter the weight to search for: "))
            if search_weight in weights:
                print(f"Container found!.\nContainer {weights.index(search_weight)+1} has weight {search_weight}.")
                print()
            else:
                print(f"No weight found with weight {search_weight}")
                print()

        if choice == 7:
            k = int(input("Enter the value of k: "))
            if k <= len(weights):
                temp = list(weights)
                temp.sort(reverse = True)
                print(f"The {k} {"st" if k == 1 else "nd" if k == 2 else "rd" if k == 3 else "th"} heaviest container has weight: {temp[k-1]}")
                print()
            else:
                print(f"Invalid Input. Only {len(temp)} containers exist.")
                print()

        if choice == 8:
            print("Exiting the program.")
            break
