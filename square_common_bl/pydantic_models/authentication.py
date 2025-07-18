from typing import List, Optional

from pydantic import BaseModel


class DeleteUserV0(BaseModel):
    password: str


class UpdatePasswordV0(BaseModel):
    old_password: str
    new_password: str
    logout_other_sessions: bool = False
    preserve_session_refresh_token: Optional[str] = None


class LogoutAppsV0(BaseModel):
    app_names: List[str]


class ValidateEmailVerificationCodeV0(BaseModel):
    verification_code: str
