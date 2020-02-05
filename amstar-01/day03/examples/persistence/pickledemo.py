import pickle

print("Pickling lists")

variety = ["sweet", "hot", "dill"]
shape   = ["whole", "spear", "chip"]
brand   = ["Claussen", "Heinz", "Vlassic"]
f       = open("pickles1.dat", "wb")

pickle.dump(variety, f)
pickle.dump(shape, f)
pickle.dump(brand, f)
pickle.dump(variety + brand + shape, f)

f.close()


