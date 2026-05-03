import sys
import os
import site

executable: str = sys.executable


def in_venv() -> bool:
    return sys.prefix != sys.base_prefix


def run_venv() -> None:
    venv_path: str = sys.prefix
    venv_path_folder: str = os.path.basename(venv_path)
    site_pack_folder: str = site.getsitepackages()[0]

    print("MATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {executable}")
    print(f"Virtual Environment: {venv_path_folder}")
    print(f"Environment Path: {venv_path}\n")

    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.\n")

    print(f"Package installation path: {site_pack_folder}")


def run_no_venv() -> None:
    print("MATRIX STATUS: You're still plugged in\n")

    print(f"Current Python: {executable}")
    print("Virtual Environment: None detected\n")

    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")

    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate\t# On Unix")
    print("matrix_env\\Scripts\\activate\t# On Windows")


def main() -> None:
    if in_venv():
        run_venv()
    else:
        run_no_venv()


if __name__ == "__main__":
    main()
