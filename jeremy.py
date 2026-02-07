



# Convert path to single \ then compare
def canonicalization(path):
    while "\\\\" in path:
        path = path.replace("\\\\", "\\")
    return path

# Split path into parts seperated by the backslash then compare parts
# . or .. will determine to ignore or skip
def homograph(path):

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




    
def intro():
    print("Hi, please enter filepath 1: ")
    file_path1 = input()

    print("Enter filepath 2: ")
    file_path2 = input()

    result1 = compare(file_path1)
    result2 = compare(file_path2)

    # Now compare results
    if result1 == result2:
        print("The paths are homographs")
    else:
        print("The paths are NOT homographs")



START = "home\\user\\cse453"
TARGET = "home\\user\\secret\\password.txt"

def compare(user_input):

    # 1. attach START to users input
    full = START + "\\" + user_input

    # 2. Canonicalize 
    new_path = homograph(canonicalization(full))

    print("Filepath:", new_path)
    
    return new_path



def main():
    print("\n\n\n")
    # Intro function
    intro()

    # Test 1
    same = "..\\\secret\\password.txt"
    print("\n\n\n") # test path

    same = canonicalization(same)
    print(same) # get rid of extra slashes

    actual_path = homograph(same)  # show path
    print("Actual path:", actual_path)


    # Test 2
    same = "home\\user\\..\\user\\secret\\password.txt"
    print("\n\n\n") # test path

    same = canonicalization(same)
    print(same) # get rid of extra slashes

    actual_path = homograph(same)  # show path
    print("Actual path:", actual_path)







if __name__ == '__main__':
    main()
