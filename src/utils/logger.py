import logging
import os

def setup_logger(log_file="D:/Vishnu files/LawSmartt/logs/lawsmart.log"):
    logger = logging.getLogger("ChatbotLogger")

    # Avoid duplicate handlers
    if not logger.handlers:
        # Ensure the logs directory exists
        os.makedirs(os.path.dirname(log_file), exist_ok=True)

        # Create file handler with UTF-8 encoding
        handler = logging.FileHandler(log_file, mode='a', encoding='utf-8')

        # Define log format
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        # Add handler to logger
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

    return logger
