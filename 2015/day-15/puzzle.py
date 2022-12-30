def parser(input_file_name: str):
    ingredients = {}
    with open(input_file_name, 'r') as input_file:
        for line in input_file.readlines():
            line = line.strip().split(' ')
            name = line[0][:-1]
            capacity = int(line[2][:-1])
            durability = int(line[4][:-1])
            flavor = int(line[6][:-1])
            texture = int(line[8][:-1])
            calories = int(line[10])
            ingredients[name] = {
                'capacity': capacity,
                'durability': durability,
                'flavor': flavor,
                'texture': texture,
                'calories': calories
            }
    return ingredients

def part_one_test(ingredients: dict):
    num_ingredients = len(ingredients.keys())
    max_score = 0
    ing = list(ingredients.values())
    for ingredient_one_value in range(1, 100):
        print(f'--- {ingredient_one_value}')
        ingredient_two_value = 100 - ingredient_one_value
        print(f'--- {ingredient_two_value}')
        capacity = (ingredient_one_value * ing[0]['capacity']) + (ingredient_two_value * ing[1]['capacity'])
        durability = (ingredient_one_value * ing[0]['durability']) + (ingredient_two_value * ing[1]['durability'])
        flavor = (ingredient_one_value * ing[0]['flavor']) + (ingredient_two_value * ing[1]['flavor'])
        texture = (ingredient_one_value * ing[0]['texture']) + (ingredient_two_value * ing[1]['texture'])
        if capacity > 0 and durability > 0 and flavor > 0 and texture > 0:
            score = capacity * durability * flavor * texture
            if score > max_score:
                print(capacity)
                print(durability)
                print(flavor)
                print(texture)
                max_score = score
    print(max_score)

def part_one(ingredients: dict):
    possible_permutations = []
    for i1 in range(1, 97):
        for i2 in range(1, 97):
            for i3 in range(1, 97):
                remaining = 100 - (i1 + i2 + i3)
                if remaining > 0:
                    possible_permutations.append([i1, i2, i3, remaining])

    max_score = 0
    ingredients = list(ingredients.values())
    for recipe in possible_permutations:
        capacity = [recipe[index] * ingredients[index]['capacity'] for index,ingredient in enumerate(ingredients)]
        capacity = max(0, sum(capacity))
        durability = [recipe[index] * ingredients[index]['durability'] for index,ingredient in enumerate(ingredients)]
        durability = max(0, sum(durability))
        flavor = [recipe[index] * ingredients[index]['flavor'] for index,ingredient in enumerate(ingredients)]
        flavor = max(0, sum(flavor))
        texture = [recipe[index] * ingredients[index]['texture'] for index,ingredient in enumerate(ingredients)]
        texture = max(0, sum(texture))
        max_score = max(max_score, (capacity * durability * flavor * texture))

    print(max_score)


def part_two(ingredients: dict):
    ingredients = list(ingredients.values())

    possible_permutations = []
    for i1 in range(1, 97):
        for i2 in range(1, 97):
            for i3 in range(1, 97):
                remaining = 100 - (i1 + i2 + i3)
                if remaining > 0:
                    # check calories
                    recipe = [i1, i2, i3, remaining]
                    calories = [recipe[index] * ingredients[index]['calories'] for index,ingredient in enumerate(ingredients)]
                    calories = sum(calories)
                    if calories == 500:
                        possible_permutations.append(recipe)

    max_score = 0
    for recipe in possible_permutations:
        capacity = [recipe[index] * ingredients[index]['capacity'] for index,ingredient in enumerate(ingredients)]
        capacity = max(0, sum(capacity))
        durability = [recipe[index] * ingredients[index]['durability'] for index,ingredient in enumerate(ingredients)]
        durability = max(0, sum(durability))
        flavor = [recipe[index] * ingredients[index]['flavor'] for index,ingredient in enumerate(ingredients)]
        flavor = max(0, sum(flavor))
        texture = [recipe[index] * ingredients[index]['texture'] for index,ingredient in enumerate(ingredients)]
        texture = max(0, sum(texture))
        max_score = max(max_score, (capacity * durability * flavor * texture))

    print(max_score)



if __name__ == '__main__':
    part_two(parser('input.txt'))