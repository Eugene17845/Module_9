def all_variants(text):
    value = len(text)
    for j in range(1, value+1):
        for g in range(value-j+1):
            yield text[g:g+j]


a = all_variants("abc")
for i in a:
    print(i)
