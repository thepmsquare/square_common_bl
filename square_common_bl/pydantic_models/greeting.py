from typing import Optional

from pydantic import BaseModel


class CreateAnonymousGreetingV0(BaseModel):
    greeting_anonymous_sender_name: Optional[str] = None
    greeting_text: Optional[str] = None


class CreateAnonymousGreetingV0ResponseMain(BaseModel):
    greeting_anonymous_sender_name: str | None
    user_id: str | None
    greeting_id: int
    greeting_datetime: str
    greeting_is_anonymous: bool
    greeting_text: str | None


class CreateAnonymousGreetingV0Response(BaseModel):
    main: list[CreateAnonymousGreetingV0ResponseMain]
