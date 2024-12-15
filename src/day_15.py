from dataclasses import dataclass, field

MOVEMENTS = {"^": -1 + 0j, ">": 0 + 1j, "v": 1 + 0j, "<": 0 - 1j}
OTHER_PART_OF_BOX_DELTA = {"[": 0 + 1j, "]": 0 - 1j}


@dataclass
class Warehouse:
    robot: complex | None = None
    walls: set[complex] = field(default_factory=set)
    boxes: dict[complex, str] = field(default_factory=dict)

    def get_cascading_boxes(self, root_box, direction):
        if root_box not in self.boxes:
            return set()
        boxes = {root_box}
        # Add the other part of the box if we need to
        if (box_value := self.boxes[root_box]) in {"[", "]"} and direction in {-1 + 0j, 1 + 0j}:
            other_part_of_box = root_box + OTHER_PART_OF_BOX_DELTA[box_value]
            boxes.add(other_part_of_box)
        for box in boxes:
            more_boxes = self.get_cascading_boxes(box + direction, direction)
            boxes = boxes.union(more_boxes)
        return boxes

    def move_robot(self, direction):
        next_position = self.robot + direction
        if next_position in self.walls:
            # Ouch!
            return
        elif next_position in self.boxes:
            boxes = self.get_cascading_boxes(next_position, direction)
            for box in boxes:
                if box + direction in self.walls:
                    # A box in the cascadable boxes cannot move => None can move
                    return
            else:
                # Move the cascadable boxes
                boxes_to_add_back = {}
                for box in boxes:
                    boxes_to_add_back[box + direction] = self.boxes.pop(box)
                self.boxes.update(boxes_to_add_back)
        self.robot = next_position


    def gps_total(self):
        return sum(100 * position.real + position.imag for position, box in self.boxes.items() if box in ("O", "["))


def parse(lines, expand):
    split_index = lines.index("")
    warehouse = Warehouse()
    for a, line in enumerate(lines[:split_index]):
        if expand:
            line = line.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")
        for b, item in enumerate(line):
            position = complex(a, b)
            match item:
                case "#":
                    warehouse.walls.add(position)
                case "O" | "[" | "]":
                    warehouse.boxes[position] = item
                case "@":
                    warehouse.robot = position
    movements = [MOVEMENTS[movement_char] for movement_char in "".join(lines[split_index + 1:])]
    return warehouse, movements


def part_1(warehouse, movements):
    for movement in movements:
        warehouse.move_robot(movement)
    return warehouse.gps_total()


def part_2(warehouse, movements):
    for movement in movements:
        warehouse.move_robot(movement)
    return warehouse.gps_total()
