def merge(arr):
    # initializing n as 1
    n = 1
    # repeating until the whole array is sorted
    while n < len(arr):
        # making an empty array
        narr = []
        # taking two parts at a time
        for i in range(0, len(arr), n * 2):
            # separating left side
            left = arr[i:i+n]
            # separating right side
            right = arr[i+n:i+n*2]
            # comparing both sides
            while left and right:
                if left[0] < right[0]:
                    narr.append(left.pop(0))
                else:
                    narr.append(right.pop(0))
            # adding remaining elements
            narr += left
            narr += right
        # updating the array
        arr = narr
        # doubling the size of parts
        n = n * 2
        #printing the output
    print("Sorted Array:", arr)
# taking input
arr = list(map(int, input("Enter the Array Elements: ").split()))
# calling the function
merge(arr)