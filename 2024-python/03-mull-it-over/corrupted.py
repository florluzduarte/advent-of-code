import re, sys


def main():
    corrupted_codes = get_codes("example_data.txt")
    muls_filtered = get_muls(corrupted_codes)
    all_values = get_muls_values(muls_filtered)
    results = get_individual_results(all_values)
    final_count = get_final_result(results)
    print(final_count)


def get_codes(file):
    corrupted_codes = []
    try:
        with open(file) as codes:
            for line in codes:
                corrupted_codes.append(line.strip())
        return corrupted_codes
    except FileNotFoundError:
        sys.exit(f"File not found: {file}")
    

def get_muls(codes):
    muls_filtered = []
    for code in codes:
        muls = re.findall(r"(mul\([0-9]{1,3},[0-9]{1,3}\))", code)
        for mul in muls:
            muls_filtered.append(mul)
    return muls_filtered


def get_muls_values(muls_filtered):
    all_values = []
    for mul in muls_filtered:
        values = re.findall(r"[0-9]{1,3},[0-9]{1,3}", mul)
        all_values.append(values)
    return all_values
    

def get_individual_results(all_values):
    results = []
    for i in range(len(all_values)):
            value = all_values[i][0]
            astr, bstr = value.split(",")
            result = int(astr) * int(bstr)
            results.append(result)
    return results


def get_final_result(results):
    counter = 0
    for result in results:
        counter = counter + result
    return counter


if __name__ == "__main__":
    main()