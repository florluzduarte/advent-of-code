import sys

def main():
    left_list, right_list = get_left_and_right_list("list_example.txt")
    sorted_left, sorted_right = get_sorted_lists(left_list, right_list)
    distances = calculate_distance_between_pairs(sorted_left, sorted_right)
    final = get_accumulated_distance(distances)
    print(f"FINAL_DISTANCE: {final}")


def get_left_and_right_list(file):
    left_list = []
    right_list = []
    try:
        with open(file, "r") as lists: 
            for line in lists:
                left_number, right_number = line.split("   ")
                left_list.append(left_number.strip())
                right_list.append(right_number.strip())
        return (left_list, right_list)
    except FileNotFoundError:
        sys.exit(f"File not found: {file}")


def get_sorted_lists(left, right):
    sorted_left = sorted(left)
    sorted_right = sorted(right)
    return (sorted_left, sorted_right)


def calculate_distance_between_pairs(left, right):
    distances = []
    index = 0
    for _ in left:
        distances.append(abs(int(left[index]) - int(right[index])))
        index += 1
    return distances


def get_accumulated_distance(distances):
    total_distance = 0
    for distance in distances:
        total_distance = total_distance + distance
    return total_distance


if __name__ == "__main__":
    main()