



# Convert path to single \ then compare
def fix_slashes(path):
    while "\\\\" in path:
        path = path.replace("\\\\", "\\")
    return path

# Split path into parts seperated by the backslash then compare parts
# . or .. will determine to ignore or skip
def test(path):

    skip = 0
    actual = []

    while True:
        x = path.rfind("\\")     # Find last backslash

        if x == -1:             # No backslash left 
            part = path         # Use the rest of the path
            path = ""           
        else:
            part = path[x+1:]     # Take out the last part - after last \
            path = path[:x]       # Remaining path         - before last \

        if part == "" or part == ".":   # current directory
            pass                        # ignore

        elif part == "..":         # parent directory
            skip += 1              # cancel next folder 

        else:
            if skip > 0:
                skip -= 1             # cancel this folder and reset skip
            else:
                actual.insert(0, part) # keep this folder in canonical path

        if path == "": 
            break

    return "\\".join(actual)   # return as string



# Add function to compare
# Add function for intro
# Add function for test cases

def main():


    # Test 1
    same = "..\\\secret\\password.txt"
    print("\n\n\n") # test path

    same = fix_slashes(same)
    print(same) # get rid of extra slashes

    actual_path = test(same)  # show path
    print("Actual path:", actual_path)


    # Test 2
    same = "home\\user\\..\\user\\secret\\password.txt"
    print("\n\n\n") # test path

    same = fix_slashes(same)
    print(same) # get rid of extra slashes

    actual_path = test(same)  # show path
    print("Actual path:", actual_path)


if __name__ == '__main__':

    main()
