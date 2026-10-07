import json
from pathlib import Path


def ensure_directory_exists(raw_path):
    raw_path = Path(raw_path)
    new_path = raw_path / "Processed"
    new_path.mkdir(parents=True, exist_ok=True)
    return new_path


def save_metadata(metadata, raw_path):
    new_path = ensure_directory_exists(raw_path)
    new_path = new_path / "metadata.json"
    with open(new_path, "w") as f:
        json.dump(metadata, f)
    return new_path


def load_metadata(metadata_path):
    metadata_path = Path(metadata_path)
    if not metadata_path.exists():
        raise FileNotFoundError(f"Metadata file not found at {metadata_path}")
    with open(metadata_path, "r") as f:
        metadata = json.load(f)
    print(metadata)
    return metadata


def get_unique_classes_and_counts(metadata):
    class_counts = {}
    for item in metadata:
        for cls, count in item["class_counts"].items():
            count_set = class_counts.get(cls, set())
            count_set.add(count)
            class_counts[cls] = count_set
    for cls in class_counts:
        class_counts[cls] = sorted(class_counts[cls])
    return class_counts
