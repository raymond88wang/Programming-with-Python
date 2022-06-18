def fibonacci_recursive(n):
    #usually it is just n <= 1: return n, but the prompt is written weirdly so these extra conditions is needed to meet those requirements
    # if n <= 1:
    #     return n
    if n <= 1:
        return 0
    elif n <= 2:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

print([(i, fibonacci_recursive(i)) for i in range(1, 10)])

# What is the problem with this iterative approach?
# def fibonacci_iterative(n):
#     # if n <= 1:
#     #     return n
#     if n <= 1:
#         return 0
#     elif n <= 2:
#         return 1
    
#     #result = [0, 1, sum of previous 2 numbers, sum of previous 2 numbers]
#     result = [0,1]
#     for i in range(2, n+1):
#         #add the previous 2 numbers
#         result.append(result[i-1] + result[i-2])
#         print(result)
#     # return result[n]
#     return result[n-1]

#len(result) = n + 1
#if n is a huge number, result will take up too much memory!

#Here is another approach that will not run into that issue
def fibonacci_iterative(n):
    # if n <= 1:
    #     return n
    if n <= 1:
        return 0
    elif n <= 2:
        return 1
    
    #result = [0, 1, sum of previous 2 numbers, sum of previous 2 numbers]
    #you can do this with a tuple as well, but you would just need to reallocate every time
    result = [0,1]
    for i in range(2, n+1):
        #add the previous 2 numbers
        sum = result[0] + result[1]
        result[0] = result[1]
        result[1] = sum
        print(result)
    return result[0]
    # return result[1]

print([(i, fibonacci_iterative(i)) for i in range(1, 10)])
