def merge(arr):
    #initializing n as length of array 
    n=len(arr)
    #making sure that n is greater than 1 so the array if divided into two
    while n>1:
        #declaring an empty array for sorted array
        narr = []
        #initializing a loop to go through the array in parts of size n  
        for i in range(0, len(arr), n):
            #finding mid point
            mid=n//2
            #separating left side
            left = arr[i:i+mid]
            #separating right side
            right = arr[i+mid:i+n]
            #making sure that both side arn't empty
            while left and right:
                #comparing first eklements of both sides and appending the smaller one into narr
                if left[0] < right[0]:
                    narr.append(left.pop(0))
                else:
                    narr.append(right.pop(0))
            #if theres something left it is added to narr
            narr += right
            narr += left
        #
        arr = narr
        #doubling n so that next time array is separated into bigger parts
        n = n * 2
    #printing array
    print(arr)

#taking input of elements of array and calling the function
arr = input("Enter the Array Elements: ").split()
#converting elements to integers
arr = [int(x) for x in arr]
merge(arr)