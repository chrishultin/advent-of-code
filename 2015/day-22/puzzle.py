# state = (player_hp, player_mana, boss_hp, shield_time, poison_time, recharge_time, mana_spent)
import collections


def part_one_bfs(boss_damage: int, starting_boss_hp: int):
    player_hp: int = 50
    player_mana: int = 500
    queue = collections.deque([(player_hp, player_mana, starting_boss_hp, 0, 0, 0, 0)])

    minimum_mana = 99999999

    while queue:
        current_state = queue.popleft()
        print(current_state)

        player_hp = current_state[0]
        player_mana = current_state[1]
        boss_hp = current_state[2]
        shield_time = current_state[3]
        poison_time = current_state[4]
        recharge_time = current_state[5]
        mana_spent = current_state[6]

        if shield_time > 0:
            shield_time -= 1
        if poison_time > 0:
            poison_time -= 1
            boss_hp -= 3
        if recharge_time > 0:
            recharge_time -= 1
            player_mana += 101

        if boss_hp <= 0:
            # player has won
            if mana_spent < minimum_mana:
                minimum_mana = mana_spent
                break

        possible_player_actions = []
        # Do player actions
        if shield_time == 0 and player_mana >= 113:
            possible_player_actions.append((player_hp, player_mana - 113, boss_hp, 6, poison_time, recharge_time, mana_spent + 113))
        if poison_time == 0 and player_mana >= 173:
            possible_player_actions.append((player_hp, player_mana - 173, boss_hp, shield_time, 6, recharge_time, mana_spent + 173))
        if recharge_time == 0 and player_mana >= 229:
            possible_player_actions.append((player_hp, player_mana - 229, boss_hp, shield_time, poison_time, 5, mana_spent + 229))
        if player_mana >= 53:
            possible_player_actions.append((player_hp, player_mana - 53, boss_hp - 4, shield_time, poison_time, recharge_time, mana_spent + 53))
        if player_mana >= 73:
            possible_player_actions.append((player_hp + 2, player_mana - 73, boss_hp - 2, shield_time, poison_time, recharge_time, mana_spent + 73))
        if player_mana < 53:
            continue

        # boss actions
        for action in possible_player_actions:
            player_hp = action[0]
            player_mana = action[1]
            boss_hp = action[2]
            shield_time = action[3]
            poison_time = action[4]
            recharge_time = action[5]
            mana_spent = action[6]

            shield_boost = 0
            if shield_time > 0:
                shield_time -= 1
                shield_boost = 7
            if poison_time > 0:
                poison_time -= 1
                boss_hp -= 3
            if recharge_time > 0:
                recharge_time -= 1
                player_mana += 101

            if mana_spent > minimum_mana:
                continue
            if boss_hp <= 0:
                # player has won
                if mana_spent < minimum_mana:
                    minimum_mana = mana_spent
                    break

            boss_damage_to_player = max(1, boss_damage - shield_boost)
            if player_hp > boss_damage_to_player:
                queue.append((
                    player_hp - boss_damage_to_player,
                    player_mana,
                    boss_hp,
                    shield_time,
                    poison_time,
                    recharge_time,
                    mana_spent,
                ))
            else:
                print('player died')

    return minimum_mana

def part_two_bfs(boss_damage: int, starting_boss_hp: int):
    player_hp: int = 50
    player_mana: int = 500
    queue = collections.deque([(player_hp, player_mana, starting_boss_hp, 0, 0, 0, 0)])

    minimum_mana = 99999999

    while queue:
        current_state = queue.popleft()
        print(current_state)

        player_hp = current_state[0] - 1
        player_mana = current_state[1]
        boss_hp = current_state[2]
        shield_time = current_state[3]
        poison_time = current_state[4]
        recharge_time = current_state[5]
        mana_spent = current_state[6]

        if shield_time > 0:
            shield_time -= 1
        if poison_time > 0:
            poison_time -= 1
            boss_hp -= 3
        if recharge_time > 0:
            recharge_time -= 1
            player_mana += 101

        if boss_hp <= 0:
            # player has won
            if mana_spent < minimum_mana:
                minimum_mana = mana_spent
                break

        possible_player_actions = []
        # Do player actions
        if shield_time == 0 and player_mana >= 113:
            possible_player_actions.append((player_hp, player_mana - 113, boss_hp, 6, poison_time, recharge_time, mana_spent + 113))
        if poison_time == 0 and player_mana >= 173:
            possible_player_actions.append((player_hp, player_mana - 173, boss_hp, shield_time, 6, recharge_time, mana_spent + 173))
        if recharge_time == 0 and player_mana >= 229:
            possible_player_actions.append((player_hp, player_mana - 229, boss_hp, shield_time, poison_time, 5, mana_spent + 229))
        if player_mana >= 53:
            possible_player_actions.append((player_hp, player_mana - 53, boss_hp - 4, shield_time, poison_time, recharge_time, mana_spent + 53))
        if player_mana >= 73:
            possible_player_actions.append((player_hp + 2, player_mana - 73, boss_hp - 2, shield_time, poison_time, recharge_time, mana_spent + 73))
        if player_mana < 53:
            continue

        # boss actions
        for action in possible_player_actions:
            player_hp = action[0]
            player_mana = action[1]
            boss_hp = action[2]
            shield_time = action[3]
            poison_time = action[4]
            recharge_time = action[5]
            mana_spent = action[6]

            shield_boost = 0
            if shield_time > 0:
                shield_time -= 1
                shield_boost = 7
            if poison_time > 0:
                poison_time -= 1
                boss_hp -= 3
            if recharge_time > 0:
                recharge_time -= 1
                player_mana += 101

            if mana_spent > minimum_mana:
                continue
            if boss_hp <= 0:
                # player has won
                if mana_spent < minimum_mana:
                    minimum_mana = mana_spent
                    break

            boss_damage_to_player = max(1, boss_damage - shield_boost)
            if player_hp > boss_damage_to_player:
                queue.append((
                    player_hp - boss_damage_to_player,
                    player_mana,
                    boss_hp,
                    shield_time,
                    poison_time,
                    recharge_time,
                    mana_spent,
                ))
            else:
                print('player died')

    return minimum_mana


if __name__ == '__main__':
    print(part_two_bfs(9, 58))