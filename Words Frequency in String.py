s = "hello world hello everyone please don't mind it's our happiness to coding"
res = {}
for word in s.split():
    res[word] = res.get(word, 0) + 1
print(res)
