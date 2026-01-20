
import random
import math


names = input("Enter customer names (comma-separated): ")


names_list = names.split(",")

clean_names = list(set(name.strip() for name in names_list))


random.shuffle(clean_names)


winners = random.sample(clean_names, 2)


reversed_winners = []
for name in winners:
    reversed_winners.append(name[::-1])


count = len(clean_names)

rounded_sqrt = round(math.sqrt(count))

print("\n Lucky Draw Results ")
print("Unique participants:", clean_names)
print("Total participants:", count)
print("Winners:", winners)
print("Reversed winner names:", reversed_winners)
print("Rounded square root of participants:", rounded_sqrt)
