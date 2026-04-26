import random,math,copy
import numpy as np
import pandas as pd

def generate_data(n):
    data=[]
    for i in range(n):
        data.append({"id":i+1,"marks":random.randint(40,100),"attendance":random.randint(60,100),"scores":[random.randint(10,25),random.randint(10,25)]})
    return data

def mutate(data,roll):
    r=roll%3
    if r==0:
        r=1
    for i in range(len(data)):
        if i%r==0:
            m=data[i]["marks"]
            data[i]["marks"]=int(m+math.sqrt(m))
            data[i]["attendance"]-=5
            data[i]["scores"][0]+=2
    return data

def analyze(orig,mod):
    o=[x["marks"] for x in orig]
    m=[x["marks"] for x in mod]
    mean=np.mean(m)
    std=np.std(m)
    drift=abs(np.mean(o)-mean)
    manual_mean=sum(m)/len(m)
    return mean,std,drift,manual_mean

def classify(drift,threshold,orig,after_shallow):
    if orig!=after_shallow:
        return "Copy Failure Detected"
    elif drift<threshold:
        return "Stable Data"
    elif drift<threshold*2:
        return "Minor Drift"
    else:
        return "Critical Drift"

roll=2411001591

data=generate_data(12)

shallow=data.copy()
deep=copy.deepcopy(data)

mutate(shallow,roll)
mutate(deep,roll)

df_orig=pd.DataFrame(data)
df_shallow=pd.DataFrame(shallow)
df_deep=pd.DataFrame(deep)

norm=(df_deep["marks"]-df_deep["marks"].min())/(df_deep["marks"].max()-df_deep["marks"].min())
df_deep["normalized_marks"]=norm

mean,std,drift,manual_mean=analyze(data,deep)

threshold=5
result=classify(drift,threshold,data,shallow)

print("Original DataFrame")
print(df_orig)

print("\nShallow Copy Result")
print(df_shallow)

print("\nDeep Copy Result")
print(df_deep)

print("\nDrift Value")
print(drift)

print("\nTuple (mean, drift, std_dev)")
print((mean,drift,std))

print("\nFinal Classification")
print(result)
