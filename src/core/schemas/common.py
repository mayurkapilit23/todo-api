from pydantic import BaseModel, Field


class ApiResponse[T](BaseModel):
    status: bool = Field(..., description="Response status")
    message: str = Field(..., description="Response message")
    data: T | None = Field(None, description="Response data")