class Circuit:
    def __init__(self):
        # Operation: AND, OR, RSHIFT, LSHIFT, NOT
        self.circuit_map = {
            # 'x': {
            #     'operation': [],
            #     'value': None,
            #     'inputs': []
            # }
        }

    def parser(self, input_file_name: str):
        with open(input_file_name, 'r') as input_file:
            for line in input_file.readlines():
                components = line.strip().split(' ')
                if len(components) == 3:
                    wire_id = components[2]
                    if components[0].isnumeric():
                        self.circuit_map[wire_id] = {'value': int(components[0])}
                    else:
                        self.circuit_map[wire_id] = {'operation': 'SELF', 'inputs': [components[0]]}
                elif len(components) == 4:
                    wire_id = components[3]
                    self.circuit_map[wire_id] = {
                        'operation': 'NOT',
                        'inputs': [components[1]]
                    }
                elif len(components) == 5:
                    wire_id = components[4]
                    if components[1] in ['LSHIFT', 'RSHIFT']:
                        components[2] = int(components[2])
                    self.circuit_map[wire_id] = {
                        'operation': components[1],
                        'inputs': [components[0], components[2]]
                    }
        print(self.circuit_map)

    def get_wire_value(self, wire_id):
        print(wire_id)
        if wire_id not in self.circuit_map:
            if str(wire_id).isnumeric():
                return int(wire_id)

        wire_info = self.circuit_map.get(wire_id)
        if wire_info.get('value') is not None:
            return wire_info['value']

        OPERATION_MAP = {
            'AND': lambda left, right: left & right,
            'OR': lambda left, right: left | right,
            'LSHIFT': lambda left, shift: left << shift,
            'RSHIFT': lambda left, shift: left >> shift,
            'NOT': lambda left: ~left,
            'SELF': lambda left: self.get_wire_value(left)
        }

        if wire_info.get('inputs') is not None:
            values = []
            for index, wire_input in enumerate(wire_info['inputs']):
                if not str(wire_input).isnumeric():
                    input_value = self.get_wire_value(wire_input)
                    if input_value is None:
                        print(f'Cant calc {wire_id}')
                        print(f'Wire {wire_input} value is not set')
                        return None
                    values.append(input_value)
                else:
                    values.append(int(wire_input))
            operation = wire_info.get('operation')
            if operation == 'SELF':
                pass
            wire_value = OPERATION_MAP[operation](*values)
            self.circuit_map[wire_id]['value'] = wire_value
            return wire_value

    def calculate_wire_values(self):
        while True:
            allValuesFound = True
            for wire in self.circuit_map.keys():
                value = self.get_wire_value(wire)
                print(f'Wire {wire}: {value}')
                if value is None:
                    allValuesFound = False

            if allValuesFound:
                break

if __name__ == '__main__':
    circuit = Circuit()
    circuit.parser('input.txt')
    circuit.calculate_wire_values()
    print(circuit.get_wire_value('a'))
