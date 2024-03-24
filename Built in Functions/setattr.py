#myclass
class Compuy:
    name = "Javascript"
    brnd = "apple"

print(getattr(Compuy, "brnd"))
setattr(Compuy, "brnd", "Walton")
print(getattr(Compuy, "brnd"))

# print(getattr(Compuy, "brndx"))
print(Compuy.__dict__)