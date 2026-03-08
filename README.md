project_name/
├── data/
│   ├── raw/            # Immutable original data (images, videos)
│   ├── processed/      # Transformed data (augmented, resized)
│   └── annotations/    # Labels/ground truth (JSON, XML, YOLO txt)
├── src/
│   ├── data_loader.py  # Data loading and preprocessing
│   ├── train.py        # Training pipeline
│   ├── model.py        # Model architecture
│   └── utils.py        # Helper functions
├── notebooks/          # Jupyter notebooks for experimentation
├── config/             # Config files (YAML, JSON, params)
├── models/             # Saved trained models (pth, h5, weight files)
├── results/            # Visualizations, logs, evaluation plots
├── tests/              # Unit tests
├── README.md
├── requirements.txt
└── .gitignore
