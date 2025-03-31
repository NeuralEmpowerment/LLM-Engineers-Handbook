# Python Environment Setup Guide

This guide provides step-by-step instructions for setting up a complete Python development environment from scratch, including Python, pip, pipx, Poetry, and pyenv.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installing Python](#installing-python)
- [Setting Up pip](#setting-up-pip)
- [Installing pipx](#installing-pipx)
- [Installing Poetry](#installing-poetry)
- [Setting Up pyenv](#setting-up-pyenv)
- [Environment Validation](#environment-validation)
- [Troubleshooting](#troubleshooting)

## Prerequisites

- macOS, Linux, or WSL on Windows
- Terminal access
- Homebrew (for macOS users)

## Installing Python

### macOS

1. Install Python using Homebrew:
   ```bash
   brew install python
   ```

2. Verify the installation:
   ```bash
   python3 --version
   ```

### Linux

1. Install Python using your package manager:
   ```bash
   # Ubuntu/Debian
   sudo apt update
   sudo apt install python3 python3-dev python3-venv

   # Fedora
   sudo dnf install python3 python3-devel
   ```

2. Verify the installation:
   ```bash
   python3 --version
   ```

## Setting Up pip

Pip is Python's package installer and comes bundled with Python 3.4+.

1. Ensure pip is installed:
   ```bash
   python3 -m pip --version
   ```

2. Upgrade pip to the latest version:
   ```bash
   python3 -m pip install --upgrade pip
   ```

3. Configure pip to use a local user directory for installations:
   ```bash
   python3 -m pip config set global.user true
   ```

## Installing pipx

pipx allows you to install and run Python applications in isolated environments.

### Using pip (recommended)

```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

### Using Homebrew (macOS)

```bash
brew install pipx
pipx ensurepath
```

### Verify Installation

Close and reopen your terminal, then run:

```bash
pipx --version
```

## Installing Poetry

Poetry is a tool for dependency management and packaging in Python.

### Using pipx (recommended)

```bash
pipx install poetry
```

### Using the official installer

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Verify Installation

```bash
poetry --version
```

### Configure Poetry

```bash
# Configure Poetry to create virtual environments inside the project directory
poetry config virtualenvs.in-project true
```

## Setting Up pyenv

pyenv lets you easily switch between multiple versions of Python.

### Install Dependencies (macOS)

```bash
brew install openssl readline sqlite3 xz zlib tcl-tk
```

### Install pyenv

#### Using Homebrew (macOS)

```bash
brew install pyenv
pyenv init
```

#### Using the Installer Script (Linux/macOS)

```bash
curl https://pyenv.run | bash
```

### Important: Restart Your Terminal

Close and reopen your terminal for the changes to take effect.

### Verify pyenv Installation

```bash
pyenv --version
```

### Install Python Versions with pyenv

```bash
# List available Python versions
pyenv install --list

# Install specific Python version (e.g., 3.11.8)
pyenv install 3.11.8

# Set global Python version
pyenv global 3.11.8

# Set project-specific version
cd your-project-directory
pyenv local 3.11.8
```

## Environment Validation

Run these commands to verify your complete setup:

```bash
# Check Python
python --version                 # Should match the version you set with pyenv

# Check pip
pip --version                    # Should reference the pyenv Python version

# Check pipx
pipx --version                   # Should be installed

# Check Poetry
poetry --version                 # Should be installed

# Check pyenv
pyenv --version                  # Should be installed
pyenv which python               # Should point to the pyenv-managed Python
```

## Troubleshooting

### pyenv Python Version Not Being Used

If `python --version` shows the wrong version:

1. Check your PATH ordering:
   ```bash
   echo $PATH | tr ':' '\n' | grep -i python
   ```
   The pyenv shims directory should be early in the PATH.

2. Verify pyenv initialization in your shell config:
   ```bash
   export PYENV_ROOT="$HOME/.pyenv"
   [[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
   eval "$(pyenv init - zsh)"  # or eval "$(pyenv init -)" for bash
   ```

3. Confirm the `.python-version` file contents (for project-specific settings):
   ```bash
   cat .python-version
   ```

### Conda Conflicts with pyenv

If you have Conda installed and it's conflicting with pyenv:

1. Deactivate Conda:
   ```bash
   conda deactivate
   ```

2. Configure Conda not to auto-activate:
   ```bash
   conda config --set auto_activate_base false
   ```

### Poetry Not Finding the Right Python Version

If Poetry is using the wrong Python version:

1. Explicitly tell Poetry which Python to use:
   ```bash
   poetry env use $(pyenv which python)
   ```

2. Verify the Poetry environment:
   ```bash
   poetry env info
   ```

### PATH Reset Script

If all else fails, create this reset script:

```bash
cat > ~/reset_python_env.sh << 'EOF'
#!/bin/bash
# Reset PATH to remove potential conflicts
export PATH="/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"

# Add pyenv to PATH
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
export PATH="$PYENV_ROOT/shims:$PATH"
eval "$(pyenv init -)"

# Add other tools back to PATH
export PATH="$HOME/.local/bin:$PATH"
EOF

chmod +x ~/reset_python_env.sh
```

Run it when needed:
```bash
source ~/reset_python_env.sh
``` 