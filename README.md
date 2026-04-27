# YOLOv11 行人与车辆目标检测实验
> 基于YOLOv11的轻量级行人/车辆检测课程实验 | 深圳大学 人工智能实验项目

---

## 目录
- [项目简介](#项目简介)
- [快速开始](#快速开始)
- [文件结构](#文件结构)
- [环境配置](#环境配置)
- [数据集说明](#数据集说明)
- [训练流程](#训练流程)
- [推理与测试](#推理与测试)
- [实验结果与分析](#实验结果与分析)
- [作者信息](#作者信息)

---

## 项目简介
本项目基于 **YOLOv11n** 轻量级目标检测模型，实现了行人（Pedestrian）与车辆（Vehicle）的实时检测任务，适用于低配CPU环境的课程实验。
- 目标类别：`0: Pedestrian`、`1: Vehicle`
- 数据集：Roboflow公开标注数据集（1596张图像）
- 核心优势：模型轻量化、训练流程完整、可直接复现实验结果

---

## 快速开始
### 1. 克隆仓库
```bash
2. 安装依赖
bash
运行
pip install ultralytics
3. 一键训练
bash
运行
python train.py
4. 快速推理
bash
运行
python infer.py
文件结构
plaintext
/YOLOv11-Pedestrian-Vehicle-Detection
├── README.md               # 项目说明文档（本文件）
├── data.yaml               # 数据集路径与类别配置文件
├── train.py                # 模型训练主脚本
├── infer.py                # 模型推理与测试脚本
├── README.dataset.txt      # 数据集原始说明
├── README.roboflow.txt     # Roboflow导出信息
└── runs/                   # 训练日志、模型权重与结果输出目录
    └── detect/
        └── yolo11_vp/
            └── weights/
                └── best.pt # 训练得到的最优权重文件
环境配置
推荐环境
Python 版本：3.10
核心依赖：ultralytics>=8.0
运行环境：Windows/Linux（CPU/GPU 均可）
完整配置命令
bash
运行
# 创建虚拟环境（可选）
conda create -n yolov11 python=3.10 -y
conda activate yolov11

# 安装ultralytics库
pip install ultralytics
数据集说明
数据集来源
来源：Roboflow Universe 公开数据集
项目名：Pedestrian & vehicle detection v7
图像总数：1596 张
标注格式：YOLO 格式（.txt标注文件）
预处理与增强
图像尺寸：640×640 统一缩放
数据增强：随机亮度、旋转、模糊、水平翻转
数据集划分：默认按训练 / 验证 / 测试集划分
训练流程
训练参数配置（train.py）
表格
参数	取值	说明
epochs	15	训练轮次
imgsz	640	输入图像尺寸
batch	4	批次大小
device	cpu	训练设备（CPU）
workers	2	数据加载线程数
训练执行
bash
运行
python train.py
训练过程中，日志与模型权重会自动保存到 runs/detect/yolo11_vp/ 目录下。
推理与测试
推理参数配置（infer.py）
表格
参数	取值	说明
conf	0.25	置信度阈值
iou	0.45	NMS 交并比阈值
推理执行
bash
运行
python infer.py
推理结果（带检测框的图像 / 视频）会保存到 runs/detect/ 目录下。
实验结果与分析
关键指标
表格
指标	数值	说明
mAP@0.5	0.83	类别平均精度
mAP@0.5:0.95	0.55	多尺度精度
训练时间	~30 分钟	CPU 环境下 15 轮训练耗时
结果分析
模型在行人与车辆目标上均能稳定识别，无明显漏检 / 误检问题。
轻量级 YOLOv11n 模型在 CPU 环境下也能实现实时推理，满足课程实验需求。
数据增强有效提升了模型的泛化能力，对不同光照、角度的目标鲁棒性较好。
作者信息
报告人：林钰韵
学号：2023280266
班级：电信 01 班
指导教师：戴林蕙
项目地址：https://github.com/luchuan-alt/YOLOv11-Pedestrian-Vehicle-Detection
