from ultralytics import YOLO
from pathlib import Path
from src.config import load_config


class InferenceYolo:
    def __init__(self, model_path, device="cpu"):
        self.model = YOLO(model_path)
        self.device = device
        self.model.to(self.device)
        config = load_config()
        self.config_threshold = config["model"]["config_threshold"]
        self.image_extensions = config["data"]["image_extensions"]
        print(f"Model loaded from {model_path} with threshold {self.config_threshold}")

    def process_image(self, image_path):
        results = self.model.predict(
            source=image_path, conf=self.config_threshold, device=self.device
        )
        detections = []
        class_counts = {}
        for result in results:
            for box in result.boxes:
                cls = result.names[int(box.cls)]
                confidence = float(box.conf)
                bbox = box.xyxy[0].tolist()
                detections.append(
                    {"class": cls, "confidence": confidence, "bbox": bbox}
                )
                class_counts[cls] = class_counts.get(cls, 0) + 1
        for detection in detections:
            detection["count"] = class_counts[detection["class"]]
        return {
            "image_path": str(image_path),
            "detections": detections,
            "total_objects": len(detections),
            "unique_classes": list(class_counts.keys()),
            "class_counts": class_counts,
        }

    def process_directory(self, directory_path):
        metadata = []
        patterns = [f"*{ext}" for ext in self.image_extensions]
        images_path = []
        for ext in patterns:
            images_path.extend(Path(directory_path).glob(ext))
        for img_path in images_path:
            try:
                metadata.append(self.process_image(img_path))
            except Exception as e:
                print(f"Error processing {img_path}: {str(e)}")
                continue
        return metadata
