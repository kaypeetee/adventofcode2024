import re

# Sample Test Input
testInput = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
parsed = testInput.split("mul(")

# Refined Patterns Using Lookarounds
doPattern = r"(?<!\w)do\(\)(?!\w)"
dontPattern = r"(?<!\w)don't\(\)(?!\w)"

# Pattern to Extract Numbers
pattern = r"(\d{1,3}),(\d{1,3})\)"

# Counters and Flags
docount = 0
dontcount = 0
do_flag = True  # Renamed to avoid conflict with the 'do' keyword
total = 0

for index, s in enumerate(parsed):
    print(f"\nProcessing segment {index}: {s}")

    # Search for the number pattern
    match = re.search(pattern, s)
    if match:
        num1, num2 = match.groups()
        print(f"Found numbers: {num1}, {num2}")
        if do_flag:
            total += int(num1) * int(num2)
            print(f"Added to total: {int(num1)} * {int(num2)} = {int(num1)*int(num2)}")
    else:
        print("No number pattern found.")

    # Search for 'do()'
    do_matches = re.findall(doPattern, s)
    if do_matches:
        print(f"'do()' found in segment {index}: {s}")
        do_flag = True
        docount += len(do_matches)

    # Search for "don't()"
    dont_matches = re.findall(dontPattern, s)
    if dont_matches:
        print(f"'don't()' found in segment {index}: {s}")
        do_flag = False
        dontcount += len(dont_matches)

print("\nFinal Counts and Total:")
print(f"'do()' count: {docount}")
print(f"'don't()' count: {dontcount}")
print(f"Total: {total}")