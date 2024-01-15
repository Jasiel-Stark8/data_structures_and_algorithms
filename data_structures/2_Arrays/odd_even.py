"""create a list with user input as max element"""

max_num = int(input('Enter a positive number: '))

def max_range(max_num: int) -> list:
    """create list range"""
    return [num for num in range(1, max_num) if num % 2 != 0]

print(max_range(max_num))
