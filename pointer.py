list = [10,50,30]

print(list)

for idx, value in enumerate(list):
    print(
        "idx:", idx,
        "value:", value,
        "id(value):", id(value),
        "id(list[idx]):", id(list[idx]),
    )