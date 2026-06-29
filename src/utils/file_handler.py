import json
from pathlib import Path


def save_json(data, folder_path, file_name):
    """
    Save Python object as JSON file.

    Args:
        data: Dictionary or List
        folder_path: Folder location
        file_name: JSON file name
    """

    folder = Path(folder_path)

    folder.mkdir(parents=True, exist_ok=True)

    file_path = folder / file_name

    with open(file_path, "w", encoding="utf-8") as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )

    print(f"✅ Saved : {file_path}")