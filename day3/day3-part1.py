
def arrange_batteries(cell: str) -> str: 
    cell_len = len(cell)
    largest = 0
    second = 0
    for n in range(len(cell)): 
        if cell[n] == "\n":
            break
        dig = int(cell[n])
        if dig == largest: 
            second = dig
        elif dig > largest:
            if n != cell_len -2: 
                largest = dig
                second = 0
            else:
                second = dig
        elif largest > dig > second:
            second = dig

    return str(largest) + str(second)

def main():

    fname = "data/data.txt"
    res = []
    with open(fname, "r") as f: 
        data = f.readlines()
    for cell in data: 
        max_combo = arrange_batteries(cell)
        res.append(int(max_combo))
    print(res)

    print(sum(res))

    



if __name__ == "__main__":
    main()

