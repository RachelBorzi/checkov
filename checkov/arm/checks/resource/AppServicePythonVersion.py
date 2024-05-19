from checkov.arm.base_resource_value_check import BaseResourceValueCheck
from checkov.common.models.enums import CheckCategories, CheckResult


class AppServicePythonVersion(BaseResourceValueCheck):

    def __init__(self) -> None:
        name = "Ensure that 'Python version' is the latest, if used to run the web app"
        id = "CKV_AZURE_82"
        supported_resources = ("Microsoft.Web/sites",)
        categories = (CheckCategories.GENERAL_SECURITY,)
        super().__init__(
            name=name,
            id=id,
            categories=categories,
            supported_resources=supported_resources,
            missing_block_result=CheckResult.UNKNOWN)

    def get_inspected_key(self) -> str:
        return "properties/siteConfig/pythonVersion"

    def get_expected_value(self) -> str:
        return "3.10"


check = AppServicePythonVersion()

