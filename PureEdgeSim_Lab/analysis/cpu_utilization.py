import pandas as pd
import matplotlib.pyplot as plt

file_path = "../source/PureEdgeSim/PureEdgeSim/examples/Example1/output/2026-11-21_08-42-34/Sequential_simulation.csv"

df = pd.read_csv(file_path)

metrics = [
    "Average CPU usage (%)",
    "Average CPU usage (Cloud) (%)",
    "Average CPU usage (Edge) (%)",
    "Average CPU usage (Mist) (%)"
]

plt.figure(figsize=(12, 7))

for metric in metrics:
    df[metric] = pd.to_numeric(df[metric], errors="coerce")

for architecture, group in df.groupby("Orchestration architecture"):
    group = group.sort_values("Edge devices count")
    plt.plot(
        group["Edge devices count"],
        group["Average CPU usage (%)"],
        marker="o",
        label=architecture
    )

plt.title("PureEdgeSim - Average CPU Utilization")
plt.xlabel("Number of Edge Devices")
plt.ylabel("Average CPU Usage (%)")
plt.grid(True)
plt.legend()
plt.tight_layout()

output_path = "../analysis/cpu_utilization.png"
plt.savefig(output_path, dpi=300)

print(f"Graph saved to: {output_path}")
plt.show()
