import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

def plot_time_series(df, output_path: Path):
    sns.lineplot(data=df, x="Year", y="number_of_courses", marker="o")
    plt.title("Historical Evolution of AI Programs in Brazil")
    plt.xlabel("Year")
    plt.ylabel("Number of Programs")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
