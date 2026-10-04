import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "results/contamination_experiment.csv"
)

plt.figure(figsize=(8, 5))

plt.plot(
    df["contamination"] * 100,
    df["anomalies_detected"],
    marker="o"
)

plt.xlabel("Contamination (%)")
plt.ylabel("Number of anomalies detected")
plt.title("Effect of Contamination on Anomaly Detection")

plt.xticks([1, 2, 5])

plt.tight_layout()

plt.savefig(
    "results/contamination_experiment.png",
    dpi=300
)

plt.show()