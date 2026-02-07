# Setup for the lab environment
CURRENT_WORKING_DIRECTORY = "/home/user/secret/password"
FORBIDDEN_FILE = "/home/user/secret/password/secret_data.txt"


def canonicalize(path):
    # if it doesn't start with / then slap one on the front
    if not path.startswith('/'):
        path = CURRENT_WORKING_DIRECTORY + "/" + path

    # break the path apart to handle dots and slashes
    parts = path.split('/')
    stack = []

    for part in parts:
        if part == "..":
            # go back one directory
            if stack:
                stack.pop()
        elif part == "." or part == "":
            # ignore single dots and empty gaps from double slashes
            continue
        else:
            # just a regular folder or file name
            stack.append(part)

    # put it back together as a clean path
    return "/" + "/".join(stack)


def is_homograph(p1, p2):
    # compare the "clean" versions of both paths
    return canonicalize(p1) == canonicalize(p2)


def run_tests():
    # cases that should point to the same file
    homographs = [
        "secret_data.txt",
        "./secret_data.txt",
        "../password/secret_data.txt",
        "/home/user/secret/password/../../secret/password/secret_data.txt",
        "//home//user/secret/password/secret_data.txt"
    ]

    # cases that should point somewhere else
    non_homographs = [
        "../secret_data.txt",
        "/home/user/secret_data.txt",
        "password/secret_data.txt",
        "././../user/secret/password/data"
    ]

    print(f"Forbidden: {FORBIDDEN_FILE}")
    print(f"CWD: {CURRENT_WORKING_DIRECTORY}\n")

    print("--- Running Homograph Tests ---")
    for test in homographs:
        result = is_homograph(test, FORBIDDEN_FILE)
        print(f"Result: {result} | Path: {test}")

    print("\n--- Running Non-Homograph Tests ---")
    for test in non_homographs:
        result = is_homograph(test, FORBIDDEN_FILE)
        print(f"Result: {result} | Path: {test}")


def main():
    while True:
        print("\n1. Run Automated Tests")
        print("2. Manual Comparison")
        print("3. Exit")

        choice = input("> ")

        if choice == '1':
            run_tests()
        elif choice == '2':
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