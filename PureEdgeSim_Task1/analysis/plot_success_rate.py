import csv
import matplotlib.pyplot as plt

file_path = "PureEdgeSim/examples/Example1/output/2026-11-21_08-42-34/Sequential_simulation.csv"

with open(file_path, newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

# Focus on TRADE_OFF algorithm
rows = [r for r in rows if r["Orchestration algorithm"] == "TRADE_OFF"]

architectures = sorted(set(r["Orchestration architecture"] for r in rows))
device_counts = [100, 200, 300]

plt.figure(figsize=(12, 7))

for architecture in architectures:
    rates = []

    for device_count in device_counts:
        row = next(
            r for r in rows
            if r["Orchestration architecture"] == architecture
            and int(r["Edge devices count"]) == device_count
        )

        generated = int(row["Number of generated tasks"])
        successful = int(row["Tasks successfully executed"])

        rate = (successful / generated) * 100
        rates.append(rate)

    plt.plot(device_counts, rates, marker="o", label=architecture)

plt.title("Task Success Rate vs Edge Device Count (TRADE_OFF)")
plt.xlabel("Number of Edge Devices")
plt.ylabel("Task Success Rate (%)")
plt.xticks(device_counts)
plt.grid(True)
plt.legend(bbox_to_anchor=(1.02, 1), loc="upper left")
plt.tight_layout()

output_file = "~/PureEdgeSim_Lab/analysis/success_rate_trade_off.png"
plt.savefig(
    output_file.replace("~", __import__("os").path.expanduser("~")),
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Graph saved successfully.")
