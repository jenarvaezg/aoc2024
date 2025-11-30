from copy import copy


with open("../inputs/day09.txt") as f:
    lines = [x.strip() for x in f.read().splitlines()]

memory: list[int | None] = []
file = True
file_id = 0
for x in lines[0]:
    num = int(x)
    if file:
        for _ in range(num):
            memory.append(file_id)
        file_id += 1
        file = False
    else:
        for _ in range(num):
            memory.append(None)
        file = True


def checksum(memory):
    total = 0
    for i, v in enumerate(memory):
        if v:
            total += i * v

    return total


def defrag(memory: list[int | None]) -> list[int | None]:
    start = 0
    end = len(memory) - 1
    while True:
        while start < end and memory[start] is not None:
            start += 1
            # print(f"Moving start forward to {start}")

        while start < end and memory[end] is None:
            end -= 1
            # print(f"Moving end backwards to {end}")

        if start >= end:
            return [x for x in memory if x is not None]

        memory[start], memory[end] = memory[end], memory[start]


def defrag_whole(memory: list[int | None]) -> list[int | None]:
    p_file = len(memory) - 1
    id_num = max(x for x in memory if x is not None)

    while id_num >= 0:
        # pull p_file back
        while 0 < p_file and memory[p_file] != id_num:
            p_file -= 1
        if p_file == 0:
            return memory
        # find size of file
        p_temp = p_file
        while memory[p_temp] == id_num:
            p_temp -= 1
        file_size = p_file - p_temp
        # find first free block to fit file
        for p_free in range(0, p_file - file_size + 1):
            if all(memory[p_free + k] is None for k in range(file_size)):
                # move file
                for k in range(file_size):
                    memory[p_free + k], memory[p_file - k] = (
                        memory[p_file - k],
                        memory[p_free + k],
                    )
                break
        p_file -= file_size
        id_num -= 1

    return memory


print(checksum(defrag(copy(memory))))
print(checksum(defrag_whole(copy(memory))))
