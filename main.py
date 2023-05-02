def movingAverage(inputArray, windowSize):
    results = []
    if windowSize > len(inputArray):
        return results
    if windowSize == 1:
        return inputArray
    start = 0
    while start+windowSize <= len(inputArray):
        sum_nums = 0
        for i in range(windowSize):
            sum_nums += inputArray[i+start]
        average = sum_nums / windowSize
        results.append(average)
        start += 1
    return results


# Test case 1
input_array = [1, 2, 3, 4, 5]
window_size = 3
results = movingAverage(input_array, window_size)
if results == [2.0, 3.0, 4.0]:
    print("Test case 1 passed")

# Test case 2
input_array = [1, 2, 3, 4, 5]
window_size = 4
results = movingAverage(input_array, window_size)
if results == [2.5, 3.5]:
    print("Test case 2 passed")

# Test case 3
input_array = [1, 2, 3, 4, 5]
window_size = 6
results = movingAverage(input_array, window_size)
if not results:
    print("Test case 3 passed")

# Test case 4
input_array = [190, 295, 293, 203, 2093, 689, 105, 394, 795]
window_size = 2
results = movingAverage(input_array, window_size)
if results == [242.5, 294, 248, 1148, 1391, 397, 249.5, 594.5]:
    print("Test case 4 passed")

# Test case 5
input_array = [190, 295, 293, 203, 2093, 689, 105, 394, 795]
window_size = 1
results = movingAverage(input_array, window_size)
if results == [190, 295, 293, 203, 2093, 689, 105, 394, 795]:
    print("Test case 5 passed")
