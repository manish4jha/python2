import pickle

print("\nUnpickling lists")
f = open("pickles1.dat", "rb")

v = pickle.load(f)
s   = pickle.load(f)
b   = pickle.load(f)
print(variety)
print(shape)
print(brand)

f.close()
