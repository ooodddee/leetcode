def findMinimumSum(power):
    total_increment = 0
    
    for i in range(1, len(power)):
        if power[i] < power[i-1]:
            total_increment += power[i-1] - power[i]
            power[i] = power[i-1]  # Make the array non-decreasing
    
    return total_increment

power = [3, 4, 1, 6, 2]
print(findMinimumSum(power))