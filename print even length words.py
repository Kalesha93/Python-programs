s = "Python is great"
wrds = s.split()
even_wrds = filter(lambda w: len(w) % 2 == 0, wrds)
res = " ".join(even_wrds)
print(res)
