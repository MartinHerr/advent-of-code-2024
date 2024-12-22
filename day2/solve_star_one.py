#!/usr/bin/env python3
def parse_input(input):
    reports = []
    for report in input.readlines():
        report = report.strip("\n").split(" ")
        reports.append([int(level) for level in report])
    return reports

def is_safe_report(report):
    first_diff = report[1] - report[0]
    if abs(first_diff) > 3:
        return False
    for i, _ in enumerate(report[1:-1]):
        diff = report[i + 2] - report[i + 1]
        if abs(diff) > 3:
            return False
        if diff * first_diff <= 0:
            return False
    return True

def count_safe_reports(reports):
    count = 0
    for report in reports:
        if is_safe_report(report):
            count += 1
    return count

if __name__ == "__main__":
    with open("input.txt") as input:
        reports = parse_input(input)
    # for report in reports[:10]:
    #     print(f"{report} | {is_safe_report(report)}")
    #     print(report[1:-1])
    print(count_safe_reports(reports))