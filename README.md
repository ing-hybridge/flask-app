# Estructura base Flask

## Estructura
```
tu_app/
├── app/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   └── views.py
├── config.py
├── run.py
├── requirements.txt
└── venv/ (opcional, creada localmente)
```

## Ejecutar
1) (Opcional) Crear venv:
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```
2) Instalar deps:
   ```bash
   pip install -r requirements.txt
   ```
3) Correr:
   ```bash
   python run.py
   ```
Abrir http://localhost:5050/