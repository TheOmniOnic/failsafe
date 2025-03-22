"""
This is more of an example of FailSafe than a test, but who cares. Run it, cool colors, yay.
"""

from failsafe import ImperativeTestCase, DeclarativeTestCase

class ExampleTest(ImperativeTestCase):
    def set_up(self) -> None:
        self.meaning = None

    def tear_down(self) -> None:
        delattr(self, "meaning")

    def test_set_up(self) -> None:
        self.assert_equal(self.meaning, None)

    def test_ok(self) -> None:
        life = "sucky"
        self.assert_equal(life, "sucky")

    def test_warn(self) -> None:
        life = "good"
        raise Warning("the value life should not be good")
    
    def test_error(self) -> None:
        life = "sucky"
        self.assert_equal(life, "good")

    def testbadformatting(self) -> None:
        print("hellobadformatting")

example_testcase = DeclarativeTestCase("example_testcase")

def set_up() -> None:
    example_testcase.meaning = None

def tear_down() -> None:
    delattr(example_testcase, "meaning")

def test_set_up() -> None:
    example_testcase.assert_equal(example_testcase.meaning, None)

def test_ok() -> None:
    life = "sucky"
    example_testcase.assert_equal(life, "sucky")

example_testcase.add_test(test_ok)

def test_warn() -> None:
    life = "good"
    raise Warning("the value life should not be good")

def test_error() -> None:
    life = "sucky"
    example_testcase.assert_equal(life, "good")

def testbadformatting() -> None:
    print("hellobadformatting")

example_testcase.add_tests(set_up, tear_down, test_ok, test_set_up, test_warn, testbadformatting)

if __name__ == "__main__":
    tests = ExampleTest()
    tests.run()
    example_testcase.run()
