import os


def save_to_file(
    directory: str,
    filename: str,
    content: list,
    encoding="utf-8",
    newline="\n",
) -> None:
    """
    Saves a list of strings to a file.
    """
    if not content:
        return

    os.makedirs(directory, exist_ok=True)
    file_path = os.path.join(directory, filename)

    with open(file_path, "w", encoding=encoding) as f:
        f.write(newline.join(content) + newline)
