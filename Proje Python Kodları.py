# 1. YOLOv5 reposunu klonla ve bağımlılıkları yükle
!git clone https://github.com/ultralytics/yolov5
%cd yolov5
%pip install -r requirements.txt

# 2. Dataset.zip yükle ve çıkar
import zipfile
with zipfile.ZipFile("/content/dataset.zip", 'r') as zip_ref:
    zip_ref.extractall("/content/data_yolo")

# 3. XML → TXT dönüştürme fonksiyonu (YOLO formatına)
import os
import xml.etree.ElementTree as ET

classes = ["Car", "Motorcycle", "Bus", "Truck", "Taxi"]

def convert_annotation(xml_file, txt_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    with open(txt_file, 'w') as out_file:
        for obj in root.iter('object'):
            cls = obj.find('name').text
            if cls not in classes:
                continue
            cls_id = classes.index(cls)
            xmlbox = obj.find('bndbox')
            b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text),
                 float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
            x_center = (b[0] + b[1]) / 2.0 / w
            y_center = (b[2] + b[3]) / 2.0 / h
            box_width = (b[1] - b[0]) / w
            box_height = (b[3] - b[2]) / h
            out_file.write(f"{cls_id} {x_center} {y_center} {box_width} {box_height}\n")

# 4. Dönüştürme işlemini tüm veri seti için uygula
splits = ['train', 'val', 'test']
for split in splits:
    label_dir = f"data_yolo/labels/{split}"
    image_dir = f"data_yolo/images/{split}"
    os.makedirs(label_dir, exist_ok=True)
    for file in os.listdir(image_dir):
        if file.endswith(".jpg"):
            xml_path = os.path.join(image_dir, file.replace(".jpg", ".xml"))
            txt_path = os.path.join(label_dir, file.replace(".jpg", ".txt"))
            if os.path.exists(xml_path):
                convert_annotation(xml_path, txt_path)

# 5. data.yaml dosyasını oluştur
yaml_content = """
train: ../data_yolo/images/train
val: ../data_yolo/images/val
test: ../data_yolo/images/test

nc: 5
names: ['Car', 'Motorcycle', 'Bus', 'Truck', 'Taxi']
"""
with open("/content/yolov5/data.yaml", "w") as f:
    f.write(yaml_content)

# 6. YOLOv5 modelini eğit
!python train.py --img 416 --batch 16 --epochs 20 --data data.yaml --weights yolov5s.pt --name arac_siniflandirma_gpu

# 7. Test görselleri üzerinde tahmin yap
!python detect.py --weights runs/train/arac_siniflandirma_gpu/weights/best.pt \
--img 416 --conf 0.4 --source ../data_yolo/images/test --name test_sonuclari

# 8. Tahmin görsellerini görüntüle (hepsi)
import glob
from IPython.display import Image, display

image_paths = glob.glob('runs/detect/test_sonuclari/*.jpg')
for img_path in image_paths:
    display(Image(filename=img_path))

# 9. Eğitim sonrası grafiksel sonuçları görüntüle
display(Image(filename='runs/train/arac_siniflandirma_gpu/results.png'))
display(Image(filename='runs/train/arac_siniflandirma_gpu/confusion_matrix.png'))
display(Image(filename='runs/train/arac_siniflandirma_gpu/f1_curve.png'))
display(Image(filename='runs/train/arac_siniflandirma_gpu/R_curve.png'))
display(Image(filename='runs/train/arac_siniflandirma_gpu/labels.jpg'))
