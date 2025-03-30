import sys
import logging

class CustomException(Exception):
    """Custom exception class to capture errors with detailed information."""
    
    def __init__(self, error_message: str, error_detail: sys):
        super().__init__(error_message)
        self.error_message = CustomException.format_error_message(error_message, error_detail)

    @staticmethod
    def format_error_message(error_message: str, error_detail: sys) -> str:
        """Formats error messages to include filename and line number."""
        _, _, exc_tb = error_detail.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
        return f"Error in '{file_name}', line {line_number}: {error_message}"

    def __str__(self):
        return self.error_message


if __name__ == "__main__":
    try:
        a = 1/0  # This will cause a ZeroDivisionError

    except Exception as e:
        logging.info("Divide by zero error")
        raise CustomException(str(e), sys)
