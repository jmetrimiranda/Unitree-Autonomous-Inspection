from ultralytics import YOLO

# 1. Carrega o modelo YOLOv8 Small pré-treinado
model = YOLO('yolov8s.pt')

# 2. Configurações de Treinamento
results = model.train(
    data=r'/home/jorgemetri/Desktop/Helmet_Detection_Unitree/data/raw/My-First-Project-4/data.yaml',
    epochs=100,             
    patience=20,            
    imgsz=640,              
    batch=-1,               # MUDANÇA AQUI: Modo automático. A Ultralytics vai calcular o limite seguro da sua RTX 5070.
    device=0,               
    workers=4,              # MUDANÇA AQUI: Reduzido de 8 para 4. Evita sobrecarga na RAM e os erros de ConnectionReset.
    amp=True,               
    optimizer='auto',       
    project='Go2_Edu_Detect', 
    name='yolov8s_realsense', 
    
    mosaic=1.0,             
    close_mosaic=10,        
    lr0=0.01                
)

# 3. Validação imediata após o treino
metrics = model.val()
print(f"mAP50-95: {metrics.box.map}")