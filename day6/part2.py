import os


with open(os.path.join(os.getcwd(), "input.txt"), "r") as stream:
    buffer = list(stream.readline().rstrip("\n"))

counter = 14

while buffer:
    if len(set(buffer[:14])) == 14:
        break
    else:
        del buffer[0]
        counter += 1

print(counter)
