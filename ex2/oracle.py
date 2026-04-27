import os
import sys
import dotenv

def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")

    print("Configuration loaded:")
    correct: bool = dotenv.load_dotenv(".env")
    if (not correct):
        print("Something happened")
    matrix_mode: str | None = os.getenv('MATRIX_MODE')
    if (not matrix_mode):
        matrix_mode = "development"
    database_url: str | None = os.getenv('DATABASE_URL')
    api_key: str | None = os.getenv('API_KEY')
    log_level: str | None = os.getenv('LOG_LEVEL')
    zion_endpoint: str | None = os.getenv('ZION_ENDPOINT')



if __name__ == "__main__":
    main()
