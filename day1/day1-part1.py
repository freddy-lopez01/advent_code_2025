import re

def obtain_code(data: list[str], start_postition: int) -> int: 

    curr_position = start_postition

    code = 0

    for instr in data: 
        m = re.match(r"([A-Za-z]+)(\d+)", instr.strip("\n"))
        direction, value = m.groups()
        val = int(value)
        # print(direction, val)
        if direction == "L":
            curr_position = (curr_position - val) %100
        elif direction == "R":
            curr_position = (curr_position + val) %100
        
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
