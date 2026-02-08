
cwd = "/home/user/cse453/"
forbidden = "/home/user/cse453/secret_data.txt"

def canonicalize(path):
    # "Create a canonicalization function to convert an encoding (the input path) into some canon."

    #establishing absolute directory if one was not provided
    if not path.startswith("/"):
        if cwd.endswith("/"):
            path = cwd + path
        #not currently needed, but if the cwd was differently formatted (ex. "/home/user/cse453"
        # the program would have ensured it was properly appended to the front with a separating /
        # else:
        #     path = cwd + "/" + pat

    #split the path according to '/' position
    parts = path.split('/')
    stack = []

    for part in parts:
        if part == "..":
            # if go back one directory indicator, remove one directory level from stack
            if stack:
                stack.pop()
        elif part == "." or part == "":
            # ignore single dots and empty gaps from double slashes
            continue
        else:
            # just a regular folder or file name gets added to stack
            stack.append(part)

    # put stack back together as a path
    return "/" + "/".join(stack)


def is_homograph(p1, p2):
    # "Create a homograph function that determines if two file paths are the same. It should make use of the work done by the canonicalization function."
    # "This function should return True or False to indicate whether the two encodings are the same."
    # note that if provided paths are not the same ex.(secret_data.txt and /home/user/cse453/secret_data.txt) the canon adjusts the directories to be absolute
    c1 = canonicalize(p1)
    c2 = canonicalize(p2)

    return c1 == c2


def run_tests():
    # "Write a function to compare each of your homograph test cases against a forbidden file path to demonstrate that they are the same."
    homographs = [
        "secret_data.txt",
        #this is a direct match
        "./secret_data.txt",
        #./ references the current directory, so it's basically the filename by itself
        "/home/user/cse453/secret_data.txt",
        # the exact filepath with directory
        "../cse453/secret_data.txt",
        #goes up one directory then re-enters that same directory
        "secret/../secret_data.txt",
        # enters secret, exits secret
        "/home/user/cse453/./secret_data.txt",
        #. referencing current directory, so we stay in cse453
        "/home/user/cse453/temp/../secret_data.txt",
        #goes up a directory getting rid of invalid directory "temp" then enters a valid directory
        "//home//user//cse453//secret_data.txt"
        #because of how cannonicalize function looks at this, it will simplify to home/user/cse453/secret_data.txt
    ]

    # "Write a function to compare each of your non-homograph test cases against a forbidden file path to demonstrate that they are different"
    non_homographs = [
        "../secret_data.txt",
        #goes up a directory then tries to reference secret_data.txt from a different location that doesn't contain secret_data.txt
        "/home/user/secret_data.txt",
        # directory path missing cse453
        "password/secret_data.txt",
        # "password" isn't a folder
        "././../cse453/password/secret_data.txt",
        # enter present directory, enter same directory, go up directory try password, which isn't valid directory
        "secret_data_backup.txt",
        #non-existent file
        "/home/user/cse453/secret/secret_data.txt"
        #no "secret" folder exists
    ]

    print(forbidden)
    print(cwd)

    print ("homograph tests")
    for test in homographs:
        result = is_homograph(test, forbidden)
        print(f"Result: {result} | Path: {test}")

    print("non_homograph tests")
    for test in non_homographs:
        result = is_homograph(test, forbidden)
        print(f"Result: {result} | Path: {test}")


def main():
    while True:
        print("1. Run Automated Tests")
        print("2. Manual Comparison")
        print("3. Exit")
        choice = input("> ")
        if choice == '1':
            run_tests()
        elif choice == '2':
            print("note that if the given path begins with '/' the program will assume it is a complete (absolute) directory")
            path1 = input("Enter first path: ")
            path2 = input("Enter second path: ")
            if is_homograph(path1, path2):
                print("Result: These are homographs")
            else:
                print("Result: These are different files")
        elif choice == '3':
            print("Exiting...")
            break


if __name__ == '__main__':
    main()