def calculate_code_index(row: int, column: int) -> int:
    return sum(range(row + column - 1)) + column

def calculate_code(index: int):
    code = 20151125
    for _ in range(index - 1):
        code = (code * 252533) % 33554393

    return code

if __name__ == '__main__':
    index = (calculate_code_index(2981,3075))
    # index = (calculate_code_index(1,1))
    print(index)
    print(calculate_code(index))