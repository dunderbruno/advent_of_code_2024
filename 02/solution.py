# Part 1

def growing_trend(report):
    passed = True
    for i in range(len(report)-1):
        if report[i]<=report[i+1]:
            continue
        else:
            passed = False
    return passed


def decreasing_trend(report):
    passed = True
    for i in range(len(report)-1):
        if report[i]>=report[i+1]:
            continue
        else:
            passed = False
    return passed


def deviation(report):
    passed = True
    for i in range(len(report)-1):
        if (abs(report[i]-report[i+1]) > 0) and (abs(report[i]-report[i+1]) <=3):
            continue
        else:
            passed = False
    return passed


with open("input.txt", "r") as input_file:
    reports = input_file.readlines()

safe_reports = 0
for report in reports:
    report_int = [int(i) for i in report.split()]
    if growing_trend(report_int):
        if deviation(report_int):
            safe_reports += 1
    elif decreasing_trend(report_int):
        if deviation(report_int):
            safe_reports += 1

print(safe_reports)
