# Single Line
# - take a line of c/c++ code
# - insert it into a basic c file with common libraries and a main function
# - insert a print statement that prints the result of that line
# - compile that file with gcc
# - run that file

# Multiline
# - repeat single line, 
# - each time appending the new line and potential print statement to the same file

# import os
import subprocess

def get_print_statement(line):
    # TODO: use regex to better recognize assignment operator
    exprs = line.split(" = ")
    var = exprs[0].split()[1].strip()
    return f"printf(\"%d\\n\", {var});\n"

base_file = "base_file.c"
repl_file = "repl_file.c"
insert_index = 6

while True:
    line = input("> ").strip() + "\n"
    if line == "exit()":
        break
    
    print_line = get_print_statement(line)

    with open(base_file, "r") as f:
        base_lines = f.readlines()

    # TODO: remove/overwrite print statement in consecutive repl entry
    base_lines.insert(insert_index + 1, line)
    base_lines.insert(insert_index + 2, print_line)
    new_file_string = "".join(base_lines)

    with open(repl_file, "w") as f:
        f.write(new_file_string)
        
    subprocess.call(["gcc", "-std=c99", f"{repl_file}", "-o", "repl_executable"])
    subprocess.call("./repl_executable")
    
    # remove print line
    base_lines.pop(insert_index + 2)
    new_file_string = "".join(base_lines)
    
    with open(repl_file, "w") as f:
        f.write(new_file_string)
        
    insert_index += 1
    base_file = repl_file