
from pathlib import Path
from typing import Annotated

from langchain_core.tools import tool


# ============================================================
# TOOL 1: DIRECTORY
# ============================================================

@tool
def directory(
    path: Annotated[
        str,
        "Path of the directory to inspect. Defaults to the current project directory."
    ] = "."
) -> str:
    """
    List all files and directories inside a given directory.

    Use this tool to understand the structure of the static website
    project before creating or modifying files.
    """

    try:
        directory_path = Path(path)

        if not directory_path.exists():
            return f"Directory does not exist: {path}"

        if not directory_path.is_dir():
            return f"Not a directory: {path}"

        items = []

        for item in directory_path.iterdir():
            if item.is_dir():
                items.append(f"[DIR]  {item.name}")
            else:
                items.append(f"[FILE] {item.name}")

        if not items:
            return "Directory is empty."

        return "\n".join(sorted(items))

    except Exception as e:
        return f"Error reading directory: {str(e)}"


# ============================================================
# TOOL 2: READ
# ============================================================

@tool
def read(
    file_path: Annotated[
        str,
        "Path of the existing file whose contents need to be read."
    ]
) -> str:
    """
    Read the complete contents of an existing file.

    Use this tool before modifying an existing website file so that
    existing code and functionality can be understood and preserved.
    """

    try:
        path = Path(file_path)

        if not path.exists():
            return f"File does not exist: {file_path}"

        if not path.is_file():
            return f"Path is not a file: {file_path}"

        return path.read_text(encoding="utf-8")

    except Exception as e:
        return f"Error reading file: {str(e)}"


# ============================================================
# TOOL 3: CREATE FILE
# ============================================================

@tool
def create_file(
    file_path: Annotated[
        str,
        "Path where the new website file should be created."
    ]
) -> str:
    """
    Create a new empty file in the static website project.

    Use this tool when a required file does not already exist.
    After creating the file, use the write tool to add its content.
    """

    try:
        path = Path(file_path)

        if path.exists():
            return f"File already exists: {file_path}"

        path.parent.mkdir(parents=True, exist_ok=True)
        path.touch()

        return f"File created successfully: {file_path}"

    except Exception as e:
        return f"Error creating file: {str(e)}"


# ============================================================
# TOOL 4: WRITE
# ============================================================

@tool
def write(
    file_path: Annotated[
        str,
        "Path of the existing file that needs to be updated."
    ],
    content: Annotated[
        str,
        "Complete new content that should be written into the file."
    ]
) -> str:
    """
    Write or replace the complete contents of an existing file.

    Use this tool to update HTML, CSS, JavaScript, or other static
    website files after reading the existing file when necessary.

    The content provided should be the complete file content.
    """

    try:
        path = Path(file_path)

        if not path.exists():
            return (
                f"File does not exist: {file_path}. "
                "Use create_file first."
            )

        if not path.is_file():
            return f"Path is not a file: {file_path}"

        path.write_text(content, encoding="utf-8")

        return f"File updated successfully: {file_path}"

    except Exception as e:
        return f"Error writing file: {str(e)}"


# ============================================================
# ALL AVAILABLE TOOLS
# ============================================================

tools = [
    directory,
    read,
    create_file,
    write,
]
