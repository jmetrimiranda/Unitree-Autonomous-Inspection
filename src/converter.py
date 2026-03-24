from ultralytics import YOLO

# 1. Carrega o modelo PyTorch que você enviou para a placa
model = YOLO(r'/home/jorgemetri/Desktop/Helmet_Detection_Unitree/src/runs/detect/Go2_Edu_Detect/yolov8s_realsense_v5/weights/best.pt')

# 2. Exporta para TensorRT com precisão FP16 (Ideal para Nvidia Orin)
print("Iniciando conversão para TensorRT... Isso pode levar alguns minutos.")
model.export(format='engine', device=0, half=True, workspace=4)
print("Conversão concluída! Arquivo best.engine gerado.")