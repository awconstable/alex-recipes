import time


def output_x(letter, times):
    x_output = ""
    for i in range(times):
        x_output = x_output + letter
    print(x_output)
    time.sleep(0.25)


count = 0
for l in "abcdefghijklmnopqrstuvwxyz123456789!?":
    count = count + 1
    output_x(l, count)

