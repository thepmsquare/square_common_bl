from pydantic import BaseModel


class GetAppIdV0Response(BaseModel):
    main: str
