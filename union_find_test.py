import weighted_quick_union

file1 = ".\\tinyUF.txt"
file2 = ".\mediumUF.txt"
file3 = ".\largeUF.txt"

union_operations = []
with open(file2, "r") as f:
    line = f.readline()
    quick_find = weighted_quick_union.WeightedQuickUnion(int(line.replace("\\n", "")))
    quick_find.print()
    for line in enumerate(f.readlines()):
        pair = line[1].split(" ")
        union_operations.append((int(pair[0]), int(pair[1].replace("\\n", ""))))

print(union_operations)
for op in union_operations:
    print(f"Union({op[0]},{op[1]})")
    quick_find.union(op[0], op[1])
    quick_find.print()
