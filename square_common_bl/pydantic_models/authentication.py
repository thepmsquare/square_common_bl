from typing import List, TypeAlias

from pydantic import BaseModel
from square_commons.api_utils import StandardResponse
from square_database_structure.square.authentication.enums import RecoveryMethodEnum


class DeleteUserV0(BaseModel):
    password: str


class LogoutAppsV0(BaseModel):
    app_names: List[str]


class ValidateEmailVerificationCodeV0(BaseModel):
    verification_code: str


class SendResetPasswordEmailV0(BaseModel):
    username: str


class UpdateUserRecoveryMethodsV0(BaseModel):
    recovery_methods_to_add: List[RecoveryMethodEnum] = None
    recovery_methods_to_remove: List[RecoveryMethodEnum] = None


DeleteUserV0Response: TypeAlias = StandardResponse[None]


class UpdateUsernameV0ResponseMain(BaseModel):
    user_id: str
    username: str


class UpdateUsernameV0Response(BaseModel):
    main: UpdateUsernameV0ResponseMain


class GetUserDetailsV0ResponseMainProfile(BaseModel):
    user_profile_id: int
    user_profile_photo_storage_token: str | None
    user_profile_email: str | None
    user_profile_phone_number_country_code: str | None
    user_profile_phone_number: str | None
    user_profile_first_name: str | None
    user_profile_last_name: str | None
    user_profile_email_verified: str | None


class GetUserDetailsV0ResponseMainSession(BaseModel):
    app_name: str
    active_sessions: int


class GetUserDetailsV0ResponseMainEmailVerification(BaseModel):
    expires_at: str
    cooldown_reset_at: str


class GetUserDetailsV0ResponseMainBackupCodes(BaseModel):
    total: int
    available: int
    generated_at: str


class GetUserDetailsV0ResponseMain(BaseModel):
    user_id: str
    username: str
    profile: GetUserDetailsV0ResponseMainProfile
    apps: List[str]
    sessions: List[GetUserDetailsV0ResponseMainSession]
    recovery_methods: Dict[str, bool]
    email_verification_details: GetUserDetailsV0ResponseMainEmailVerification | None
    backup_code_details: GetUserDetailsV0ResponseMainBackupCodes | None


class GetUserDetailsV0Response(BaseModel):
    main: GetUserDetailsV0ResponseMain
