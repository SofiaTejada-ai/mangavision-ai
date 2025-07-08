from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO("yolov8n-seg.pt")  # Start with nano-size model for fast training

    model.train(
        data="configs/bubble.yaml",
        epochs=3,                  # Start small to test
        imgsz=640,
        batch=2,
        project="runs/detect",
        name="bubble_test",
        dry_run=True               # Change to False for real training
    )
