import collections
import math
import typing

ADD = 1
MULTIPLY = 2
HALT = 99
INPUT = 3
OUTPUT = 4
JUMP_TRUE = 5
JUMP_FALSE = 6
LESS_THAN = 7
EQUALS = 8

OPCODES_NEED_INPUT = [INPUT]

POSITION = 0
IMMEDIATE = 1

class IntCodeComputer:
    def __init__(self, instructions: typing.List[int]):
        self.instructions = instructions
        self.instruction_pointer = 0
        self.input = collections.deque()
        self.output = collections.deque()

    def execute_instruction(self):
        current_instruction = self.instructions[self.instruction_pointer]
        opcode, parameter_modes = self.parse_opcode(current_instruction)
        print(f'Executing OpCode {opcode} @ {self.instruction_pointer}')

        if opcode == ADD:
            return self.opcode_add(parameter_modes)
        elif opcode == MULTIPLY:
            return self.opcode_multiply(parameter_modes)
        elif opcode == INPUT:
            if not self.needs_input():
                return self.opcode_input()
        elif opcode == OUTPUT:
            return self.opcode_output(parameter_modes)
        elif opcode == JUMP_TRUE:
            return self.opcode_jump_true(parameter_modes)
        elif opcode == JUMP_FALSE:
            return self.opcode_jump_false(parameter_modes)
        elif opcode == LESS_THAN:
            return self.opcode_less_than(parameter_modes)
        elif opcode == EQUALS:
            return self.opcode_equals(parameter_modes)
        elif opcode == HALT:
            return self.opcode_halt()

    @staticmethod
    def parse_opcode(opcode: int):
        instruction_value = opcode % 100
        PARAMETER_COUNT_MAP = {
            ADD: 2,
            MULTIPLY: 2,
            INPUT: 0,
            OUTPUT: 1,
            HALT: 0,
            JUMP_TRUE: 2,
            JUMP_FALSE: 2,
            LESS_THAN: 2,
            EQUALS: 2
        }
        parameter_modes = []
        for i in range(2, PARAMETER_COUNT_MAP[instruction_value] + 2):
            mode_int = int(opcode // (math.pow(10,i)) % 2)
            parameter_modes = [mode_int] + parameter_modes

        return instruction_value, parameter_modes

    def opcode_add(self, parameter_modes: list[int]):
        # Read from two positions, store sum in third
        # left position
        left_value = self.get_value(self.instructions[self.instruction_pointer + 1], parameter_modes[1])
        right_value = self.get_value(self.instructions[self.instruction_pointer + 2], parameter_modes[0])

        output_index = self.instructions[self.instruction_pointer + 3]
        total = left_value + right_value
        # print(f'{left_value}+{right_value} = {total} -> {output_index}')

        self.instructions[output_index] = total
        self.instruction_pointer += 4

        return True

    def get_value(self, parameter_value: int, parameter_mode: int) -> int:
        if parameter_mode == POSITION:
            return self.instructions[parameter_value]
        elif parameter_mode == IMMEDIATE:
            return parameter_value

    def opcode_multiply(self, parameter_modes: list[int]):
        # Read from two positions, store product in third
        left_value = self.get_value(self.instructions[self.instruction_pointer + 1], parameter_modes[1])
        right_value = self.get_value(self.instructions[self.instruction_pointer + 2], parameter_modes[0])

        output_index = self.instructions[self.instruction_pointer + 3]
        product = left_value * right_value

        self.instructions[output_index] = product
        self.instruction_pointer += 4

        return True

    def opcode_input(self):
        input_value = self.input.popleft()
        storage_location = self.instructions[self.instruction_pointer + 1]
        self.instructions[storage_location] = input_value
        self.instruction_pointer += 2
        return True

    def opcode_output(self, parameter_modes: list[int]):
        storage_location = self.instructions[self.instruction_pointer + 1]
        output_str = self.get_value(storage_location, parameter_modes[0])
        self.output.append(output_str)
        self.instruction_pointer += 2
        return True

    def opcode_jump_true(self, parameter_modes: list[int]):
        conditional_value = self.get_value(self.instructions[self.instruction_pointer + 1], parameter_modes[1])
        jump_destination = self.get_value(self.instructions[self.instruction_pointer + 2], parameter_modes[0])

        if conditional_value != 0:
            self.instruction_pointer = jump_destination
        else:
            self.instruction_pointer += 3

        return True

    def opcode_jump_false(self, parameter_modes: list[int]):
        conditional_value = self.get_value(self.instructions[self.instruction_pointer + 1], parameter_modes[1])
        jump_destination = self.get_value(self.instructions[self.instruction_pointer + 2], parameter_modes[0])

        if conditional_value == 0:
            self.instruction_pointer = jump_destination
        else:
            self.instruction_pointer += 3

        return True

    def opcode_less_than(self, parameter_modes: list[int]):
        left_value = self.get_value(self.instructions[self.instruction_pointer + 1], parameter_modes[1])
        right_value = self.get_value(self.instructions[self.instruction_pointer + 2], parameter_modes[0])

        output_index = self.instructions[self.instruction_pointer + 3]

        if left_value < right_value:
            self.instructions[output_index] = 1
        else:
            self.instructions[output_index] = 0

        self.instruction_pointer += 4
        return True

    def opcode_equals(self, parameter_modes: list[int]):
        left_value = self.get_value(self.instructions[self.instruction_pointer + 1], parameter_modes[1])
        right_value = self.get_value(self.instructions[self.instruction_pointer + 2], parameter_modes[0])

        output_index = self.instructions[self.instruction_pointer + 3]

        if left_value == right_value:
            self.instructions[output_index] = 1
        else:
            self.instructions[output_index] = 0

        self.instruction_pointer += 4
        return True

    def opcode_halt(self):
        return False

    def run_until_input(self, output=True):
        if self.needs_input():
            return

        while not self.needs_input():
            continue_execution = True
            while continue_execution:
                continue_execution = self.execute_instruction()
                if output:
                    while self.output:
                        message = self.output.popleft()
                        print(message)
            if not self.needs_input():
                break

    def needs_input(self) -> bool:
        current_instruction = self.instructions[self.instruction_pointer]
        opcode, _ = self.parse_opcode(current_instruction)
        if opcode in OPCODES_NEED_INPUT:
            return len(self.input) == 0
        else:
            return False

    def has_halted(self) -> bool:
        current_instruction = self.instructions[self.instruction_pointer]
        opcode, modes = self.parse_opcode(current_instruction)
        return opcode == 99


    def __repr__(self):
        return ','.join([str(i) for i in self.instructions])

class IntCodeScheduler:
    vms: typing.Dict[str, IntCodeComputer]
    connections: typing.Dict[str, typing.List[str]]

    def __init__(self):
        self.vms: typing.Dict[str, IntCodeComputer] = {}
        self.connections: typing.Dict[str, typing.List[str]] = {}
        return

    def add_vm(self, vm_name: str, vm_program: typing.List[int]):
        self.vms[vm_name] = IntCodeComputer(vm_program.copy())
        self.connections[vm_name] = []

    def add_connection(self, input_vm: str, output_vm: str):
        self.connections[output_vm].append(input_vm)

    def run_system(self):
        final_output = None
        while True:
            all_halted = True
            for vm_name, vm_instance in self.vms.items():
                if not vm_instance.has_halted():
                    all_halted = False
                    # print(f'{vm_name} is running')
                    vm_instance.run_until_input(output=False)
                else:
                    # print(f'{vm_name} is halted')
                    break
                while vm_instance.output:
                    output_line = vm_instance.output.popleft()
                    if len(self.connections[vm_name]) == 0:
                        print(output_line)
                        return output_line
                    for connection in self.connections[vm_name]:
                        print(f'Outputting {output_line} to {connection}')
                        self.vms[connection].input.append(output_line)
                        final_output = output_line
            if all_halted:
                return final_output
