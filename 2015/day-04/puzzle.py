import hashlib

def puzzle_1(secret: str):
    index = 1
    while True:
        adventcoin_string = f"{secret}{index}"
        adventcoin = hashlib.md5(adventcoin_string.encode()).hexdigest()
        if adventcoin[0:5] == "00000":
            return index
        index += 1

def puzzle_2(secret: str):
    index = 1
    while True:
        adventcoin_string = f"{secret}{index}"
        adventcoin = hashlib.md5(adventcoin_string.encode()).hexdigest()
        if adventcoin[0:6] == "000000":
            return index
        index += 1

if __name__ == '__main__':
    secret = 'ckczppom'
    print(f'Puzzle 1: {puzzle_1(secret)}')
    print(f'Puzzle 2: {puzzle_2(secret)}')

