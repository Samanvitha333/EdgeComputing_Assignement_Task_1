import csv

file_path = "PureEdgeSim/examples/Example1/output/2026-11-21_08-42-34/Sequential_simulation.csv"

with open(file_path, newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

print("\nARCHITECTURE | ALGORITHM | DEVICES | SUCCESS RATE (%)")
print("-" * 65)

for r in rows:
    generated = int(r["Number of generated tasks"])
    successful = int(r["Tasks successfully executed"])

    success_rate = (successful / generated) * 100 if generated else 0

    print(
        f'{r["Orchestration architecture"]:18} | '
        f'{r["Orchestration algorithm"]:12} | '
        f'{r["Edge devices count"]:7} | '
        f'{success_rate:10.2f}%'
    )
