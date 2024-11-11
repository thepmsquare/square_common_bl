from typing import Optional

from pydantic import BaseModel
from pydantic.v1 import UUID4


class CreateGreetingV0(BaseModel):
    app_id: Optional[int] = None
    greeting_is_anonymous: bool
    greeting_anonymous_sender_name: Optional[str] = None
    user_id: Optional[UUID4] = None
    greeting_text: Optional[str] = None
