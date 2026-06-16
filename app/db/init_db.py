from app.db.database import engine
from app.db.base import Base

from app.db.models.user import User
from app.db.models.scan_job import ScanJob

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
    print("Tables created successfully.")