from fastapi import APIRouter
from app.schemas.scan import ScanCreate

router = APIRouter()

@router.post("/scans")
def create_scan(scan: ScanCreate):
    return{
        "message" : "Scan request received safely",
        "target" : scan.target,
        "scan_type" : scan.scan_type
    }