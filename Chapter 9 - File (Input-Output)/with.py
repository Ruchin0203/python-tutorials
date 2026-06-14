f = open("file.txt")
data = f.read()
print(data)
f.close()

# the same can be written using with statement like this.
with open("file.txt") as f:
    print(f.read())

# you don't have to explicitly close the file. Aa j faydo chhe with statement no.