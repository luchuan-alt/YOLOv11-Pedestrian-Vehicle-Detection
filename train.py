from ultralytics import YOLO

# 加载YOLOv11n模型
model = YOLO('yolo11n.pt')

# 开始训练
results = model.train(
    data='D:/download/yolov11/data.yaml',
    epochs=15,
    imgsz=640,
    batch=4,
    device='cpu',
    workers=2,
    project='runs/detect',
    name='yolo11_vp',
    val=True
)

print("训练完成！权重保存于：", results.save_dir)