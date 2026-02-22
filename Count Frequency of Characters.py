def char_frequency(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

string = input("Enter a string: ")
frequency = char_frequency(string)
print("Character frequencies:")
for char, count in frequency.items():
    print(f"{char}: {count}")
