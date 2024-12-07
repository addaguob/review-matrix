"""
Test main function in review_matrix module

These tests check the main function in review_matrix module.
The main function is the entry point of the program and it parses the command line arguments
and initiates the matrix for the provided modules.
"""

import unittest
from unittest.mock import patch
from review_matrix.review_matrix import main
from review_matrix.review_matrix import CYAN, RED


class TestMainFunction(unittest.TestCase):

    @patch("sys.argv", ["review_matrix.py"])
    def test_main_with_no_args(self):
        with patch("builtins.print") as mock_print:
            main()
            mock_print.assert_called_with(
                f"{CYAN}\nInitiating matrix for: \nreview_matrix.py"
            )  # It will find itself if no arguments are provided

    @patch("sys.argv", ["review_matrix.py", "test_module.py"])
    def test_main_with_module_arg(self):
        with patch("builtins.print") as mock_print:
            main()
            mock_print.assert_called_with(
                f"{CYAN}\nInitiating matrix for: \n" f"{'test_module.py'}"
            )

    @patch("sys.argv", ["review_matrix.py", "test_module.txt"])
    def test_main_with_non_python_module_arg(self):
        with patch("builtins.print") as mock_print:
            main()
            mock_print.assert_called_with(
                f"{RED}The module provided should be a .py file."
                "\nUsage: python review_matrix.py <path_to_module.py>"
            )

    @patch("sys.argv", ["review_matrix.py", "../review_matrix/_private_module.py"])
    def test_main_with_private_module_arg(self):
        with patch("builtins.print") as mock_print:
            main()
            mock_print.assert_called_with(
                f"{CYAN}\nInitiating matrix for: \n../review_matrix/_private_module.py"
            )

    @patch("sys.argv", ["review_matrix.py", "non_existent_module.py"])
    def test_main_with_non_existent_module_arg(self):
        with patch("builtins.print") as mock_print:
            main()
            mock_print.assert_called_with(
                f"{RED}The module provided does not exist"
                "\nUsage: python review_matrix.py <path_to_module.py>"
            )


if __name__ == "__main__":
    unittest.main()
