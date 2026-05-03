import importlib
import sys
from importlib.metadata import version
from typing import Any

MISSING: list[str] = []


def check_dependency(name: str, description: str) -> Any:
    try:
        module: Any = importlib.import_module(name)
        mod_version: str = version(name)
        print(f"[OK] {name} ({mod_version}) - {description}")
        return module
    except ModuleNotFoundError:
        MISSING.append(name)
        print(f"[ERR] {name} - not found")
        return None


def check_all_dependencies() -> bool:
    print("Checking dependencies:")
    check_dependency("pandas", "Data manipulation ready")
    check_dependency("numpy", "Numerical computation ready")
    check_dependency("matplotlib", "Visualization ready")
    check_dependency("requests", "Network access ready")
    return len(MISSING) == 0


def print_install_instructions() -> None:
    print("\nMissing dependencies detected. Install them with:\n")
    print("  pip:")
    print("    pip install -r requirements.txt\n")
    print("  Poetry:")
    print("    poetry install")
    sys.exit(1)


def show_package_manager_comparison() -> None:
    print("\nDependency management comparison:")
    print("  pip + requirements.txt:")
    print("    - Simple file listing package names")
    print("    - pip freeze > requirements.txt to pin versions")
    print("    - pip install -r requirements.txt to install")
    print("  Poetry + pyproject.toml:")
    print("    - TOML-based config with version constraints")
    print("    - poetry.lock ensures reproducible builds")
    print("    - poetry install creates isolated environments")
    print("  Installed versions:")
    for mod_name in ["pandas", "numpy", "matplotlib", "requests"]:
        try:
            v: str = version(mod_name)
            print(f"    {mod_name}: {v}")
        except Exception:
            pass


def generate_matrix_data(n: int = 1000) -> Any:
    np: Any = importlib.import_module("numpy")
    pd: Any = importlib.import_module("pandas")
    rng: Any = np.random.default_rng(42)
    return pd.DataFrame({
        "signal":  rng.normal(loc=0.0, scale=1.0, size=n),
        "noise":   rng.uniform(low=-0.5, high=0.5, size=n),
        "anomaly": rng.exponential(scale=0.3, size=n),
    })


def analyze_matrix_data(df: Any) -> Any:
    df["composite"] = df["signal"] + df["noise"] + df["anomaly"]
    return df["composite"].describe()


def generate_visualization(df: Any) -> None:
    plt: Any = importlib.import_module("matplotlib.pyplot")
    plt.figure(figsize=(10, 4))
    plt.plot(df["composite"].values[:200], color="green", linewidth=0.8)
    plt.title("Matrix Signal")
    plt.xlabel("Time")
    plt.ylabel("Signal Strength")
    plt.tight_layout()
    plt.savefig("matrix_analysis.png")
    plt.close()


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")

    if not check_all_dependencies():
        print_install_instructions()

    show_package_manager_comparison()

    print("\nAnalyzing Matrix data...")
    df: Any = generate_matrix_data(1000)
    analyze_matrix_data(df)
    print("Processing 1000 data points...")
    generate_visualization(df)
    print("Generating visualization...\n")

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
