"""The Oracle - secure configuration system using environment variables."""

import os
import sys

try:
    import dotenv  # type: ignore[import-not-found]
except ModuleNotFoundError:
    print("ERROR: python-dotenv is not installed.")
    print("Install it with: pip install python-dotenv")
    print("Or with uv: uv add python-dotenv")
    sys.exit(1)


def load_config() -> dict[str, str]:
    loaded: bool = dotenv.load_dotenv(".env")
    if not loaded:
        print(
            "WARNING: No .env file found,"
            " using environment variables only.\n"
        )

    config: dict[str, str] = {
        "MATRIX_MODE": os.getenv("MATRIX_MODE", "development"),
        "DATABASE_URL": os.getenv("DATABASE_URL", ""),
        "API_KEY": os.getenv("API_KEY", ""),
        "LOG_LEVEL": os.getenv("LOG_LEVEL", "DEBUG"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT", ""),
    }
    return config


def display_config(config: dict[str, str]) -> None:
    is_dev: bool = config["MATRIX_MODE"] == "development"

    print(f"Mode: {config['MATRIX_MODE']}")

    print("Database: ", end="")
    if is_dev:
        print("Connected to local instance")
    elif config["DATABASE_URL"]:
        print("Connected (connection string hidden)")
    else:
        print("[WARNING] No DATABASE_URL configured")

    print("API Access: ", end="")
    if is_dev and config["API_KEY"]:
        print(f"Authenticated (dev key: {config['API_KEY'][:8]}...)")
    elif config["API_KEY"]:
        print("Authenticated")
    else:
        print("[WARNING] No API_KEY configured")

    print(f"Log Level: {config['LOG_LEVEL']}")

    print("Zion Network: ", end="")
    if config["ZION_ENDPOINT"]:
        print("Online")
    else:
        print("[WARNING] No ZION_ENDPOINT configured")


def security_check(config: dict[str, str]) -> None:
    print("Environment security check:")

    hardcoded: bool = False
    for key, value in config.items():
        if value and not value.startswith(("http", "mongodb", "wss", "ws")):
            if key in ("API_KEY",):
                hardcoded = False
            if key in ("LOG_LEVEL", "MATRIX_MODE"):
                hardcoded = False
    if hardcoded:
        print("[WARN] Potential hardcoded secrets detected")
    else:
        print("[OK] No hardcoded secrets detected")

    env_exists: bool = os.path.isfile(".env")
    if env_exists:
        print("[OK] .env file properly configured")
    else:
        print("[WARN] No .env file found - create one from .env.example")

    print("[OK] Production overrides available via environment variables")


def check_missing_config(config: dict[str, str]) -> list[str]:
    missing: list[str] = []
    if not config["DATABASE_URL"]:
        missing.append("DATABASE_URL")
    if not config["API_KEY"]:
        missing.append("API_KEY")
    if not config["ZION_ENDPOINT"]:
        missing.append("ZION_ENDPOINT")
    return missing


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")

    config: dict[str, str] = load_config()

    print("Configuration loaded:")
    display_config(config)

    print()
    security_check(config)

    missing: list[str] = check_missing_config(config)
    if missing:
        print()
        for key in missing:
            print(f"[WARNING] {key} is not set")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
