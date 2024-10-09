#!/usr/bin/env python3

"""Read a random fortune from Eno & Schmidt's Oblique Strategies."""

import pathlib
import random

def _get_strategy_file() -> pathlib.Path:
    """Return the path to the strategy file.

    Raises:
        FileNotFoundError: If the expected path is not a file.
    """
    path = pathlib.Path(__file__).resolve().parent / 'eno.txt'
    if not path.is_file():
        raise FileNotFoundError(path)
    return path

def read_strategies() -> list[str]:
    """Read the list of strategies from the strategy file."""
    strategy_file = _get_strategy_file()
    contents = strategy_file.read_text()
    lines = contents.split('\n')
    return [line.replace('\\n', '\n') for line in lines]

def main() -> None:
    """Execute the main logic of the script."""
    strategies = read_strategies()
    choice = random.choice(strategies)
    print(choice)

if __name__ == '__main__':
    main()
