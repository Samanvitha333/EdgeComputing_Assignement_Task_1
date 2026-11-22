import pandas as pd
import matplotlib.pyplot as plt

file_path = "../report/pureedgesim_results.csv"
df = pd.read_csv(file_path)

df["Success Rate (%)"] = (
    df["Tasks successfully executed"] /
    df["Number of generated tasks"] * 100
)

plt.figure(figsize=(14, 8))

for (architecture, algorithm), group in df.groupby(
    ["Orchestration architecture", "Orchestration algorithm"]
):
    group = group.sort_values("Edge devices count")

    plt.plot(
        group["Edge devices count"],
        group["Success Rate (%)"],
        marker="o",
        label=f"{architecture} - {algorithm}"
    )

plt.title("PureEdgeSim - Task Success Rate")
plt.xlabel("Number of Edge Devices")
plt.ylabel("Task Success Rate (%)")
plt.grid(True)
plt.legend(fontsize=8)
plt.tight_layout()

output_path = "../report/task_success_rate_verified.png"
plt.savefig(output_path, dpi=300)

print(f"Graph saved to: {output_path}")
print("\nSuccess rate data:")
print(
    df[[
        "Orchestration architecture",
        "Orchestration algorithm",
        "Edge devices count",
        "Success Rate (%)"
    ]].round(2).to_string(index=False)
)

plt.show()
