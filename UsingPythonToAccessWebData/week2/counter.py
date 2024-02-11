import re

txt: str = open("data/regex_sum_1977923.txt").read()

sum: int = 0
for num in re.findall(r"[0-9]+", txt):
    sum += int(num)
print("sum:", sum)
