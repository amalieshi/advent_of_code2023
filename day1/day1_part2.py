from part2_func import multipleReplace


if __name__ == "__main__":
    digit = "one, two, three, four, five, six, seven, eight, nine"
    digit = digit.split(", ")
    digit_numerical = ["o1e", "t2o", "t3e", "f4r", "f5e", "s6x", "s7n", "e8t", "n9e"]

    digit_numerical = [str(i) for i in digit_numerical]
    digit_dict = {digit[i]: digit_numerical[i] for i in range(len(digit))}
    data_path = r"../data/day1/example_4.txt"

    with open(data_path, "r") as f:
        doc = f.readlines()

    doc = [i.rstrip("\n") for i in doc]

    new_doc = []
    # Convert the text into numerical
    for msg in doc:
        new_msg = multipleReplace(msg, digit_dict)
        new_doc.append(new_msg)

    numerical_list = []
    for i in new_doc:
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
