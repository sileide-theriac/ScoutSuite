# Sileide De Freitas Theriac
# CS 464 - Assignment 3 Report - Testing

import unittest
from ScoutSuite import run_from_cli


class TestCase(unittest.TestCase):
    def test1(self):
        # Testing for Authentication failure with credentials.
        input = 2
        expected = None
        self.assertEqual(run_from_cli(input), expected,
                         msg="run_from_cli({}) expected {}, got {}"
                         .format(input, expected, run_from_cli(input)))

    def test2(self):
        # Testing for Authentication failure with credentials.
        input = 101
        expected = "Authentication failure"
        self.assertEqual(run_from_cli(input), expected,
                         msg="run_from_cli({}) expected {}, got {}"
                         .format(input, expected, run_from_cli(input)))

    def test3(self):
        # Testing for Initialization failure with Cloud Providers.
        input = 'AWS'
        expected = 1
        self.assertEqual(run_from_cli(input), expected,
                         msg="run_from_cli({}) expected {}, got {}"
                         .format(input, expected, run_from_cli(input)))

    def test4(self):
        # Testing for Initialization failure with Cloud Providers.
        input = None
        expected = "Initialization failure"
        self.assertEqual(run_from_cli(input), expected,
                         msg="run_from_cli({}) expected {}, got {}"
                         .format(input, expected, run_from_cli(input)))

    def test5(self):
        # Testing for Report initialization failure.
        input = 100
        expected = "Report initialization failure"
        self.assertEqual(run_from_cli(input), expected,
                         msg="run_from_cli({}) expected {}, got {}"
                         .format(input, expected, run_from_cli(input)))

    def test6(self):
        # Testing for Report initialization failure.
        input = 103
        expected = "Report created"
        self.assertEqual(run_from_cli(input), expected,
                         msg="run_from_cli({}) expected {}, got {}"
                         .format(input, expected, run_from_cli(input)))

    def test7(self):
        # Testing List of Cloud Providers
        input = "Amazon Web Services"
        expected = True
        self.assertEqual(run_from_cli(input), expected,
                         msg="run_from_cli({}) expected {}, got {}"
                         .format(input, expected, run_from_cli(input)))

    def test8(self):
        # Testing List of Cloud Providers
        input = "Microsoft Azure"
        expected = True
        self.assertEqual(run_from_cli(input), expected,
                         msg="run_from_cli({}) expected {}, got {}"
                         .format(input, expected, run_from_cli(input)))

    def test9(self):
        # Testing List of Cloud Providers
        input = "Google Cloud Platform"
        expected = True
        self.assertEqual(run_from_cli(input), expected,
                         msg="run_from_cli({}) expected {}, got {}"
                         .format(input, expected, run_from_cli(input)))

    def test10(self):
        # Testing List of Cloud Providers
        input = "Alibaba Cloud"
        expected = True
        self.assertEqual(run_from_cli(input), expected,
                         msg="run_from_cli({}) expected {}, got {}"
                         .format(input, expected, run_from_cli(input)))

    def test11(self):
        # Testing List of Cloud Providers
        input = "Oracle Cloud Infrastructure"
        expected = True
        self.assertEqual(run_from_cli(input), expected,
                         msg="run_from_cli({}) expected {}, got {}"
                         .format(input, expected, run_from_cli(input)))

    def test12(self):
        # Testing List of Cloud Providers
        input = "Apple Store"
        expected = False
        self.assertEqual(run_from_cli(input), expected,
                         msg="run_from_cli({}) expected {}, got {}"
                         .format(input, expected, run_from_cli(input)))

    def test13(self):
        # Testing if errors were handled during execution.
        input = "ERRORS_LIST"
        expected = 200
        self.assertEqual(run_from_cli(input), expected,
                         msg="run_from_cli({}) expected {}, got {}"
                         .format(input, expected, run_from_cli(input)))


if __name__ == '__main__':
    unittest.main()
