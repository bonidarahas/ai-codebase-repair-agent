from collections.abc import Iterator
from pathlib import Path


IGNORED_DIRECTORIES = {
    ".git",
    ".venv",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    "node_modules",
    "build",
    "dist",
}


class RepositoryScanner:
    def __init__(self, root_path: str | Path) -> None:
        self.root_path = Path(root_path).expanduser().resolve()

    def scan(self) -> dict[str, str | int | bool | None]:
        self._validate_root()

        files = list(self._iter_files())

        return {
            "language": self._detect_language(files),
            "framework": self._detect_framework(),
            "files": len(files),
            "tests_found": self._tests_found(files),
        }

    def _validate_root(self) -> None:
        if not self.root_path.exists():
            raise FileNotFoundError(
                f"Repository path does not exist: {self.root_path}"
            )

        if not self.root_path.is_dir():
            raise NotADirectoryError(
                f"Repository path is not a directory: {self.root_path}"
            )

    def _iter_files(self) -> Iterator[Path]:
        for directory, dirnames, filenames in self.root_path.walk():
            dirnames[:] = [
                name
                for name in dirnames
                if name not in IGNORED_DIRECTORIES
            ]

            for filename in filenames:
                yield directory / filename

    def _detect_language(self, files: list[Path]) -> str:
        if any(file.suffix == ".py" for file in files):
            return "python"

        return "unknown"

    def _detect_framework(self) -> str | None:
        dependency_files = [
            self.root_path / "requirements.txt",
            self.root_path / "pyproject.toml",
            self.root_path / "Pipfile",
        ]

        dependency_text = ""

        for dependency_file in dependency_files:
            if dependency_file.exists():
                dependency_text += dependency_file.read_text(
                    encoding="utf-8",
                    errors="ignore",
                ).lower()

        if "fastapi" in dependency_text:
            return "fastapi"

        if "django" in dependency_text:
            return "django"

        if "flask" in dependency_text:
            return "flask"

        return None

    def _tests_found(self, files: list[Path]) -> bool:
        return any(
            file.name.startswith("test_")
            or file.name.endswith("_test.py")
            for file in files
        )