import itertools
from collections import deque as queue
from dataclasses import dataclass
from functools import cache


def parser(input_file_name: str):
    with open(input_file_name, 'r') as input_file:
        volcano = {}
        for line in input_file.readlines():
            line = line.strip().split(' ')
            valve_id = line[1]
            flow_rate = int(line[4][5:-1])
            valves = [v.replace(',', '') for v in line[9:]]

            volcano[valve_id] = {
                'rate': flow_rate,
                'valves': valves
            }
        return volcano

# @cache
def best_route_to_destination(volcano, start, end):
    #bfs
    q = queue([[start]])

    while q:
        path = q.popleft()
        if end == path[-1]:
            return len(path[1:])
        for possible_move in volcano[path[-1]]['valves']:
            new_path = path + [possible_move]
            q.append(new_path)

def calculate_distances(volcano):
    distance_map = {}
    for start_valve in volcano.keys():
        # print(f'start: {start_valve}')
        distance_map[start_valve] = {}
        for end_valve in volcano.keys():
            if volcano[end_valve]['rate'] != 0:
                # print(f'end: {end_valve}')
                if end_valve != start_valve:
                    # print(f'route: {best_route_to_destination(volcano, start_valve, end_valve)}')
                    distance_map[start_valve][end_valve] = best_route_to_destination(volcano, start_valve, end_valve)

    return distance_map

@dataclass
class VolcanoState:
    current_position: str
    visited: list[str]
    time: int
    score: int

    def connections(self, distance_map):
        return [v for v in distance_map[self.current_position] if v not in self.visited and v in distance_map[self.current_position]]

    def flow(self, volcano):
        return (30 - (self.time)) * volcano[self.current_position]['rate']

    def __repr__(self):
        return f'{self.current_position} {self.visited} {self.time} {self.score}'

def part_one(volcano, distance_map):

    q = queue([VolcanoState('AA', ['AA'], 0, 0)])

    max_score = 0
    while q:
        current_state = q.popleft()
        remaining_valves = current_state.connections(distance_map)
        if len(remaining_valves) == 0:
            if current_state.score + current_state.flow(volcano) > max_score:
                max_score = current_state.score + current_state.flow(volcano)
        for next_valve in remaining_valves:
            # Check to make sure travel time wont exceed 30 minute limit
            travel_time = distance_map[current_state.current_position][next_valve]
            if travel_time + current_state.time < 29:
                q.append(VolcanoState(next_valve,
                                      current_state.visited + [next_valve],
                                      travel_time + current_state.time + 1,
                                      current_state.score + current_state.flow(volcano)))
            else:
                if current_state.score + current_state.flow(volcano) > max_score:
                    max_score = current_state.score + current_state.flow(volcano)
    print(max_score)

def part_two(volcano, distance_map):

    q = queue([VolcanoState('AA', [], 4, 0)])

    max_score = 0
    all_states = []
    useful_states = {}
    while q:
        current_state = q.popleft()
        remaining_valves = current_state.connections(distance_map)
        for next_valve in remaining_valves:
            # Check to make sure travel time wont exceed 30 minute limit
            travel_time = distance_map[current_state.current_position][next_valve]

            new_state = VolcanoState(next_valve,
                                     current_state.visited + [next_valve],
                                     travel_time + current_state.time + 1,
                                     current_state.score + current_state.flow(volcano))
            if new_state.score != 0:
                all_states.append(new_state)
                state_str = ','.join(sorted(new_state.visited))
                if state_str in useful_states:
                    if new_state.score > useful_states[state_str][1]:
                        useful_states[state_str] = (new_state, new_state.score)
                else:
                    useful_states[state_str] = (new_state, new_state.score)
            if travel_time + current_state.time < 30:
                q.append(new_state)

    for human_state in useful_states.values():
        for elephant_state in useful_states.values():
            for h_visited in human_state[0].visited:
                if h_visited in elephant_state[0].visited:
                    break
            else:
                score = human_state[0].score + elephant_state[0].score
                if score > max_score:
                    max_score = score
    print(max_score)

if __name__ == '__main__':
    volcano = parser('test_input.txt')
    distance_map = calculate_distances(volcano)
    part_one(volcano, distance_map)
    part_two(volcano, distance_map)
