list_divide(numbers, divide=2) counts how many numbers in the list are divisible by the given divisor (default is 2). It iterates through each number in the list, checks if it is divisible by the divisor, and increments a count accordingction returns the total count of divisible numbers.
def list_divide(numbers, divide=2):
    count = 0
    for n in numbers:
        if n % divide == 0:
            count += 1
    return count
class ListDivideException(Exception):
    pass 

def_list_divide():

    """
    Test listDivide
    """
    assert list_divide([1,2,3,4,5]) == 2
    assert list_divide([2,4,6,8,10]) == 5
    assert list_divide([30, 54, 63,98, 100], divide=10) == 2
    assert list_divide([]) == 0
    assert list_divide([1,2,3,4,5], 1) == 5
    
if __name__ == "__main__":
    test_list_divide()
