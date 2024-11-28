import json
from typing import Annotated

from fastapi import APIRouter, Header, HTTPException, status
from fastapi.responses import JSONResponse
from requests import HTTPError
from square_commons import get_api_output_in_standard_format

from square_common_bl.configuration import (
    global_object_square_logger,
    global_object_square_authentication_helper,
)
from square_common_bl.messages import messages

router = APIRouter(
    tags=["authentication"],
)


@router.delete("/logout/v0")
@global_object_square_logger.async_auto_logger
async def remove_app_for_self_v0(
    refresh_token: Annotated[str, Header()],
):

    try:
        """
        validation
        """
        # pass
        """
        main process
        """
        response = global_object_square_authentication_helper.logout_v0(
            refresh_token=refresh_token
        )
        """
        return value
        """

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=response,
        )
    except HTTPError as http_error:
        global_object_square_logger.logger.error(http_error, exc_info=True)
        """
        rollback logic
        """
        # pass
        return JSONResponse(
            status_code=http_error.response.status_code,
            content=json.loads(http_error.response.content),
        )
    except HTTPException as http_exception:
        global_object_square_logger.logger.error(http_exception, exc_info=True)
        """
        rollback logic
        """
        # pass
        return JSONResponse(
            status_code=http_exception.status_code, content=http_exception.detail
        )
    except Exception as e:
        global_object_square_logger.logger.error(e, exc_info=True)
        """
        rollback logic
        """
        # pass
        output_content = get_api_output_in_standard_format(
            message=messages["GENERIC_500"],
            log=str(e),
        )
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=output_content
        )


@router.get("/generate_access_token/v0")
@global_object_square_logger.async_auto_logger
async def generate_access_token_v0(
    refresh_token: Annotated[str, Header()],
):

    try:
        """
        validation
        """
        # pass
        """
        main process
        """
        response = global_object_square_authentication_helper.generate_access_token_v0(
            refresh_token=refresh_token
        )
        """
        return value
        """

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=response,
        )
    except HTTPError as http_error:
        global_object_square_logger.logger.error(http_error, exc_info=True)
        """
        rollback logic
        """
        # pass
        return JSONResponse(
            status_code=http_error.response.status_code,
            content=json.loads(http_error.response.content),
        )
    except HTTPException as http_exception:
        global_object_square_logger.logger.error(http_exception, exc_info=True)
        """
        rollback logic
        """
        # pass
        return JSONResponse(
            status_code=http_exception.status_code, content=http_exception.detail
        )
    except Exception as e:
        global_object_square_logger.logger.error(e, exc_info=True)
        """
        rollback logic
        """
        # pass
        output_content = get_api_output_in_standard_format(
            message=messages["GENERIC_500"],
            log=str(e),
        )
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=output_content
        )
