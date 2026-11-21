import pandas as pd
import matplotlib.pyplot as plt

file_path = "../source/PureEdgeSim/PureEdgeSim/examples/Example1/output/2026-11-21_08-42-34/Sequential_simulation.csv"

df = pd.read_csv(file_path)

metrics = [
    "Cloud energy consumption (Wh)",
    "Edge energy consumption (Wh)",
    "Mist energy consumption (Wh)",
    "Energy consumption of computing nodes (Wh)"
]

for metric in metrics:
    df[metric] = pd.to_numeric(df[metric], errors="coerce")

plt.figure(figsize=(12, 7))

for metric in metrics:
    grouped = df.groupby("Edge devices count")[metric].mean()
    plt.plot(
        grouped.index,
        grouped.values,
        marker="o",
        label=metric
    )

plt.title("PureEdgeSim - Energy Consumption vs Edge Devices")
plt.xlabel("Number of Edge Devices")
plt.ylabel("Energy Consumption (Wh)")
plt.grid(True)
plt.legend()
plt.tight_layout()

output_path = "../analysis/energy_consumption.png"
plt.savefig(output_path, dpi=300)

print(f"Graph saved to: {output_path}")
plt.show()
