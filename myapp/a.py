a = {"dict":[{"username":"汤晓宁","sex":"女"},{"username":"小小汤","sex":"女"},{"username":"赵萌呀","sex":"男"}]}
for i in a.values():
    for k in i:
        print(k["username"])