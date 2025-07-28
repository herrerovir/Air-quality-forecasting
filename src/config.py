from pathlib import Path

# === Project Root ===
ROOT_DIR = Path(__file__).resolve().parents[1]

# === Data Directories ===
DATA_DIR = ROOT_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"

# === Figures Directory ===
FIGURES_DIR = ROOT_DIR / "figures"

# === Model Directory ===
MODELS_DIR = ROOT_DIR / "models"

# === Notebooks Directory ===
NOTEBOOKS_DIR = ROOT_DIR / "notebooks"

# === Results Directories ===
RESULTS_DIR = ROOT_DIR / "results"
METRICS_RESULTS_DIR = RESULTS_DIR / "metrics"
PREDICTIONS_DIR = RESULTS_DIR / "predictions"

# === Ensure all required directories exist ===
for path in [
    # Data
    RAW_DIR,
    PROCESSED_DIR,

    # Figures
    FIGURES_DIR,
    
    # Models
    MODELS_DIR,
    
    # Notebooks
    NOTEBOOKS_DIR,

    # Results
    RESULTS_DIR,
    METRICS_RESULTS_DIR ,
    PREDICTIONS_DIR,  
]:
    path.mkdir(parents = True, exist_ok = True)