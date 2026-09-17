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
        "Path of the directory to inspect. Defaults to the backend directory."
    ] = "."
) -> str:
    """
    List all files and directories inside a given directory.
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
# TOOL 2: CREATE PROJECT FOLDER
# ============================================================

@tool
def create_project(
    project_name: Annotated[
        str,
        "Name of the website project folder."
    ]
) -> str:
    """
    Create a new project folder directly inside the backend directory.

    Example:
        create_project("my-portfolio")

    Creates:
        backend/my-portfolio/
    """

    try:
        project_name = project_name.strip()

        if not project_name:
            return "Project name cannot be empty."

        # Backend is the current working directory
        backend_path = Path(".")

        # Prevent the LLM from creating nested paths
        safe_project_name = Path(project_name).name

        project_path = backend_path / safe_project_name

        if project_path.exists():

            if project_path.is_dir():
                return (
                    f"Project folder already exists: "
                    f"backend/{safe_project_name}"
                )

            return (
                f"A file already exists with this name: "
                f"backend/{safe_project_name}"
            )

        project_path.mkdir(parents=True)

        return (
            f"Project folder created successfully: "
            f"backend/{safe_project_name}"
        )

    except Exception as e:
        return f"Error creating project folder: {str(e)}"


# ============================================================
# TOOL 3: READ
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
# TOOL 4: CREATE FILE
# ============================================================

@tool
def create_file(
    file_path: Annotated[
        str,
        "Path of the new website file. The file must be inside "
        "the project folder."
    ]
) -> str:
    """
    Create a new empty website file inside the project folder.
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
# TOOL 5: WRITE
# ============================================================

@tool
def write(
    file_path: Annotated[
        str,
        "Path of the existing website file that needs to be updated."
    ],
    content: Annotated[
        str,
        "Complete new content that should be written into the file."
    ]
) -> str:
    """
    Write or replace the complete contents of an existing file.
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
    create_project,
    read,
    create_file,
    write,
]