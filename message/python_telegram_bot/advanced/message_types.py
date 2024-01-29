import typing


class RPCSendMsgBase(typing.TypedDict):
    pass


class RPCStatusMsg(RPCSendMsgBase):
    """Used for Status, Startup and Warning messages"""

    type: int
    status: str


class RPCHtmlMsg(RPCSendMsgBase):
    """Used for Status, Startup and Warning messages"""

    type: int
    html: str


RPCSendMsg = typing.Union[RPCStatusMsg, RPCHtmlMsg]
