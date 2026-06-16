from pydantic import BaseModel
from enum import Enum

class ScanType(str, Enum):
    nmap = "nmap"
    trivy = "trivy"

class ScanCreate(BaseModel):
    target: str
    scan_type: ScanType