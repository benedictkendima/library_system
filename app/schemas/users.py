from pydantic import BaseModel, EmailStr, Field, validator, model_validator
from app.enums import Gender
import re

class UserCreate(BaseModel):
    user_name : str = Field(min_length=3, max_length=30)
    user_phone: str = Field(min_length=11)
    user_email: EmailStr
    user_password: str = Field(min_length=6)
    user_confirmed_password: str = Field(min_length=6)
    user_gender: Gender
    user_location: str = Field(min_length=1)

    @validator('user_phone')
    def user_phone_numberic_value(cls, value):
        if value.isdigit() is not True:
            raise ValueError('Phone number most be Digits')
        return value
    
    @validator('user_password')
    def user_password_validation(cls, value):
        if not re.search(r"[A-Z]", value):
            raise ValueError('password must contain atleast one capital letter')
        if not re.search(r"[a-z]", value):
            raise ValueError('password must contain atleast one lowercase letter')
        if not re.search(r"\d", value):
            raise ValueError('password must contain atleast one numeric value')
        if not re.search(r"[^A-Za-z0-9]", value):
            raise ValueError('password must contain atleast one special character')
        return value
    
    @model_validator(mode='after')
    def validate_confirm_password(self):
        if self.user_password != self.user_confirmed_password:
            raise ValueError('password must match')
        return self
    
class UserResponse(BaseModel):
    user_id: int
    user_name: str
    user_phone: str
    user_email: str
    user_gender: str
    #user_category: str
    user_location: str