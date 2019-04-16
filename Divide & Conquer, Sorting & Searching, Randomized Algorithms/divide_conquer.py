def get_arr(text):
    ''' Load integer file and convert to array
    '''
    with open(text) as file:
        arr = [int(s) for s in file.read().split('\n') if s.isdigit()]
        print(len(arr)) # Should be 100,000 for the assignment
        return arr


def inversions(array):
    ''' Take in array of ints and compute the number of inversions
    '''
