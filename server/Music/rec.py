import dill as pickle

f = open("mrec.pkl", "rb")
p = f.read()
pickle.loads(p)
print(p)