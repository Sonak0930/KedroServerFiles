from kedro.pipeline import node

def add(a,b):
    return a+b

n1=node(add,inputs=["left","right"],outputs="total",name="add_num")
#print("n1 " , n1.run({"left":2, "right":3 }))

n2=node(add,{"a": "left","b":"right"},"total")
print("n2 ",n2.run({"left":2, "right":3}))

def extremes(values):
    return min(values), max(values)

n3 = node(extremes, "values", ["minimum","maximum"], name="find_extreme")
print("n3 ",n3.run({"values":[141,2,34,234,234,233264,234,324]}))