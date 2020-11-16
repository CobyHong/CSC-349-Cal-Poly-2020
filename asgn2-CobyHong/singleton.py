def singleton(array):
    last_index = len(array) - 1
    mid = len(array) // 2

    if (0 == last_index):
        return array[0]
    elif(mid % 2 == 0):
        if(array[mid] == array[mid+1]):
            return singleton(array[mid+2:])
        else:
            return singleton(array[:mid+1])
    elif(mid % 2 != 0):
        if(array[mid-1] == array[mid]):
            return singleton(array[mid+1:])
        else:
            return singleton(array[:mid])