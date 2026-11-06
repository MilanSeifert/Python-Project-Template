import os

from dotenv import load_dotenv


def add(a: int, b: int) -> int:
    """Add two integers.

    Args:
        a: First number.
        b: Second number.

    Returns:
        The sum of a and b.
    """
    return a + b


def main() -> None:
    """Run the command-line entry point."""
    load_dotenv()  # loads variables from .env, if the file exists
    api_key_set = os.getenv("API_KEY") is not None
    print(f"2 + 3 = {add(2, 3)}; API key loaded: {api_key_set}")
