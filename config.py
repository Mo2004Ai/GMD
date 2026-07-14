from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent
DATASET_DIR = BASE_DIR / "Dataset"
MODELS_DIR = BASE_DIR / "models"

EYE_MODEL_PATH = MODELS_DIR / "eye_model_best.pth"
YAWN_MODEL_PATH = MODELS_DIR / "yawn_model_best_unfreeze.pth"

EYE_CLASSES = ["open", "close"]
YAWN_CLASSES = ["Yawn", "no_yawn"]

INPUT_SIZE = 224
CONFIDENCE_THRESHOLD = 0.50

EYE_CLOSED_FRAMES_FOR_DROWSY = 18
YAWN_COOLDOWN_FRAMES = 30
ALERT_SOUND_COOLDOWN_SECONDS = 1.5