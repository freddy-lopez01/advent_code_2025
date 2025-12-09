
def is_invalid_code(num: int) -> bool:

    num_str = str(num) 
    for size in range(1, len(num_str) // 2 +1):
        if len(num_str) % size != 0:
            continue  
        substring = num_str[:size]
        val = len(num_str) // size
        if substring * val == num_str: 
            return True
    return False


def parse_range(data: str) -> list[int]:
    sequence = data.strip().split("-")
    start, end = int(sequence[0]), int(sequence[1])
    invalid_ids = []
    for n in range(int(start), int(end) + 1):
        if is_invalid_code(n):
            invalid_ids.append(n)
    return invalid_ids


def main():

    fname = "data/data-real.txt"

    with open(fname, "r") as f: 
        data = f.readlines()

    data_split = data[0].split(",")
    all_inval_ids = []
    for code in data_split: 
        res = parse_range(code)
        if res: 
            all_inval_ids += res

    print(all_inval_ids)
    list_sum = sum(all_inval_ids)

    return print(list_sum)


if __name__ == "__main__":
    main()


