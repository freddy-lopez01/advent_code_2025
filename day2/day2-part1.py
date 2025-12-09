def parse_range(data: str) -> list[int]:
    sequence = data.strip().split("-")
    start, end = int(sequence[0]), int(sequence[1])
    invalid_ids = []

    for n in range(start, end + 1):
        num_str = str(n)
        if len(num_str) % 2 == 0 and num_str[:len(num_str)//2] == num_str[len(num_str)//2:]:
            invalid_ids.append(n)
    return invalid_ids


def main():

    fname = "day2/data/data-real.txt"

    with open(fname, "r") as f: 
        data = f.readlines()

    data_split = data[0].split(",")
    all_inval_ids = []
    for code in data_split: 
        # print(code)
        res = parse_range(code)
        if res: 
            all_inval_ids += res

    list_sum = sum(all_inval_ids)

    return print(list_sum)


if __name__ == "__main__":
    main()

