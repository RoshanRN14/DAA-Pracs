def fractional_knapsack(capacity, items):
    # Sort items by profit-to-weight ratio
    items = sorted(items, key=lambda x: x[1]/x[0], reverse=True)

    total_value = 0
    for weight, profit in items:
        if capacity >= weight:
            capacity -= weight
            total_value += profit
        else:
            # Add the fraction of the remaining capacity
            total_value += profit * (capacity / weight)
            break

    return total_value

# Input: (Weight, Profit)
items = [(10, 60), (20, 100), (30, 120)]
capacity = 50
print("Maximum profit:", fractional_knapsack(capacity, items))
