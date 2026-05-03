import os
import sys
import dotenv

def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")

    print("Configuration loaded:")
    correct: bool = dotenv.load_dotenv(".env")
    g_dev: bool = False
    g_db: bool = False
    g_api: bool = False
    g_zion: bool = False
    if (not correct):
        print("Something happened")
    matrix_mode: str = os.getenv('MATRIX_MODE') or "development"
    if (matrix_mode == "development"):
        g_dev = True
    print("Mode: " + matrix_mode)

    database_url: str = os.getenv('DATABASE_URL') or ""
    if (database_url):
        g_db = True
    print("Database: ", end="")
    if (g_dev):
        database_url = "mongodb://localhost:27017/"
        print("DEVELOPMENT MODE, using dev db, ", end="")
        print("mongodb://localhost:27017/")
    elif (database_url and not g_dev):
        print("Connected in prod. Database hidden")

    api_key: str = os.getenv('API_KEY') or ""
    if (api_key):
        g_api = True
    print("API Access: ", end="")
    if (g_dev):
        print("DEVELOPMENT MODE, api key shown: ", end="")
        print(api_key)
    else:
        print("Api Key verified")

    log_level: str = os.getenv('LOG_LEVEL') or "DEBUG"
    print("Log Level: " + log_level)

    zion_endpoint: str = os.getenv('ZION_ENDPOINT') or ""
    if (zion_endpoint):
        g_zion = True
    print("Zion Network: ", end="")
    if (g_dev):
        print(f"Endpoint `{zion_endpoint}` is online")
    else:
        print("Online")
    print()
    print()




if __name__ == "__main__":
    main()
