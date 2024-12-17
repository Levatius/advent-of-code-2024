from dataclasses import dataclass, field
from math import floor


@dataclass
class Computer:
    a: int
    b: int
    c: int
    instruction_pointer: int = 0
    outputs: list[int] = field(default_factory=list)

    @classmethod
    def from_lines(cls, lines: list[str]):
        register_values = [int(line.split(": ")[1]) for line in lines]
        return cls(*register_values)

    def combo(self, operand: int) -> int:
        match operand:
            case 0 | 1 | 2 | 3:
                return operand
            case 4:
                return self.a
            case 5:
                return self.b
            case 6:
                return self.c

    def run_instruction(self, opcode, operand):
        match opcode:
            case 0:  # adv
                self.a = floor(self.a / 2 ** self.combo(operand))
            case 1:  # bxl
                self.b ^= operand
            case 2:  # bst
                self.b = self.combo(operand) % 8
            case 3:  # jnz
                if self.a != 0:  # Program stops looping when self.a reaches 0
                    self.instruction_pointer = operand - 2  # Minus 2 to counteract the usual pointer increase
            case 4:  # bxc
                self.b ^= self.c
            case 5:  # out
                self.outputs.append(self.combo(operand) % 8)
            case 6:  # bdv
                self.b = floor(self.a / 2 ** self.combo(operand))
            case 7:  # cdv
                self.c = floor(self.a / 2 ** self.combo(operand))
        self.instruction_pointer += 2

    def run_program(self, program, cycle_once=False):
        while self.instruction_pointer < len(program) - 1:
            opcode = program[self.instruction_pointer]
            operand = program[self.instruction_pointer + 1]
            self.run_instruction(opcode, operand)
            if cycle_once and (opcode == 3 and operand == 0):
                break


def parse(lines):
    split_index = lines.index("")
    computer = Computer.from_lines(lines[:split_index])
    program = list(map(int, lines[split_index + 1].split(": ")[1].split(",")))
    return computer, program


def part_1(computer, program):
    computer.run_program(program)
    return ",".join(map(str, computer.outputs))


def part_2(_, program):
    def find_int_a_solutions(current_oct_a, program_index):
        """
        Implementation details of input program:
        - Assumes 0,3 is in the program for simpler digit finding
        - Assumes steps are only dependent on the state of A (i.e. that B and C are recalculated using just A)
        """
        solutions = []
        desired_output = program[program_index]
        for i in range(8):
            oct_a = current_oct_a + str(i)
            int_a = int(oct_a, 8)

            computer = Computer(int_a, 0, 0)  # Does not matter what B and C are set to
            computer.run_program(program, cycle_once=True)
            if computer.outputs[-1] != desired_output:
                continue

            if program_index > 0:
                new_solutions = find_int_a_solutions(oct_a, program_index - 1)
                solutions.extend(new_solutions)
            else:
                # Index has reached 0 => Solution found
                solutions.append(int_a)
        return solutions

    int_a_solutions = find_int_a_solutions(current_oct_a="0o", program_index=len(program) - 1)
    return min(int_a_solutions)
