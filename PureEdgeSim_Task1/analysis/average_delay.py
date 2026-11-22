import pandas as pd
import matplotlib.pyplot as plt

file_path = "../source/PureEdgeSim/PureEdgeSim/examples/Example1/output/2026-11-21_08-42-34/Sequential_simulation.csv"

df = pd.read_csv(file_path)

# Average request makespan
metric = "Average execution delay (s)"

# Convert values to numeric
df[metric] = pd.to_numeric(df[metric], errors="coerce")

# Plot
plt.figure(figsize=(12, 7))

for (architecture, algorithm), group in df.groupby(
    ["Orchestration architecture", "Orchestration algorithm"]
):
    group = group.sort_values("Edge devices count")

    plt.plot(
        group["Edge devices count"],
        group[metric],
        marker="o",
        label=f"{architecture} - {algorithm}"
    )

plt.title("PureEdgeSim - Average Request Makespan")
plt.xlabel("Number of Edge Devices")
plt.ylabel("Average Request Makespan (seconds)")
plt.grid(True)
plt.legend(fontsize=8)
plt.tight_layout()

output_path = "../analysis/average_request_makespan.png"
plt.savefig(output_path, dpi=300)

print(f"Graph saved to: {output_path}")

plt.show()

