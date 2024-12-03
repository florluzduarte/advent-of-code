from safe_reports import get_reports_data


def main():
    reports = get_reports_data("reports_data.txt")
    no_duplicates = filter_duplicates(reports)
    unsafe = validate_adjacents(no_duplicates)
    print(unsafe)


def filter_duplicates(reports):
    no_duplicates = []
    for report in reports:
        for i in range(len(report) - 1):
            ammount = report.count(report[i])
            if ammount > 1 and ammount < 3:
                report.remove(report[i])
        no_duplicates.append(report)
    return no_duplicates


def validate_adjacents(reports):
    unsafe_reports = []
    for report in reports:
        i = 0
        while i < len(report) - 1:
            first = report[i]
            second = report[i + 1]
            adjacent_diff = abs(first - second)
            if adjacent_diff < 1:
                unsafe_reports.append(report)
                break
            if adjacent_diff > 3:
                if second == len(report) - 1:
                    break
                third = report[i + 2]
                far_diff = abs(first - third)
                if far_diff < 1 or far_diff > 3:
                    unsafe_reports.append(report)
                    break
            i += 1
    return unsafe_reports


if __name__ == "__main__":
    main()