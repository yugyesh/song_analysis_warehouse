from configparser import ConfigParser

# reading config file
config = ConfigParser()
config.read_file(open("./dwh.cfg"))


KEY = config.get("AWS", "KEY")
SECRET = config.get("AWS", "SECRET")

DWH_DB = config.get("DWH", "DWH_DB")
DWH_DB_USER = config.get("DWH", "DWH_DB_USER")
DWH_DB_PASSWORD = config.get("DWH", "DWH_DB_PASSWORD")
DWH_PORT = config.get("DWH", "DWH_PORT")

DWH_ENDPOINT = config.get("DWH", "DWH_ENDPOINT")
DWH_ROLE_ARN = config.get("DWH", "DWH_ROLE")
