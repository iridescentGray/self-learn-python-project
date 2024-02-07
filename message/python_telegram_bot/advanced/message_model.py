import typing


class SendMsgBase(typing.TypedDict):
    parse: str
    type: str


class StatusMsg(SendMsgBase):
    """"""

    status: str


class HtmlMsg(SendMsgBase):
    """"""

    html: str


class ForceUserMsg(SendMsgBase):
    """"""

    rep: int


SendMsgModel = typing.Union[StatusMsg, HtmlMsg, ForceUserMsg]
