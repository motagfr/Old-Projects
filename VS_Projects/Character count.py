article = "In Syria, Trump Distills a Foreign Policy of Impulse, and Faces the Fallout By Peter Baker and Lara Jakes (NYTimes) Oct. 10, 2019 WASHINGTON — No one should have been surprised, and yet it seems that everyone was. President Trump made clear long ago that he wanted to get out of the Middle East, … … … . At the same time, the Kurds have been counterattacking, firing off shells at Turkish border villages as the danger of escalation spiralled."

# Find the most repeated letter.
d = dict()
s = set()

for char in article:
    s.add(char)
for char in s:
    d[char] = 0

for char in article:
    for key in d.keys():
        if char == key:
            d[char] += 1

d

sorted_dic = sorted((value, key) for (key, value) in d.items())
sorted_dic
type(sorted_dic)
sorted_dic[-1:]
[(key, value) for (key, value) in d.items()]

# Another way
d1 = dict()
for char in article:
    if char in d1.keys():
        d1[char] += 1
    else:
        d1[char] = 1

d1
