import numpy as np

def calculate(list):
    if len(list) !=9:
        raise ValueError("List must contain nine numbers.")
    list= np.array(list)
    list=list.reshape(3,3)
    
    calculations = {
        'mean': (np.mean(list,axis=0).tolist(), np.mean(list, axis=1).tolist(), np.mean(list)),
        'variance':(np.var(list,axis=0).tolist(), np.var(list, axis=1).tolist(), np.var(list)),
        'standard deviation':(np.std(list,axis=0).tolist(), np.std(list, axis=1).tolist(), np.std(list)),
        'max':(np.max(list,axis=0).tolist(), np.max(list, axis=1).tolist(), np.max(list)),
        'min':(np.min(list,axis=0).tolist(), np.min(list, axis=1).tolist(), np.min(list)),
        'sum':(np.sum(list,axis=0).tolist(), np.sum(list, axis=1).tolist(), np.sum(list))
    }

    return calculations

print("Please input nine numbers in the following format: 0 1 2 3)
numbers = input()
list = [int(x) for x in input().split()]
results = calculate(list)
print(results)
