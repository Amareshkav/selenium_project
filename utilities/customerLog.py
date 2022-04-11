import logging


class Loggen:

    @staticmethod
    def loggen():
        logging.basicConfig(filename=r"C:\Users\Balabheem Shivaraj\OneDrive\Desktop\Amaresh_proj\Selenium\Logs\automation.log",format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        return logger

