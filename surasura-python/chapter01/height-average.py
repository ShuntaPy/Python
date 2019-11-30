heigths={"taro": 168,"jiro": 171,"takashi": 165}

total=0
for i in heigths.values():
    total += i

average=total/len(heigths)

print("平均身長は{0}cmです。".format(average))
 