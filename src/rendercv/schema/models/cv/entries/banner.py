import typing

import pydantic

from .bases.entry import BaseEntry


class BannerEntry(BaseEntry):
    """cvxresume cover-page banner (large title + subtitle + call-to-action)."""

    banner_kind: typing.Literal["cover"] = pydantic.Field(
        default="cover",
        examples=["cover"],
    )
    title: str = pydantic.Field(
        default="快速预览",
        examples=["快速预览"],
    )
    subtitle: str = pydantic.Field(
        default="",
        examples=["以下为精简概览，便于快速建立印象。"],
    )
    cta: str = pydantic.Field(
        default="",
        examples=["完整简历见下页 →"],
    )
