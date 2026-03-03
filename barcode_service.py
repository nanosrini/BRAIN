"""
services/barcode_service.py — Barcode Generation
==================================================
Generates unique barcodes for each sample.
Format: BS-XXXXX-YYYY
  BS   = BioSentinel prefix
  XXXXX = 5 random uppercase alphanumeric chars
  YYYY  = last 4 digits of current timestamp (ms)
"""

import random
import string
from datetime import datetime
from sqlalchemy.orm import Session
from models.models import Sample


def generate_barcode() -> str:
    """Generate a unique barcode string. Does NOT check DB uniqueness here."""
    chars = string.ascii_uppercase + string.digits
    random_part = "".join(random.choices(chars, k=5))
    time_part = str(int(datetime.now().timestamp() * 1000))[-4:]
    return f"BS-{random_part}-{time_part}"


def generate_unique_barcode(db: Session) -> str:
    """
    Generate a barcode and verify it doesn't already exist in the database.
    Retries up to 10 times (collision is extremely unlikely).
    """
    for _ in range(10):
        barcode = generate_barcode()
        existing = db.query(Sample).filter(Sample.barcode == barcode).first()
        if not existing:
            return barcode
    raise RuntimeError("Could not generate a unique barcode after 10 attempts.")


def parse_barcode(barcode: str) -> dict:
    """
    Parse a barcode string back into its components.
    Returns a dict with prefix, random_part, time_part.
    """
    parts = barcode.split("-")
    if len(parts) != 3 or parts[0] != "BS":
        return {"valid": False, "barcode": barcode}
    return {
        "valid":       True,
        "barcode":     barcode,
        "prefix":      parts[0],
        "random_part": parts[1],
        "time_part":   parts[2],
    }
