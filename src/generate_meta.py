from typing import List, Tuple, TextIO
import re

# Data storage of C++ structures for its parsing
class StructParserInfo:
    def __init__(self, struct_name: str, fields: List[Tuple[str, str]]):
        self.struct_name: str = struct_name
        self.fields: List[Tuple[str, str]] = fields


# Output of the log to the standard output stream
def log(value: any) -> None:
    print("[LOG]\t" + str(value))


# Initializing the config with paths to files
def init_config() -> List:
    config: List = []
    file_conf = open("generate_meta.conf", "r")
    for line in file_conf:
        config.append(line)

    log(config)
    return config


# The main method is the input for meta generation
def generate_meta(config: List, gen_file: TextIO) -> None:
    for path in config:
        file = open(path, "r")
        action_file(file, gen_file)


# File parsing, searching structs and generating meta
def action_file(input_file: TextIO, gen_file: TextIO):
    in_struct_stage: bool = False
    struct_info = StructParserInfo
    for line in input_file:
        struct_name = parse_struct_declaration(line)
        if in_struct_stage == False and struct_name[0] == True:
            struct_info.struct_name = struct_name[1]
            in_struct_stage = True
        elif in_struct_stage == True and line.find('};') != -1:
            in_struct_stage = False
            continue
        else:
            continue

        
        # print(struct_name[1])



# Parsing the declaration of a struct and extracting its name if it exists
def parse_struct_declaration(line: str) -> Tuple[bool, str]:
    pattern = r'^\s*struct\s+(\w+)'
    match = re.match(pattern, line)
    if match:
        struct_name = match.group(1)
        return tuple([True, struct_name])

    return tuple([False, ""])

def main():
    gen_file = open("reflect_gen.h", "w")
    config = init_config()
    generate_meta(config, gen_file)


if __name__ == "__main__":
    main()
