import importlib
from importlib.metadata import version
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def import_print(module) -> None:
    name: str = module.__name__
    mod_version: str = version(module.__name__)
    print(f"[OK] {name} ({mod_version}) - ", end="")


def try_import(name: str) -> None:
    try:
        module = importlib.import_module(name)
        import_print(module)
        if (name == 'numpy'):
            print("Numerical computation ready")
        elif (name == 'matplotlib'):
            print("Visualization ready")
        elif (name == 'pandas'):
            print("Data manipulation ready")
        elif (name == 'requests'):
            print("Numerical computation ready")
    except ModuleNotFoundError:
        print(f"[ERR] Could not find {name}")


def test_imports() -> None:
    print("Checking dependencies:")
    try_import("pandas")
    try_import("numpy")
    try_import("requests")
    try_import("matplotlib")


def generate_matrix_data(n: int = 1000) -> pd.DataFrame:
    rng = np.random.default_rng(42)
    return pd.DataFrame({
        "signal":    rng.normal(loc=0.0, scale=1.0, size=n),
        "noise":     rng.uniform(low=-0.5, high=0.5, size=n),
        "anomaly":   rng.exponential(scale=0.3, size=n),
    })


def analyze_matrix_data(df: pd.DataFrame) -> pd.Series:
    df["composite"] = df["signal"] + df["noise"] + df["anomaly"]
    return df["composite"].describe()


def generate_visualization(df: pd.DataFrame) -> None:
    plt.plot(df["composite"].values[:200], color="green", linewidth=0.8)
    plt.title("Matrix Signal")
    plt.savefig("matrix_analysis.png")
    plt.close()


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")
    test_imports()
    print()
    df = generate_matrix_data(1000)
    print("Analyzing Matrix data...")
    analyze_matrix_data(df)
    print("Processing 1000 data points...")
    generate_visualization(df)
    print("Generating visualization...\n")

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
