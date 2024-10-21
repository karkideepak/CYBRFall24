def dailyTemperatures(temperatures):
    stack = []
    # initialize an empty stack to store indices of temperatures
    output = [0] * len(temperatures)
    # initialize output array with 0s, the same length as temperatures

    print("Input:", user_input)
    # print the initial state of the output array (all zeros)

    for i in range(len(temperatures)):
        # loop through each day (index) in the temperatures list
        while stack and temperatures[stack[-1]] < temperatures[i]:
            # while the stack is not empty and the current temperature is higher
            # than the temperature at the index stored at the top of the stack

            ind = stack.pop()
            # pop the index from the stack (this is the day with a cooler temperature)

            output[ind] = i - ind
            # update the output for that day with the number of days until a warmer temperature
        stack.append(i)
        # add the current index (day) to the stack

    print("Output:", output)
    # print the final output after all calculations are done
    return output

# Given array
user_input = [98, 102, 100, 97, 104, 101, 106, 107]
result = dailyTemperatures(user_input)
