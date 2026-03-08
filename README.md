## 📁 Estrutura do Projeto

```text
project_name/
├── data/
│   ├── raw/            # Dados originais imutáveis (imagens, vídeos)
│   ├── processed/      # Dados transformados (aumentados, redimensionados)
│   └── annotations/    # Rótulos/ground truth (JSON, XML, YOLO txt)
├── src/
│   ├── data_loader.py  # Carregamento e pré-processamento de dados
│   ├── train.py        # Pipeline de treinamento
│   ├── model.py        # Arquitetura do modelo
│   └── utils.py        # Funções auxiliares
├── notebooks/          # Jupyter notebooks para experimentação
├── config/             # Arquivos de configuração (YAML, JSON, params)
├── models/             # Modelos treinados salvos (pth, h5, pesos)
├── results/            # Visualizações, logs, gráficos de avaliação
├── tests/              # Testes unitários
├── README.md           # Documentação do projeto
├── requirements.txt    # Dependências do projeto
└── .gitignore          # Arquivos e pastas ignorados pelo Git
