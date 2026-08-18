C = float(input("Enter the capacity of the port: "))
N = int(input("Enter the number of containers: "))
W_Total = 0
weights = []

for i in range(N):
    w = float(input(f"Enter the weight of container {i+1}: "))
    weights.append(w)
    W_Total += w
print()

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
    
