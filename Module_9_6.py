def all_variants(text):
    value = len(text)
    for j in range(value):
        for g in range(j + 1, value + 1):
            yield text[j:g]


a = all_variants("abc")
for i in a:
    print(i)