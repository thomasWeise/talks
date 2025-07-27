"""Enumerate all combinations of numbers 1 to 10."""
mean_lower_or_equal_to_4 = 0  # how often did we find a mean <= 4
total_combinations       = 0  # total number of tested combinations

for i in range(1, 11):             # i goes from 1 to 10
    for j in range(1, i):          # j goes from 1 to i - 1
        for k in range(1, j):      # k goes from 1 to j - 1
            for l in range(1, k):  # l goes from 1 to k - 1
                if ((i + j + k + l) / 4) <= 4:  # check for extreme case
                    mean_lower_or_equal_to_4 += 1  # count extreme case
                total_combinations += 1   # count all combinations

print(f" combinations with mean <= 4: {mean_lower_or_equal_to_4}")
print(f"total number of combinations: {total_combinations}")
