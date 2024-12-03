import sys


def main():
    reports = get_reports_data("reports_data.txt")
    asc_desc_reports = validate_asc_or_dsc(reports)
    adj_levels = validate_adjacent_levels(asc_desc_reports)
    n_safe_reports = get_safety_status(asc_desc_reports, adj_levels)
    print(n_safe_reports)


def get_reports_data(file):
    reports = []
    try:
        with open(file) as data:
            for line in data:
                report = line.strip()
                levels = report.split(" ")
                levels_n = []
                for level in levels:
                    levels_n.append(int(level))
                reports.append(levels_n)
        return reports
    except FileNotFoundError:
        sys.exit(f"File not found: {file}")


def validate_asc_or_dsc(reports):
    filtered_reports = []
    for report in reports:
        asc_report = sorted(report)
        dsc_report = sorted(report, reverse=True)
        if report == asc_report or report == dsc_report:
            filtered_reports.append(report)
    return filtered_reports


def validate_adjacent_levels(reports):
    unsafe_reports = []
    for report in reports:
        base_index = 0
        while base_index < len(report) - 1:
            first = int(report[base_index])
            second = int(report[base_index + 1])
            adjacent_diff = abs(first - second)
            if adjacent_diff < 1 or adjacent_diff > 3:
                unsafe_reports.append(report)
                break
            base_index += 1
    return unsafe_reports


def get_safety_status(filtered_reports, unsafe_reports):
    return len(filtered_reports) - len(unsafe_reports)


if __name__ == "__main__":
    main()