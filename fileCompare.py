import filecmp

fileA = "./textA.txt"
fileB = "./textB.txt"

comparison = filecmp.cmp(fileA, fileB)
if comparison:
    print("Both metadatas are equal")
else:
    print("Metadatas are different")

comparison = filecmp.cmp(fileA, fileB, True)
if comparison:
    print("Both metadatas and contents are equal")
else:
    print("Both metadatas or contents are different")

filecmp.clear_cache()
print("======== END TEST CASE ========")