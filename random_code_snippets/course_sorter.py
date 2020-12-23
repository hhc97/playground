def print_sorted() -> None:
    """
    Reads courses from courses.txt and prints out a sorted version.
    """
    courses = []
    with open('courses.txt', 'r') as f:
        for line in f:
            courses.append(line.strip())
    courses.sort()
    print(', '.join(courses))


if __name__ == '__main__':
    print_sorted()
