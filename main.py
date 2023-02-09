INPUT_FILE = "template_file.txt"
OUTPUT_FILE = "processed_file.txt"


def get_vars() -> dict:
    input_file = open(INPUT_FILE, "r", encoding="utf-8")
    vars: dict = {}
    for line in input_file:
        if line[0] == "*":
            splitted_line = line.split(" ")  # ["*key", "value", etc.]
            key = splitted_line[0].replace("*", "")
            without_key = splitted_line[1:]  # ["value\n" or "value, value\n", etc.]
            without_n = without_key[-1].strip()  # last "value" in list without \n
            value = " ".join(without_key[:-1] + [without_n])  # ["Vasya" + "Ivanov"]
            vars.update({key: value})
    return vars


def replace(vars: dict):
    input_file = open(INPUT_FILE, "r", encoding="utf-8")
    output_file = open(OUTPUT_FILE, "w", encoding="utf-8")
    file_copy = input_file.readlines()
    for key, value in vars.items():
        for line in file_copy:
            if line.find(key):
                processed_line = line.replace(f"!{key}!", value)
                file_copy[file_copy.index(line)] = processed_line
    output_file.write(" ".join(file_copy))


def main():
    vars = get_vars()
    replace(vars)


if __name__ == "__main__":
    main()
