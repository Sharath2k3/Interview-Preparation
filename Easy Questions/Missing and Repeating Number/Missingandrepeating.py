def print_two_elements(arr):
    n = len(arr)
    missing = (n* (n+1))//2
    print("Repeating ",end=" ")
    for i in range(n):
        if(abs(arr[i]-1)>0):
            arr[abs(arr[i]-1)]=-arr[abs(arr[i]-1)]
            missing -= abs(arr[i])
        else:
            print(abs(arr[i]))
    print("Missing =",missing)
    
