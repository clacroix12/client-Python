from .errors import EntryCreatedError as EntryCreatedError, \
    OperationCompletionError as OperationCompletionError, \
    ResponseError as ResponseError
from logging import Logger

from typing import Text
from requests import Response

logger: Logger

def generate_uuid() -> Text: ...
def convert_string(value: Text) -> Text: ...
def dict_to_payload(dictionary: dict) -> list[dict]: ...
def gen_attributes(rp_attributes: list) -> list[dict]: ...
def get_launch_sys_attrs()-> dict[Text]: ...
def get_package_version(package_name:Text) -> Text: ...
def uri_join(*uri_parts: Text) -> Text: ...
def get_id(response: Response) -> Text: ...
def get_msg(response: Response) -> dict: ...
def get_data(response: Response) -> dict: ...
def get_json(response: Response) -> dict: ...
def get_error_messages(data: dict) -> list: ...
def verify_value_length(attributes: list[dict]) -> list[dict]: ...

def timestamp() -> Text: ...
