from dataclasses import dataclass, field


@dataclass
class File:
    id: int
    size: int


@dataclass
class Block:
    id: int
    size: int
    files: list[File] = field(default_factory=list)
    modified: bool = False

    @property
    def available(self):
        return self.size - sum(file.size for file in self.files)

    @property
    def checksum(self):
        total = 0
        file_position = 0
        for file in self.files:
            positions_sum = file.size * (self.id + file_position) + int((file.size - 1) * file.size / 2)
            total += positions_sum * file.id
            file_position += file.size
        return total


def parse(line):
    blocks = []
    block_id = 0
    for i, size_str in enumerate(line):
        if (size := int(size_str)) == 0:
            continue
        block = Block(block_id, size)
        if i % 2 == 0:
            block.files.append(File(id=i // 2, size=size))
        blocks.append(block)
        block_id += size
    return blocks


def part_1(blocks):
    search_start = 0
    for j, file_block in enumerate(reversed(blocks)):
        search_end = len(blocks) - j
        if search_start >= search_end:
            break
        while file_block.files:
            if file_block.modified:
                break
            file = file_block.files.pop()
            for i, free_block in enumerate(blocks[search_start:search_end]):
                if free_block.available == 0:
                    search_start += 1
                    continue
                size_to_move = min(file.size, free_block.available)
                free_block.files.append(File(file.id, size_to_move))
                free_block.modified = True
                file.size -= size_to_move
                if file.size == 0:
                    break
    return sum(block.checksum for block in blocks)


def part_2(blocks):
    search_start = 0
    for j, file_block in enumerate(reversed(blocks)):
        search_end = len(blocks) - j
        if search_start >= search_end:
            break
        while file_block.files:
            if file_block.modified:
                break
            file = file_block.files.pop()
            for i, free_block in enumerate(blocks[search_start:search_end]):
                if free_block.available < file.size:
                    continue
                free_block.files.append(file)
                free_block.modified = True
                break
    return sum(block.checksum for block in blocks)
