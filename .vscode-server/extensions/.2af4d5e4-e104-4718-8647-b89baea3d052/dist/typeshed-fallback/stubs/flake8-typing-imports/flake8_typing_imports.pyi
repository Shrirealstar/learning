import argparse
import ast
from typing import Any, ClassVar, Generator, Type

class Plugin:
    name: ClassVar[str]
    version: ClassVar[str]
    @staticmethod
    def add_options(option_manager: Any) -> None: ...
    @classmethod
    def parse_options(cls, options: argparse.Namespace) -> None: ...
    def __init__(self, tree: ast.AST) -> None: ...
    def run(self) -> Generator[tuple[int, int, str, Type[Any]], None, None]: ...

def __getattr__(name: str) -> Any: ...  # incomplete (other attributes are normally not accessed)
