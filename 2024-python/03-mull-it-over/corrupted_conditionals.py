from corrupted import get_codes, get_muls, get_muls_values, get_individual_results, get_final_result
import re


def main():
    corrupted_codes = get_codes("example_data.txt")
    data_stream = generate_data_stream(corrupted_codes)
    do_stream = get_do_muls(data_stream)
    muls = get_muls(do_stream)
    values = get_muls_values(muls)
    results = get_individual_results(values)
    final = get_final_result(results)
    print(final)


def generate_data_stream(corrupted_codes):
    stream = ""
    for list in corrupted_codes:
        stream = stream + list
    return stream + "don't()"


def get_do_muls(stream):
    do_stream = ""
    first_do, _ = stream.split("don't()", maxsplit=1)
    do_stream = do_stream + first_do
    rest = re.findall(r"(don't\(\).*)", stream)
    do_parts = re.findall(r"((?:do\(\).*?)(?:don't\(\).*?))+", rest[0])
    for do in do_parts:
        do_stream = do_stream + do
    return [do_stream]


if __name__ == "__main__":
    main()
