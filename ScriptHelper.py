import inspect
import sys
from pathlib import Path

class LoggerHelper:

    @staticmethod
    def get_current_file_path():
        return inspect.getfile(inspect.currentframe())

    @staticmethod
    def get_current_file_name():
        return Path(LoggerHelper.get_current_file_path()).name

    @staticmethod
    def get_current_function_name():
        return inspect.currentframe().f_code.co_name

    @staticmethod
    def get_current_function_args():
        frame = inspect.currentframe()
        return inspect.getargvalues(frame).args

    @staticmethod
    def get_calling_function_name():
        return sys._getframe(2).f_code.co_name

    @staticmethod
    def get_calling_file_path():
        return sys._getframe(2).f_code.co_filename

    @staticmethod
    def get_calling_file_name():
        return Path(LoggerHelper.get_calling_file_path()).name

    @staticmethod
    def get_calling_function_line_number():
        return sys._getframe(2).f_lineno

# Example usage
if __name__ == "__main__":
    def sample_function():
        print("Current file path:", LoggerHelper.get_current_file_path())
        print("Current file name:", LoggerHelper.get_current_file_name())
        print("Current function name:", LoggerHelper.get_current_function_name())
        print("Current function arguments:", LoggerHelper.get_current_function_args())
        print("Calling function name:", LoggerHelper.get_calling_function_name())
        print("Calling file path:", LoggerHelper.get_calling_file_path())
        print("Calling file name:", LoggerHelper.get_calling_file_name())
        print("Calling function line number:", LoggerHelper.get_calling_function_line_number())

    def calling_function():
        sample_function()

    calling_function()
