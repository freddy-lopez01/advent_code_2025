
def obtain_code(data: list[str], start_postition: int) -> int: 

    curr_position = start_postition

    code = 0

    for instr in data: 
        direction = instr[0]
        val = int(instr[1:])
        # print(direction, val)
        passes = 0
        if direction == "L":
            total = curr_position - val 
            passes = (val - curr_position + 99) // 100
            curr_position = total % 100
        elif direction == "R":
            total = curr_position + val 
            passes = total // 100
            curr_position = total %100
        
        code += passes
        if curr_position == 0:
            code += 1
            
    return code

def main():

    fname = "data/data.txt"

    start_postition = 50

    with open(fname, "r") as f: 
        data = f.readlines()

    print(obtain_code(data, start_postition))
    



if __name__ == "__main__":
    main()
