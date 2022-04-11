import configparser

config = configparser.RawConfigParser()
config.read(r"C:\Users\Balabheem Shivaraj\OneDrive\Desktop\Amaresh_proj\Selenium\Configurations\config.ini")

class ReadConfig:

    @staticmethod
    def getApplicationUrl():
        url = config.get("common_info", "base_url")
        return url

    @staticmethod
    def getUsername():
        username = config.get("common_info", "username")
        return username

    @staticmethod
    def getPassword():
        password = config.get("common_info", "password")
        return password


