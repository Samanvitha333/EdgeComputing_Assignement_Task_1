import csv
from collections import Counter

file_path = "../source/PureEdgeSim/PureEdgeSim/examples/Example1/output/2026-11-21_08-42-34/Sequential_simulation.csv"

with open(file_path, newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

print("=" * 60)
print("PURE EDGESIM - SIMULATION RESULTS SUMMARY")
print("=" * 60)

print("Total scenarios:", len(rows))

print("\nArchitectures:")
print(sorted(set(r["Orchestration architecture"] for r in rows)))

print("\nAlgorithms:")
print(sorted(set(r["Orchestration algorithm"] for r in rows)))

print("\nEdge device counts:")
print(sorted(set(r["Edge devices count"] for r in rows)))

print("\nScenario distribution:")
print(Counter(r["Orchestration architecture"] for r in rows))

print("\n" + "=" * 60)
print("TASK EXECUTION SUMMARY")
print("=" * 60)

for r in rows:
    print(
        f'{r["Orchestration architecture"]:18} | '
        f'{r["Orchestration algorithm"]:12} | '
        f'Devices: {r["Edge devices count"]:3} | '
        f'Generated: {r["Number of generated tasks"]:6} | '
        f'Success: {r["Tasks successfully executed"]:6} | '
        f'Avg delay: {r["Average execution delay (s)"]}'
    )
