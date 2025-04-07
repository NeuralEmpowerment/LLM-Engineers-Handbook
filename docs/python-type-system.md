# Python Type System Guide (for TypeScript Developers)

## Overview

Coming from TypeScript, Python's type system might feel different but shares many similar concepts. This guide will help you understand how Python's type system works, especially in the context of this project which uses:

- [Python Type System Guide (for TypeScript Developers)](#python-type-system-guide-for-typescript-developers)
  - [Overview](#overview)
  - [Key Differences from TypeScript](#key-differences-from-typescript)
  - [Type Checking in This Project](#type-checking-in-this-project)
    - [1. Static Type Checking (like TSC)](#1-static-type-checking-like-tsc)
    - [2. Runtime Type Validation with Pydantic](#2-runtime-type-validation-with-pydantic)
    - [3. Abstract Base Classes (like TypeScript abstract classes)](#3-abstract-base-classes-like-typescript-abstract-classes)
    - [4. Generic Types](#4-generic-types)
  - [Common Types Cheat Sheet](#common-types-cheat-sheet)
  - [Best Practices](#best-practices)
  - [Project-Specific Examples](#project-specific-examples)
    - [Vector Base Document (from our codebase)](#vector-base-document-from-our-codebase)
  - [Running Type Checks](#running-type-checks)
  - [Common Issues and Solutions](#common-issues-and-solutions)

## Key Differences from TypeScript

1. **Optional Type Checking**
   ```python
   # Python - types are optional hints
   def greet(name: str) -> str:
       return f"Hello {name}"
   
   # TypeScript - types are enforced by default
   function greet(name: string): string {
       return `Hello ${name}`;
   }
   ```

2. **Runtime vs Compile-time**
   - TypeScript: Types are stripped at compile time
   - Python: Type hints are available at runtime through `__annotations__`

3. **Type Checking Tools**
   - TypeScript: Built-in `tsc` compiler
   - Python: External tools like `mypy`, `pyright`, or `pylance` in VS Code

## Type Checking in This Project

### 1. Static Type Checking (like TSC)

Install mypy:
```bash
poetry add --group dev mypy
```

Run type checks:
```bash
poetry run mypy .
```

VS Code setup:
1. Install Python extension
2. Enable "Python > Analysis: Type Checking Mode" to "basic" or "strict"

### 2. Runtime Type Validation with Pydantic

```python
# Similar to TypeScript interfaces/types with Zod
from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    id: int
    name: str
    email: Optional[str] = None  # Similar to string | undefined in TS
    age: int = Field(gt=0)  # With validation (like Zod)

# Runtime validation
user = User(id=1, name="John", age=25)  # ✅ OK
user = User(id="1", name="John", age=25)  # ✅ OK (auto-coercion)
user = User(id=1, name="John", age=-1)  # ❌ ValidationError
```

### 3. Abstract Base Classes (like TypeScript abstract classes)

```python
from abc import ABC, abstractmethod
from typing import Protocol

# Similar to TypeScript abstract class
class Animal(ABC):
    @abstractmethod
    def make_sound(self) -> str:
        pass

# Similar to TypeScript interface
class Walkable(Protocol):
    def walk(self) -> None: ...

# Implementation
class Dog(Animal):
    def make_sound(self) -> str:  # Must implement
        return "Woof!"
```

### 4. Generic Types

```python
from typing import Generic, TypeVar, List

T = TypeVar('T')  # Similar to <T> in TypeScript

# Generic class (like TypeScript generics)
class Container(Generic[T]):
    def __init__(self, item: T):
        self.item = item

# Usage
string_container: Container[str] = Container("hello")
int_container: Container[int] = Container(42)
```

## Common Types Cheat Sheet

| TypeScript | Python |
|------------|--------|
| `string` | `str` |
| `number` | `int`, `float` |
| `boolean` | `bool` |
| `any` | `Any` |
| `unknown` | `Any`* |
| `void` | `None` |
| `T[]` | `List[T]` |
| `Array<T>` | `List[T]` |
| `{ [key: string]: T }` | `Dict[str, T]` |
| `type\|null` | `Optional[type]` |
| `type\|undefined` | `Optional[type]` |

\* Python doesn't have a direct equivalent to `unknown`

## Best Practices

1. **Enable Type Checking in Your Editor**
   - VS Code: Use Pylance with strict type checking
   - PyCharm: Built-in type checking enabled by default

2. **Use Type Hints Consistently**
   ```python
   def process_items(items: List[str]) -> Dict[str, int]:
       return {item: len(item) for item in items}
   ```

3. **Leverage Pydantic for Data Validation**
   - Use for API requests/responses
   - Use for configuration objects
   - Use for database models

4. **Use Abstract Base Classes for Interfaces**
   - Define contracts for implementations
   - Ensure consistent API across related classes

5. **Type Checking During Development**
   - Run mypy regularly: `poetry run mypy .`
   - Fix type errors as you go
   - Use VS Code's real-time type checking

## Project-Specific Examples

### Vector Base Document (from our codebase)

```python
T = TypeVar("T", bound="VectorBaseDocument")

class VectorBaseDocument(BaseModel, Generic[T], ABC):
    id: UUID4 = Field(default_factory=uuid.uuid4)
    
    @classmethod
    def from_record(cls: Type[T], point: Record) -> T:
        # Implementation...
```

This is similar to TypeScript:

```typescript
interface VectorBaseDocument<T extends VectorBaseDocument<T>> {
    id: string;  // UUID
    fromRecord(point: Record): T;
}
```

## Running Type Checks

1. **During Development (VS Code)**
   - Real-time type checking with Pylance
   - Problems show up as squiggly lines (like TypeScript)

2. **Command Line**
   ```bash
   # Check entire project
   poetry run mypy .
   
   # Check specific file
   poetry run mypy llm_engineering/domain/base/vector.py
   
   # Check with more strict settings
   poetry run mypy --strict .
   ```

3. **Pre-commit Hook**
   ```yaml
   # .pre-commit-config.yaml
   - repo: https://github.com/pre-commit/mirrors-mypy
     rev: v1.9.0
     hooks:
     - id: mypy
       additional_dependencies: [types-all]
   ```

## Common Issues and Solutions

1. **Missing Type Hints**
   ```python
   # ❌ Bad
   def process(x):
       return x + 1
   
   # ✅ Good
   def process(x: int) -> int:
       return x + 1
   ```

2. **Optional Types**
   ```python
   # ❌ Bad
   def get_user(id: int):
       if not found:
           return None
       return User()
   
   # ✅ Good
   def get_user(id: int) -> Optional[User]:
       if not found:
           return None
       return User()
   ```

3. **Generic Types**
   ```python
   # ❌ Bad
   def first(lst):
       return lst[0]
   
   # ✅ Good
   T = TypeVar('T')
   def first(lst: List[T]) -> T:
       return lst[0]
   ```