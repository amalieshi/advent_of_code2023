if __name__ == "__main__":
    # Part 1
    data_path = "../data/day1/example_2.txt"

    with open(data_path, "r") as f:
        doc = f.readlines()

    doc = [i.rstrip("\n") for i in doc]

    numerical_list = []
    for i in doc:
        character = list(i)
        numerical = [str(int(j)) for j in character if j.isdigit()]
        if len(numerical) > 2:
            numerical = [numerical[0], numerical[-1]]
        if len(numerical) == 1:
            numerical = [numerical[0] * 2]
        numerical = "".join(numerical)
        numerical_list.append(int(numerical))
    result = sum(numerical_list)
    print(result)
