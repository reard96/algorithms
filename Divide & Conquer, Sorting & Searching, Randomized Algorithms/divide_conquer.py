def get_arr(text):
    ''' Load integer file and convert to array
    '''
    with open(text) as file:
        arr = [int(s) for s in file.read().split('\n') if s.isdigit()]
        return arr


def inversions(arr):
    ''' Take in array of ints and compute the number of inversions
    '''
    if len(arr) == 1:
        return arr, 0

    else:
        left = arr[:len(arr) // 2]
        right = arr[len(arr) // 2:]

        left, left_length = inversions(left)
        right, right_length = inversions(right)
        sorted = []

        i = 0
        j = 0
        count = 0 + left_length + right_length

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted.append(left[i])
            i += 1
        else:
            sorted.append(right[j])
            j += 1
            count += (len(left) - i)

    sorted += left[i:]
    sorted += right[j:]

    return sorted, count

print(inversions(get_arr('integer_array.txt'))[1])
