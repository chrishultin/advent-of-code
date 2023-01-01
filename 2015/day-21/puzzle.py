WEAPONS = [
    {
        "name": "Dagger",
        "cost": 8,
        "damage": 4
    },
    {
        "name": "Shortsword",
        "cost": 10,
        "damage": 5
    },
    {
        "name": "Warhammer",
        "cost": 25,
        "damage": 6
    },
    {
        "name": "Longsword",
        "cost": 40,
        "damage": 7
    },
    {
        "name": "Greataxe",
        "cost": 74,
        "damage": 8
    }
]

ARMOR = [
    {
        "name": "Leather",
        "cost": 13,
        "armor": 1
    },
    {
        "name": "Chainmail",
        "cost": 31,
        "armor": 2
    },
    {
        "name": "Splintmail",
        "cost": 53,
        "armor": 3,
    },
    {
        "name": "Bandedmail",
        "cost": 75,
        "armor": 4
    },
    {
        "name": "Platemail",
        "cost": 102,
        "armor": 5
    }
]

RINGS = [
    {
        "name": "Damage +1",
        "cost": 25,
        "armor": 0,
        "damage": 1
    },
    {
        "name": "Damage +2",
        "cost": 50,
        "armor": 0,
        "damage": 2
    },
    {
        "name": "Damage +3",
        "cost": 100,
        "armor": 0,
        "damage": 3
    },
    {
        "name": "Defence +1",
        "cost": 20,
        "armor": 1,
        "damage": 0
    },
    {
        "name": "Defence +2",
        "cost": 40,
        "armor": 2,
        "damage": 0
    },
    {
        "name": "Defence +3",
        "cost": 80,
        "armor": 3,
        "damage": 0
    },
]

def calculate_stats(weapon: dict, armor: dict, ring_one: dict, ring_two: dict):
    total_damage = sum([x.get('damage', 0) for x in [weapon, armor, ring_one, ring_two]])
    total_armor = sum([x.get('armor', 0) for x in [weapon, armor, ring_one, ring_two]])
    total_cost = sum([x.get('cost', 0) for x in [weapon, armor, ring_one, ring_two]])

    return {'damage': total_damage,
            'armor': total_armor,
            'cost': total_cost}

def part_one_fight(your_stats: dict, boss_stats: dict):
    player_damage_to_boss = max(1, your_stats['damage'] - boss_stats['armor'])
    boss_damage_to_player = max(1, boss_stats['damage'] - your_stats['armor'])

    player_health = your_stats['hp']
    boss_health = boss_stats['hp']

    while player_health > 0 or boss_health > 0:
        boss_health -= player_damage_to_boss
        if boss_health <= 0:
            return True

        player_health -= boss_damage_to_player
        if player_health <= 0:
            return False

def part_one(boss_stats: dict):
    lowest_cost = 9999999
    for weapon in WEAPONS:
        for armor in ARMOR + [{}]:
            for ring_one in RINGS + [{"name": "dummyring1"}, {"name": "dummyring2"}]:
                for ring_two in RINGS + [{"name": "dummyring1"}, {"name": "dummyring2"}]:
                    if ring_two != ring_one:
                        stats = calculate_stats(weapon, armor, ring_one, ring_two)
                        print(stats)
                        stats['hp'] = 100
                        if stats['cost'] >= lowest_cost:
                            continue
                        if part_one_fight(stats, boss_stats):
                            lowest_cost = stats['cost']
    print(lowest_cost)

def part_two(boss_stats: dict):
    max_cost = 0
    for weapon in WEAPONS:
        for armor in ARMOR + [{}]:
            for ring_one in RINGS + [{"name": "dummyring1"}, {"name": "dummyring2"}]:
                for ring_two in RINGS + [{"name": "dummyring1"}, {"name": "dummyring2"}]:
                    if ring_two != ring_one:
                        stats = calculate_stats(weapon, armor, ring_one, ring_two)
                        print(stats)
                        stats['hp'] = 100
                        if stats['cost'] <= max_cost:
                            continue
                        if not part_one_fight(stats, boss_stats):
                            max_cost = stats['cost']
    print(max_cost)

if __name__ == '__main__':
    print(part_two({'damage': 8, 'armor': 2, 'hp': 100}))