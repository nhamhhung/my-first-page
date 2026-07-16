"""Gate-1 contract tests — no network, no keys."""
import ast
import os
import unittest

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARD = open(os.path.join(HERE, "agent.yaml")).read()
APP = open(os.path.join(HERE, "app.py")).read()


class TestContract(unittest.TestCase):
    def test_v1_workload_shape(self):
        self.assertIn("apiVersion: platform.solo-unicorn.ai/v1", CARD)
        self.assertRegex(CARD, r"kind: (Workload|Application)")
        self.assertRegex(CARD, r'health: "?/healthz"?')

    def test_no_platform_wiring_or_kill_switch(self):
        self.assertNotIn("provider:", CARD)
        self.assertNotIn("governance:", CARD)
        self.assertNotIn("AGENT_ENABLED", CARD)

    def test_no_literal_secrets(self):
        for marker in ("sk-ant-a", "xoxb-", "password:"):
            self.assertNotIn(marker, CARD)

    def test_app_parses(self):
        ast.parse(APP)


if __name__ == "__main__":
    unittest.main()
