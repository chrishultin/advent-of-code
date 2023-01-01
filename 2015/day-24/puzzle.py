import itertools
import math


def parser(input_file_name):
    packages = []
    with open(input_file_name) as input_file:
        for line in input_file.readlines():
            packages.append(int(line.strip()))

    return packages

def possible_permutations(boxes: list[int], split=3):
    target_weight = int(sum(boxes) / split)

    result = []

    def find(arr, num, path=()):
        if not arr:
            return
        if arr[0] == num:
            result.append(path + (arr[0],))
        else:
            find(arr[1:], num - arr[0], path + (arr[0],))
            find(arr[1:], num, path)

    find(boxes, target_weight)
    return result

def p1_nonoverlapping_permutations(possible_permutations):
    shortest_overlapping = 99999
    current_shortest_permutation = None
    results = []
    for first_permutation in sorted(possible_permutations, key=len):
        if len(first_permutation) > shortest_overlapping or first_permutation == current_shortest_permutation:
            break
        first_set = set(first_permutation)
        for second_permutation in possible_permutations:
            second_set = set(second_permutation)
            if len(first_set.intersection(second_set)) == 0:
                for third_permutation in possible_permutations:
                    third_set = set(third_permutation)
                    if len(third_set.intersection(first_set)) == 0 and len(third_set.intersection(second_set)) == 0:
                        # print(first_set, second_set, third_set)
                        shortest_overlapping = len(first_set)
                        current_shortest_permutation = first_permutation
                        results.append(first_permutation)
                        break
                break
    print(results)
    return [(math.prod(r), r) for r in results]

def p2_nonoverlapping_permutations(possible_permutations):
    shortest_overlapping = 99999
    current_shortest_permutation = None
    results = []
    for first_permutation in sorted(possible_permutations, key=len):
        if len(first_permutation) > shortest_overlapping or first_permutation == current_shortest_permutation:
            continue
        first_set = set(first_permutation)
        for second_permutation in possible_permutations:
            if first_permutation == current_shortest_permutation:
                break
            second_set = set(second_permutation)
            if len(first_set.intersection(second_set)) == 0:
                for third_permutation in possible_permutations:
                    if first_permutation == current_shortest_permutation:
                        break
                    third_set = set(third_permutation)
                    if len(third_set.intersection(first_set)) == 0 and len(third_set.intersection(second_set)) == 0:
                        for fourth_permutation in possible_permutations:
                            if first_permutation == current_shortest_permutation:
                                break
                            fourth_set = set(fourth_permutation)
                            if len(fourth_set.intersection(first_set)) == 0 and len(
                                fourth_set.intersection(second_set)) == 0 and len(
                                fourth_set.intersection(third_set)) == 0:
                                print(first_set, second_set, third_set, fourth_set)
                                shortest_overlapping = len(first_set)
                                current_shortest_permutation = first_permutation
                                results.append(first_permutation)
                                break
                            else:
                                continue
                    else:
                        continue
            else:
                continue

    return [(math.prod(r), r) for r in results]

def part_one(results):
    results = [(math.prod(r), r) for r in results]
    print(sorted(results, key=lambda _: _[0])[0])

if __name__ == '__main__':
    boxes = parser('input.txt')
    part_one(possible_permutations(boxes, split=4))