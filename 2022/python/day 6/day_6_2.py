import time
def get_marker():
    start_time = time.time()
    with open("day 6/day_6_input.txt", "r") as file:
        content = file.read()
        prev_four = []
        counter = 1
        for letter in content:
            if len(prev_four) < 14:
                prev_four.append(letter)
            if len(prev_four) == 14:
                for i, item in enumerate(prev_four):
                    if item in prev_four[i + 1:]:
                        prev_four.pop(0)
                        break
                    if i == 13:
                        end_time = time.time()
                        print(f"elapsed time = {end_time - start_time}")
                        return counter
            counter += 1



print(get_marker())