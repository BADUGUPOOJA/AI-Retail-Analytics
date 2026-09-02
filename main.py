from ultralytics import YOLO
import os
import pandas as pd

# Load AI model
model = YOLO("yolov8n.pt")

image_folder = "Images"
results_list = []

for image in os.listdir(image_folder):
    if image.lower().endswith((".jpg", ".jpeg", ".png", ".avif")):
        image_path = os.path.join(image_folder, image)

        results = model(image_path)

        labels = []

        for r in results:
            for box in r.boxes:
                cls = int(box.cls[0])
                labels.append(model.names[cls])

        results_list.append({
            "Image": image,
            "Detected Objects": ", ".join(set(labels))
        })

df = pd.DataFrame(results_list)

os.makedirs("output", exist_ok=True)

df.to_csv("output/detected_labels.csv", index=False)

print(df)
print("\nCSV saved in output/detected_labels.csv")