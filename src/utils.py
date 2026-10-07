import json
from pathlib import Path
import cv2


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


def prepare_image_results(image_path, detections):
    image = cv2.imread(str(image_path))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    for detection in detections:
        bbox = detection["bbox"]
        cls = detection["class"]
        confidence = detection["confidence"]
        x1, y1, x2, y2 = map(int, bbox)
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        label = f"{cls}: {confidence:.2f}"
        cv2.putText(
            image,
            label,
            (x1, y1 + 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
        )
    return image
