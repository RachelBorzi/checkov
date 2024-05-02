from typing import Any

from checkov.arm.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import CheckCategories, CheckResult


class VnetSingleDNSServer(BaseResourceCheck):

    def __init__(self) -> None:
        """Using a single DNS server may indicate a single point of failure
        where the DNS IP address is not load balanced."""
        name = "Ensure that VNET has at least 2 connected DNS Endpoints"
        id = "CKV_AZURE_182"
        supported_resources = ("Microsoft.Network/networkInterfaces",)
        categories = (CheckCategories.NETWORKING,)
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf: dict[str, list[Any]]) -> CheckResult:
        if "properties" in conf and "dnsSettings" in conf["properties"]:
            if "dnsServers" in conf["properties"]["dnsSettings"] and isinstance(
                    conf["properties"]["dnsSettings"]["dnsServers"], list):
                dns_servers = conf["properties"]["dnsSettings"]["dnsServers"]
                if dns_servers and len(dns_servers) == 1:
                    self.evaluated_keys = ["dnsServers"]
                    return CheckResult.FAILED
            return CheckResult.PASSED


check = VnetSingleDNSServer()
