# Assisted by WCA for GP
# Latest GenAI contribution: granite-20B-code-instruct-v2 model
import unittest
from io import StringIO
from contextlib import redirect_stdout

def main():
    my_string = "Hello, World!"
    print(my_string)

    with open("hello.txt", "w") as file:
        file.write(my_string)

    with open("hello.txt", "r") as file:
        data = file.read()
        print(data)

class TestMain(unittest.TestCase):
    def test_main(self):
        output = StringIO()
        with redirect_stdout(output):
            main()
        self.assertEqual(output.getvalue(), "Hello, World!\nHello, World!\n")

if __name__ == "__main__":
    unittest.main()