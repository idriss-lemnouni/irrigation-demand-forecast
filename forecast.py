import csv
import sys
from collections import defaultdict
from datetime import date, timedelta
from statistics import linear_regression, mean

sites = defaultdict(dict)
with open(sys.argv[1], encoding="utf-8-sig", newline="") as stream:
    for row in csv.DictReader(stream):
        sites[row["site"]][date.fromisoformat(row["date"])] = float(row["et0_pm_mm"])

for name, values in sorted(sites.items()):
    pairs = [(values[day], values[day + timedelta(days=1)]) for day in sorted(values)
             if day + timedelta(days=1) in values]
    cutoff = len(pairs) * 3 // 4
    slope, intercept = linear_regression(*zip(*pairs[:cutoff]))
    test = pairs[cutoff:]
    persistence = mean(abs(y - x) for x, y in test)
    model = mean(abs(y - max(0, intercept + slope * x)) for x, y in test)
    print(f"{name}: {len(test)} test days, MAE persistence {persistence:.3f}, regression {model:.3f} mm/day")
