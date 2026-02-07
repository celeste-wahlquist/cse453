import unicodedata

#establish a map of example homographs
HOMOGRAPH_MAP = {
    "а": "a",  # Cyrillic small a
    "Ь": "b",  # Cyrillic soft sign (looks like b)
    "с": "c",  # Cyrillic small c
    "ԁ": "d",  # Cyrillic small d
    "е": "e",  # Cyrillic small e
    "ｆ": "f",  # Fullwidth latin f
    "ɡ": "g",  # Script latin g
    "һ": "h",  # Cyrillic small shha
    "і": "i",  # Cyrillic small i
    "ј": "j",  # Cyrillic small j
    "ｋ": "k",  # Fullwidth latin k
    "ⅼ": "l",  # Roman numeral fifty
    "ｍ": "m",  # Fullwidth latin m
    "ո": "n",  # Armenian small n
    "ο": "o",  # Greek small omicron
    "р": "p",  # Cyrillic small pe
    "գ": "q",  # Armenian small g
    "г": "r",  # Cyrillic small ghe
    "ѕ": "s",  # Cyrillic small dze
    "ｔ": "t",  # Fullwidth latin t
    "υ": "u",  # Greek small upsilon
    "ⅴ": "v",  # Roman numeral five
    "ԝ": "w",  # Cyrillic small we
    "х": "x",  # Cyrillic small ha
    "у": "y",  # Cyrillic small u
}


def canonicalize(path):
    #if a character in path matches a homograph in our map, replace it with clean char
    path = "".join(HOMOGRAPH_MAP.get(ch, ch) for ch in path)

    #creating empty list of clean path segments
    #and splitting the path into segments depending on '/' position
    parts = path.split('/')
    clean_segments = []

    for part in parts:
        #if we're going up a directory remove the previous directory level from the stack
        if part == "..":
            if clean_segments:
                clean_segments.pop()
        #ignore if we are addressing teh directory we're in or blank segment
        elif part == "." or part == "":
            continue
        else:
            clean_segments.append(part)

    # recreate the given path from the clean_segments
    return "/" + "/".join(clean_segments)

def is_homograph(p1, p2):
    #compare two filepaths after canonicalizing them
    return canonicalize(p1) == canonicalize(p2)

def run_tests():
    forbidden = "/secret/data.txt"
    # Homograph tests, different strings same file
    homographs = ["/ѕecret/data.txt", "/secret/./data.txt", "/var/../secret/data.txt", "/secret//data.txt"]

    #justifications for those writing the report
    #the first homograph has a cyrillic 'ѕ' ($U+0455$) instead of Latin 's'.
    #the second homograph has a redundant '.' which gets ignored by stack logic
    #the third homograph uses '..' so the stack pops that off moving us from var to root before entering secret
    #the fourth has empty segments '//' which the logic ignores to prevent any path errors

    #the test should return true because the canonicalize function converts homograph into true paths before is_homograph compares them
    #when is_homograph says they are the same, it means canonicalize has successfully weeded out homographs to return a legitimate filepath

    print("--- Testing Homographs ---")
    for test in homographs:
        result = is_homograph(test, forbidden)
        print(f"Checking: {test} vs {forbidden} -> Match: {result}")


def main():
    while True:
        print("1. Run Test Cases")
        print("2. Compare Two Paths")
        print("3. Exit")
        choice = input("Select an option: ")
        if choice == '1':
            run_tests()
        elif choice == '2':
            p1 = input("Path 1: ")
            p2 = input("Path 2: ")
            print(f"Homographs? {is_homograph(p1, p2)}")
        elif choice == '3':
            break

if __name__ == '__main__':
    main()
