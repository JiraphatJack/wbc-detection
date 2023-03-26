from ultralytics import YOLO
from PIL import Image
import os


model = YOLO("wbc-model-Feb24.pt")

for filename in os.listdir("data"):
    f = os.path.join("data", filename)
    if not os.path.isfile(f) or not f.endswith(".jpg"):
        continue
    image = Image.open(f)

    if not os.path.exists("wbc"):
        os.makedirs("wbc")
    
    results = model(f)
    for i, result in enumerate(results):
        boxes = result.boxes
        xyxy = boxes.xyxy.numpy()
        for find in xyxy:
            left, top, right, bottom = int(find[0])-5, int(find[1])-5, int(find[2])+5, int(find[3])+5
            image1 = image.crop((left, top, right, bottom))
            image1.save("wbc/" + filename + "result" + str(i) + ".jpg", 'JPEG', quality=100)
