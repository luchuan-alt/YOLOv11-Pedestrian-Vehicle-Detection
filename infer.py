from ultralytics import YOLO
import os

model = YOLO(r'D:\Download\yolov11\runs\detect\runs\detect\yolo11_vp\weights\best.pt')

# 推理测试集
results = model.predict(
    source='test/images',
    conf=0.25,
    iou=0.45,
    save=True,
    device='cpu'
)

# 输出结果
for r in results:
    img_path = os.path.basename(r.path)
    print(f"\n图片: {img_path}")
    for box in r.boxes:
        cls = int(box.cls)
        conf = float(box.conf)
        name = model.names[cls]
        print(f"  检测到: {name}, 置信度: {conf:.2f}")

print("\n✅ 推理完成！")