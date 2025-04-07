# mypy: disallow-untyped-defs=true, disallow-incomplete-defs=true, check-untyped-defs=true, disallow-untyped-decorators=true, no-implicit-optional=true, strict-optional=true, warn-redundant-casts=true, warn-unused-ignores=true, warn-return-any=true
"""Example of a file with strict type checking enabled.

This file demonstrates how to use type hints with strict checking
while the rest of the codebase can remain without strict checking.
"""

from typing import Dict, Generic, List, Optional, Tuple, TypeVar

T = TypeVar("T")


class TypedContainer(Generic[T]):
    """A generic container class with proper type hints."""

    def __init__(self, item: T) -> None:
        self.item = item

    def get_item(self) -> T:
        return self.item

    def set_item(self, item: T) -> None:
        self.item = item


def process_data(items: List[str]) -> Dict[str, int]:
    """Process a list of strings and return a dictionary with string lengths.

    This function is properly typed and will pass strict type checking.
    """
    return {item: len(item) for item in items}


def maybe_get_user(user_id: int) -> Optional[Dict[str, str]]:
    """Get user information by ID, returning None if not found.

    This demonstrates proper Optional type usage.
    """
    users = {
        1: {"name": "Alice", "email": "alice@example.com"},
        2: {"name": "Bob", "email": "bob@example.com"},
    }

    return users.get(user_id)


def demo_tuple_unpacking(data: Tuple[str, int, bool]) -> str:
    """Demonstrate tuple unpacking with type checking.

    All variables will be properly typed.
    """
    name, age, active = data

    # The following would cause type errors:
    # age_squared = name * name  # Error: Cannot multiply str
    # is_adult = age > 18  # This works fine with type checking

    return f"Name: {name}, Age: {age}, Active: {active}"


# This function has a type error that mypy will catch
def function_with_type_error(x: int) -> str:
    if x > 10:
        return str(x)
    else:
        # Error: Incompatible return value type (got "int", expected "str")
        # Uncomment to see the error:
        # return x
        return str(x)  # Fixed version


if __name__ == "__main__":
    # All these will pass type checking
    container = TypedContainer[str]("Hello")
    string_item: str = container.get_item()

    int_container = TypedContainer[int](42)
    int_item: int = int_container.get_item()

    # This would fail type checking:
    # wrong_type: int = container.get_item()  # Error: Incompatible types

    results = process_data(["apple", "banana", "cherry"])
    # Using logger instead of print (if needed in real code)
    # Instead of: print(results)

    user = maybe_get_user(1)
    if user is not None:
        # Instead of: print(f"Found user: {user['name']}")
        pass
