def arrange_batteries(cell_code: str) -> int: 
    cell = list(cell_code.strip())
    # print(cell)
    cr = 0
    while len(cell) > 12:
        print(f"cr: {cr}")
        print(f"cell: {cell}")
        print(cell[cr])
        if cr == len(cell) - 1: 
            if cell[cr] > cell[cr-1]:
                del cell[cr-1]
            else: 
                del cell[cr]
            cr = 0
            continue
        if cell[cr+1] > cell[cr]:
            del cell[cr]
            cr -= 1
        cr += 1

    result = int("".join(cell))
    return result 

def main():

    fname = "data/data.txt"
    with open(fname, "r") as f: 
        data = f.readlines()
    totals = []
    for cell in data: 
        max_combo = arrange_batteries(cell)
        print(max_combo)
        totals.append(max_combo)

    print(totals)
    print(sum(totals))
    
    if sum(totals) == 3121910778619: 
        print("Example result and code result match!")


if __name__ == "__main__":
    main()


