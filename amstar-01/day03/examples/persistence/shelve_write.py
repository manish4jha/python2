import shelve

print("\nShelving lists")
s = shelve.open("shelvedata.dat")

s["variety"] = ["sweet", "hot", "dill"]
s["shape"] = ["whole", "spear", "chip"]
s["brand"] = ["Claussen", "Heinz", "Vlassic"]

s.sync()    # make sure data is written

s.close()
