from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class ContactMessage(BaseModel):
    """
    Contact form submissions
    Collection name: "contactmessage"
    """
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    phone: Optional[str] = Field(None, max_length=30)
    message: str = Field(..., min_length=5, max_length=2000)
