from pathlib import Path

ROOT = Path(__file__).resolve().parent

DATA = ROOT/"data"
RAW_DATA = DATA/"raw"
PROCESSED_DATA = DATA/"processed"

PREPROCESSING = ROOT/"data-preprocessing"
ANALYSIS = ROOT/"data-analysis"
OUTPUT_DIR = ROOT/"output"

REPORTS = ROOT/"reports"
FIGURES_REPORTS = REPORTS/"figures"
