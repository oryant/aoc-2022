import os


def find_marker(buffer: list, length: int) -> int:
    count = length
    while buffer:
        if len(set(buffer[:length])) == length:
            break
        else:
            del buffer[0]
            count += 1
    return count


with open(os.path.join(os.getcwd(), "input.txt"), "r") as stream:
    buffer = list(stream.readline().rstrip("\n"))

print(find_marker(buffer, 4))
