import unittest
from pyhammer.tasks.taskbase import TaskBase
from pyhammer.reporters.memoryreporter import MemoryReporter
from tests.utils import ApproveStep, ReportStep

class testAbstractStep(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)

    def test_fail(self):
        step = TaskBase()
        self.assertFalse(step.build())

    def test_success(self):
        step = ApproveStep()
        self.assertTrue(step.build())

    def test_reporter(self):
        reporter = MemoryReporter()
        reportStep = ReportStep()
        reportStep.setReporter(reporter)
        reportStep.build()
        self.assertEqual(reporter.getText(), '\nok')

    def test_failureStep(self):
        step = TaskBase()
        reporter = MemoryReporter()
        reportStep = ReportStep()
        step.setFailureStep(reportStep)
        step.setReporter(reporter)

        self.assertEqual(step.reporter, reporter)
        self.assertEqual(reportStep.reporter, reporter)

        self.assertFalse(step.build())
        self.assertEqual(reporter.getText(), '\nok')

if __name__ == '__main__':
    unittest.main()
