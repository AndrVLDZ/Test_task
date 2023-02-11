from typing import List


INPUT_FILE = "template_file.txt"
OUTPUT_FILE = "processed_file.txt"


def read_file() -> List[str]:
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        return f.readlines()


def write_file(line: str):
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(line)


def find_vars(lines: str) -> dict:
    vars: dict = {}
    for line in lines:
        if line[0] == "*":
            key, value = line.replace("*", "").replace("\n", "").split(" ", 1)
            vars[key] = value
    return vars


def replace(lines: List[str], vars: dict):
    data = "".join(lines)
    for key, value in vars.items():
        # edited variable is still iterable,
        # I haven't found a solution to this problem yet 
        data = data.replace(f"!{key}!", value)
    write_file(data)


def main():
    lines = read_file()
    vars = find_vars(lines)
    replace(lines, vars)


if __name__ == "__main__":
    main()
