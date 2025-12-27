# Developing VBL Aquarium

[GitHub Actions](https://github.com/VirtualBrainLab/vbl-aquarium/actions/workflows/build-models.yml)
are used to automatically build models to the `models` directory.
To update the models, simply push changes to the underlying pydantic models in
the `vbl_aquarium/models` directory.

## Local Development Setup

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

## Deploying New Releases

Deploying a new release is done automatically via GitHub Actions. To deploy a new release:

1. Update the version number in `src/vbl_aquarium/__about__.py`
2. Commit and push the version change to the `main` branch
3. Create and push a tag with the version number:

```bash
git tag v<version>
git push origin v<version>
```

The [release workflow](https://github.com/VirtualBrainLab/vbl-aquarium/blob/main/.github/workflows/release.yml) will automatically:

- Build the package using Hatch
- Publish the package to [PyPI](https://pypi.org/project/vbl-aquarium/)
- Create a GitHub release with auto-generated release notes

!!! note
    Pre-release versions (containing `a`, `b`, `c`, or `d` in the version string) will be marked as pre-releases on GitHub.
