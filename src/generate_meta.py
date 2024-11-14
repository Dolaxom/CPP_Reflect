from typing import List, Tuple, Optional, TextIO
import re


# File with meta info
gen_file = open("reflect_gen.h", "a")
gen_file.truncate(0)


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
def generate_meta(config: List) -> None:
    gen_file.write('#pragma once\n\n#include"model/model.hpp"\n#include <vector>\n#include <string>\n#include \
<any>\n#include <common/types.hpp>\n\ntemplate<typename T>\nauto GetMeta(T src);\n\n')
    for path in config:
        file = open(path, "r")
        action_file(file)


# File parsing, searching structs and generating meta
def action_file(input_file: TextIO) -> None:
    in_struct_stage: bool = False
    struct_info = None
    for line in input_file:
        struct_name = parse_struct_declaration(line)
        if not in_struct_stage and struct_name[0]:
            struct_info = StructParserInfo(struct_name[1], [])
            in_struct_stage = True
            continue
        
        if in_struct_stage and line.find('};') != -1:
            in_struct_stage = False
            action_struct(struct_info)
            struct_info = None
            continue
        
        if in_struct_stage and struct_info:
            field = parse_field(line)
            if field:
                struct_info.fields.append(field)


# Parses a string with a structure field and returns a tuple (type, name)
def parse_field(line: str) -> Optional[Tuple[str, str]]:
    pattern = r'^\s*(\w[\w\s:<>,]*)\s+(\w+);'
    match = re.match(pattern, line)
    if match:
        field_type = match.group(1).strip()
        field_name = match.group(2).strip()
        return field_type, field_name
    return None


# Parsing the declaration of a struct and extracting its name if it exists
def parse_struct_declaration(line: str) -> Tuple[bool, str]:
    pattern = r'^\s*struct\s+(\w+)'
    match = re.match(pattern, line)
    if match:
        struct_name = match.group(1)
        return tuple([True, struct_name])

    return tuple([False, ""])


def action_struct(struct_info: StructParserInfo) -> None:
    gen_file.write('struct ' + struct_info.struct_name + 'Meta\n{\n')
    gen_file.write('\tstd::vector<std::pair<std::string, std::string>> fields = { ');
    count = len(struct_info.fields)
    counter  = 0
    for field_type, field_name in struct_info.fields:
        counter += 1;
        if (counter != count):
            gen_file.write('{"' + field_type + '", ' + '"' + field_name +'"}, ')
        else:
            gen_file.write('{"' + field_type + '", ' + '"' + field_name +'"}')

    gen_file.write(' };\n')
    gen_file.write('\tstd::vector<std::any> data;\n');
    gen_file.write('};\n\n')

    # GetMeta

    gen_file.write('template<>\nauto GetMeta<' + struct_info.struct_name + '>(' + struct_info.struct_name + ' src)\n{\n')
    gen_file.write('\t' + struct_info.struct_name + 'Meta res;\n\n')
    for field_type, field_name in struct_info.fields:
        gen_file.write('\tres.data.emplace_back(src.' + field_name + ');\n');

    gen_file.write('\n\treturn res;\n}\n\n')


def main():
    config = init_config()
    generate_meta(config)


if __name__ == "__main__":
    main()
