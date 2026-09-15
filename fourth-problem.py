vowels = "aeiouAEIOU"


def count_vowels(str):
    count = 0
    for char in str:
        if char in vowels:
            count += 1
    return count

print(count_vowels("JavaScript"))
