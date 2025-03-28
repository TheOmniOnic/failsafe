# FailSafe: The Testing Framework Of Your Dreams

Tired of the bloated testing frameworks like `unittest` which require you to make large classes to test your code? Well, not anymore! FailSafe is a lightweight, simpler, more pythonic testing framework. 

## Features
- **Imperative and Declarative Testing**: Supports both imperative and declarative styles of testing for flexibility.
- **Extensive Assertions**: Includes a wide variety of assertions for equality, truthfulness, containment, and more.
- **Test Result Formatting**: Outputs results with ANSI color coding for easy readability.
- **Test Setup and Teardown**: Optionally add setup/teardown logic for initializing and cleaning up test environments.
- **Mocking**: Built-in support for mocking external dependencies during tests.

## Installation
In your shell of choice, run the following command:
```bash
pip install failsafe
```

## Usage
After installation, FailSafe becomes a usable package. To import it, add `import failsafe` or `from failsafe import <object>` to your python file.

### Imperative Testing
```python
class ExampleTest(failsafe.ImperativeTestCase):
    def test_add(self) -> None:
        self.assert_equal(1 + 2, 3)

if __name__ == "__main__":
    tests = ExampleTest()
    tests.run()
```

### Declarative Testing
```python
example_tester = failsafe.DeclarativeTestCase("example_testcase")

def test_add() -> None:
    example_tester.assert_equal(1 + 2, 3)

example_tester.add_test(test_add)

if __name__ == "__main__":
    example_tester.run()
```

Both of the above examples result in beautiful, color-coded output when run.

### Adding `set_up`/`tear_down` Functions
The `set_up` function is called when a test is run, and the `tear_down` function is called when a test ends. For example, in the following code, `set_up` runs before `test_add`, so `self.add` is preserved, and `tear_down` cleans up `self.add`:
```python
class ExampleTest(failsafe.ImperativeTestCase):
    def set_up(self) -> None:
        self.add = 1 + 2

    def tear_down(self) -> None:
        delattr(self, "add")

    def test_add(self) -> None:
        self.assert_equal(self.add, 3)
```

or

```python
example_testcase = failsafe.DeclarativeTestCase("example_testcase")

def set_up() -> None:
    example_testcase.add = 1 + 2

def tear_down() -> None:
    delattr(example_testcase, "add")

def test_add() -> None:
    example_testcase.assert_equal(example_testcase.add, 3)
```

### Mocking Values During Testing
You can mock values by applying the `patch` decorator on a test, like this:
```python
class ExampleTest(failsafe.ImperativeTestCase):
    @failsafe.patch("sys.stdout", io.StringIO())
    def test_print(self, mock_stdout: io.StringIO) -> None:
        print("Hello, World!")
        self.assert_equal(mock_stdout.getall(), "Hello, World!\n")
```

or

```python
example_testcase = failsafe.DeclarativeTestCase("example_testcase")

@failsafe.patch("sys.stdout", io.StringIO())
def test_print(mock_stdout: io.StringIO) -> None:
    print("Hello, World!")
    example_testcase.assert_equal(mock_stdout.getall(), "Hello, World!\n")
```

## Contribution
FailSafe is an open-source project available [here](https://github.com/TheOmniOnic/failsafe) on GitHub. Feel free to fork or branch the project and submit pull requests or issues!

## License
This project is licensed under the MIT license. See the [LICENSE](https://github.com/TheOmniOnic/failsafe/blob/main/LICENSE) file for more.