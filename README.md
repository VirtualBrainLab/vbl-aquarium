# VBL Aquarium

![PyPI - Version](https://img.shields.io/pypi/v/vbl-aquarium)
[![Build Models](https://github.com/VirtualBrainLab/vbl-aquarium/actions/workflows/build-models.yml/badge.svg)](https://github.com/VirtualBrainLab/vbl-aquarium/actions/workflows/build-models.yml)
[![Static Analysis](https://github.com/VirtualBrainLab/vbl-aquarium/actions/workflows/static-analysis.yml/badge.svg)](https://github.com/VirtualBrainLab/vbl-aquarium/actions/workflows/static-analysis.yml)
[![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Checked with pyright](https://microsoft.github.io/pyright/img/pyright_badge.svg)](https://microsoft.github.io/pyright/)

Collection of Pydantic models describing data objects passed between Virtual Brain Lab projects.

Corresponding JSON schema and C# files are generated automatically and are located in the `/models` directory.

## Usage

GitHub Actions are used to automatically update the built models to the `models` directory. To update the models, simply push changes to the `main` branch.

## Install for Development

1. Install [Hatch](https://hatch.pypa.io/latest/)
2. Clone the repository
3. Run `hatch shell` in the repository root directory

Use 
```bash
python src/vbl_aquarium/build.py
```
to build the models locally.

Use
```bash
hatch run check
```
to run pyright type checking.
