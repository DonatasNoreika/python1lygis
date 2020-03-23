
# Prie kiekvieno sakinio „The Zen of Python tekstu“ žodžio pridėtų šauktuką ir atspausdintų naują sakinį

sakinys = "The Zen of Python"

# naujas = map(lambda x: x + "!", sakinys.split())
# print(" ".join(naujas))

# arba:

naujas = [x + "!" for x in sakinys.split()]
print(" ".join(naujas))

