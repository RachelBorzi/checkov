import unittest
from pathlib import Path

from checkov.arm.runner import Runner
from checkov.runner_filter import RunnerFilter
from checkov.arm.checks.resource.AzureSearchManagedIdentity import check


class TestAzureSearchManagedIdentity(unittest.TestCase):

    def test_summary(self):
        # given
        test_files_dir = Path(__file__).parent / "example_AzureSearchManagedIdentity"

        # when
        report = Runner().run(root_folder=str(test_files_dir), runner_filter=RunnerFilter(checks=[check.id]))

        # then
        summary = report.get_summary()

        passing_resources = {
            "Microsoft.Web/sites.pass",
            "Microsoft.Search/searchServices.pass2",
        }
        failing_resources = {
            "Microsoft.Web/sites.fail",
            "Microsoft.Search/searchServices.fail2",
        }

        passed_check_resources = {c.resource for c in report.passed_checks}
        failed_check_resources = {c.resource for c in report.failed_checks}

        self.assertEqual(summary["passed"], len(passing_resources))
        self.assertEqual(summary["failed"], len(failing_resources))
        self.assertEqual(summary["skipped"], 0)
        self.assertEqual(summary["parsing_errors"], 0)

        self.assertEqual(passing_resources, passed_check_resources)
        self.assertEqual(failing_resources, failed_check_resources)