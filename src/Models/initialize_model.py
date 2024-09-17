from pydantic import BaseModel
from typing import List

class InitializeVectorStore(BaseModel):
    pdf_links : List[str] | None = None
    google_drive_link : str | None = None