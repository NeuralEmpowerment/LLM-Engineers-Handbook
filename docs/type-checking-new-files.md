# Type Checking Only New Files

This guide explains how to use type checking selectively for new files in this project, without having to fix all existing type errors in the codebase.

## Setup

1. We've created a `mypy.ini` file with forgiving defaults
2. We've added type checking tasks to the `poe.tasks.toml` file

## How to Type Check New Files

When you create a new Python file, add these special comments at the very top to enable strict checking:

```python
# mypy: disallow-untyped-defs=true, disallow-incomplete-defs=true, check-untyped-defs=true, disallow-untyped-decorators=true, no-implicit-optional=true, strict-optional=true, warn-redundant-casts=true, warn-unused-ignores=true, warn-return-any=true
```

For example:

```python
# mypy: disallow-untyped-defs=true, disallow-incomplete-defs=true, check-untyped-defs=true
from typing import List, Dict, Optional
from pydantic import BaseModel

def process_data(items: List[str]) -> Dict[str, int]:
    return {item: len(item) for item in items}

class User(BaseModel):
    name: str
    age: int
    email: Optional[str] = None
```

## Running Type Checks

To check your files:

```bash
poetry run poe type-check
```

This will:
1. Skip most errors in existing files
2. Apply strict checking to files with the special mypy comments
3. Give you helpful squiggly lines in VS Code (if you have the Python extension)

## More Selective Options

You can also use individual flags for specific checks:

```python
# mypy: disallow-untyped-defs=true
```

Or check a specific file from command line:

```bash
poetry run mypy path/to/your/new_file.py --strict
```

## Common Flag Combinations

Depending on how strict you want to be, you can use different combinations:

### Basic Type Checking
```python
# mypy: disallow-untyped-defs=true
```

### Medium Strictness
```python
# mypy: disallow-untyped-defs=true, disallow-incomplete-defs=true, check-untyped-defs=true
```

### High Strictness (Almost like --strict)
```python
# mypy: disallow-untyped-defs=true, disallow-incomplete-defs=true, check-untyped-defs=true, disallow-untyped-decorators=true, no-implicit-optional=true, strict-optional=true, warn-redundant-casts=true, warn-unused-ignores=true, warn-return-any=true
```

## VS Code Integration

To get real-time type checking in VS Code:

1. Install the Python extension
2. Add this to your `.vscode/settings.json`:

```json
{
    "python.linting.mypyEnabled": true,
    "python.linting.enabled": true
}
```

## Common Type Annotations

Here are common type annotations you'll use:

```python
# Basic types
x: int = 1
name: str = "John"
is_valid: bool = True

# Collections
items: List[str] = ["a", "b", "c"]
counts: Dict[str, int] = {"a": 1, "b": 2}
values: Set[int] = {1, 2, 3}
pair: Tuple[str, int] = ("a", 1)

# Optional/None
maybe_string: Optional[str] = None

# Functions
def greet(name: str) -> str:
    return f"Hello {name}"

# Callable
callback: Callable[[int], str] = lambda x: str(x)
``` 