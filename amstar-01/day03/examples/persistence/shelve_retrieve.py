import shelve

s = shelve.open("shelvedata.dat")

print("\nRetrieving lists from a shelved file:")
print("brand -", s["brand"])
print("shape -", s["shape"])
print("variety -", s["variety"])
s.close()

input("\n\nPress the enter key to exit.")
