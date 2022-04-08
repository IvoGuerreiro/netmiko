from netmiko.cisco_base_connection import CiscoBaseConnection, CiscoFileTransfer
from netmiko.base_connection import BaseConnection
from netmiko.cisco.cisco_ios import CiscoIosBase


class RuckusSmartzoneSSH(CiscoIosBase):
    """Ruckus IOS SSH driver."""

    def config_mode(
        self,
        config_command: str = "config",
        pattern: str = "",
        re_flags: int = 0,
    ) -> str:
        return super().config_mode(
            config_command=config_command, pattern=pattern, re_flags=re_flags
        )
