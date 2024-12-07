"""A CLI matrix reviewer during lunch break to skim through python modules
in a current directory.

Usage: python review_matrix.py
Usage: python review_matrix.py <path_to_module.py>
"""

import os
import sys
import time
import random

REVIEW_SPEED_VARIATION = (0.100, 0.250, 0.500)
RED = "\033[0;31m"
GREEN = "\033[0;32m"
LIGHT_GREEN = "\033[1;32m"
ORANGE = "\033[0;33m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"

# Color for echo command---Codes-----Usage
# Black---------------------0;30-----'\033[0;30m'
# Dark Gray-----------------1;30-----'\033[1;30m'
# Red-----------------------0;31-----'\033[0;31m'
# Light Red-----------------1;31-----'\033[1;31m'
# Green---------------------0;32-----'\033[0;32m'
# Light Green---------------1;32-----'\033[1;32m'
# Brown/Orange--------------0;33-----'\033[0;33m'
# Yellow--------------------1;33-----'\033[1;33m'
# Blue----------------------0;34-----'\033[0;34m'
# Light Blue----------------1;34-----'\033[1;34m'
# Purple--------------------0;35-----'\033[0;35m'
# Light Purple--------------1;35-----'\033[1;35m'
# Cyan----------------------0;36-----'\033[0;36m'
# Light Cyan----------------1;36-----'\033[1;36m'
# Light Gray----------------0;37-----'\033[0;37m'
# White---------------------1;37-----'\033[1;37m'


def main(testing=True):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    has_no_errors = True
    not_done = True
    while not_done:
        modules_dict = {}
        # If there's only one argument, add all the python files
        if len(sys.argv) == 1:
            # Add to lines all the files in
            # the directory that ends with .py
            for module in os.listdir(current_dir):
                # Review only non-private python modules
                if module.endswith(".py") and not module.startswith("_"):
                    module_path = current_dir + "/" + module
                    lines = []
                    total_linenumbers = 0
                    with open(module_path, encoding="utf-8") as f:
                        # Add all the lines in the current file
                        for line_txt in f.readlines():
                            lines.append(line_txt)
                            total_linenumbers += 1
                    # Add the filename, its total lines and its content
                    # to the dictionary of modules
                    modules_dict.update({module: [total_linenumbers, lines]})
        else:
            # Loop through all the arguments provided by user
            for module in sys.argv[1:]:
                if not os.path.exists(module):
                    print(
                        f"{RED}The module provided does not exist"
                        "\nUsage: python review_matrix.py <path_to_module.py>"
                    )
                    has_no_errors = False
                    if not testing:
                        input("Press enter to exit...")
                        sys.exit(1)
                elif not module.endswith(".py"):
                    print(
                        f"{RED}The module provided should be a .py file."
                        "\nUsage: python review_matrix.py <path_to_module.py>"
                    )
                    has_no_errors = False
                else:
                    lines = []
                    total_linenumbers = 0
                    with open(module, encoding="utf-8") as f:
                        # Add all the lines in the current file
                        for line_txt in f.readlines():
                            lines.append(line_txt)
                            total_linenumbers += 1
                    # Add the filename, its total lines and its content
                    # to the dictionary of modules
                    modules_dict.update({module: [total_linenumbers, lines]})

        if has_no_errors:
            print(
                f"{CYAN}\nInitiating matrix for: \n" f"{'\n'.join(modules_dict.keys())}"
            )

        if not testing:
            print("Enjoy your lunch break!")
            for module, (total_line_nums, lines) in modules_dict.items():
                print(
                    f"{LIGHT_GRAY}Reviewing {module} " f"with {total_line_nums} lines:"
                )
                found_triquotes = False
                for line_no, line in enumerate(lines):
                    print(f"{LIGHT_GRAY}{line_no+1: 4d}/{total_line_nums}| ", end="")
                    # Print line contents in green
                    if line.lstrip().startswith("#"):
                        print(f"{RED}{line}", end="")
                    elif '"""' in line or found_triquotes:
                        print(f"{ORANGE}{line}", end="")
                        # Reset if there are pairs of triple quotes
                        if (
                            '"""' in line
                            and found_triquotes
                            or (line.count('"""') % 2 == 0 and not found_triquotes)
                        ):
                            found_triquotes = False  # Reset
                        else:
                            # Found only one, and wait another
                            found_triquotes = True
                    else:
                        print(f"{GREEN}{line}", end="")
                    time.sleep(random.choice(REVIEW_SPEED_VARIATION))
        else:
            # Skip endless loop for reviewing modules matrices.
            not_done = False


if __name__ == "__main__":
    main(testing=False)
