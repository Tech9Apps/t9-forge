import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ToolkitContractsTest(unittest.TestCase):
    def test_rules_schema_has_required_keys(self):
        schema_path = ROOT / "config" / "rules-schema.json"
        self.assertTrue(schema_path.exists(), "rules schema must exist")

        schema = json.loads(schema_path.read_text())
        required = set(schema.get("required", []))
        self.assertIn("schemaVersion", required)
        self.assertIn("testingRules", required)
        self.assertIn("workflowRules", required)
        self.assertIn("projectProfile", required)

        properties = schema.get("properties", {})
        project_profile = properties.get("projectProfile", {}).get("properties", {})
        workflow_rules = properties.get("workflowRules", {}).get("properties", {})
        self.assertIn("runtimeCapabilities", project_profile)
        self.assertIn("workflowCapabilities", workflow_rules)
        self.assertIn("fallbackPolicy", workflow_rules)

    def test_target_configs_exist(self):
        target_dir = ROOT / "config" / "targets"
        claude = json.loads((target_dir / "claude.json").read_text())
        cursor = json.loads((target_dir / "cursor.json").read_text())
        self.assertEqual(claude["target"], "claude")
        self.assertEqual(cursor["target"], "cursor")
        self.assertTrue(claude["supportsHooks"])
        self.assertFalse(cursor["supportsHooks"])
        self.assertTrue(claude["supportsBrowserAutomation"])
        self.assertTrue(cursor["supportsBrowserAutomation"])
        self.assertTrue(claude["supportsGitHubPR"])
        self.assertTrue(cursor["supportsGitHubPR"])
        self.assertTrue(claude["supportsRuntimeArtifacts"])
        self.assertFalse(cursor["supportsRuntimeArtifacts"])

    def test_cursor_plugin_manifest_exists(self):
        manifest = ROOT / ".cursor-plugin" / "plugin.json"
        self.assertTrue(manifest.exists(), "cursor plugin manifest must exist")
        data = json.loads(manifest.read_text())
        self.assertEqual(data["name"], "claude-code-toolkit")
        self.assertIn("skills", data)
        self.assertIn("agents", data)

    def test_setup_and_alias_skills_exist(self):
        required_skills = [
            "init",
            "setup",
            "claude-setup",
            "cursor-setup",
            "project-setup",
        ]
        for skill in required_skills:
            path = ROOT / "skills" / skill / "SKILL.md"
            self.assertTrue(path.exists(), f"missing skill: {skill}")

    def test_generated_sdlc_skills_exist(self):
        required_templates = [
            "plan",
            "plan-verify",
            "test-generate",
            "plan-ceo-review",
            "plan-design-review",
            "ship",
            "qa",
            "qa-design-review",
            "retro",
            "document-release",
        ]
        for name in required_templates:
            path = ROOT / "templates" / "skills" / name / "SKILL.md"
            self.assertTrue(path.exists(), f"missing skill template: {name}")

    def test_generated_sdlc_commands_exist(self):
        required_commands = [
            "healthcheck.md",
            "logs.md",
            "serve.md",
            "deploy-status.md",
            "rollback-status.md",
        ]
        for name in required_commands:
            path = ROOT / "templates" / "commands" / name
            self.assertTrue(path.exists(), f"missing command template: {name}")

    def test_cursor_templates_exist(self):
        required_paths = [
            ROOT / "templates" / "cursor" / "AGENTS.md",
            ROOT / "templates" / "cursor" / "rules" / "architecture.mdc",
            ROOT / "templates" / "cursor" / "rules" / "api-and-data.mdc",
            ROOT / "templates" / "cursor" / "rules" / "testing.mdc",
            ROOT / "templates" / "cursor" / "rules" / "workflow.mdc",
        ]
        for path in required_paths:
            self.assertTrue(path.exists(), f"missing cursor template: {path}")

    def test_precommit_typecheck_chain_placeholder(self):
        precommit = (ROOT / "templates" / "hooks" / "pre-commit.json").read_text()
        self.assertIn("{{TYPECHECK_CHAIN}}", precommit)
        self.assertNotIn("&& {{TYPECHECK_COMMAND}} ||", precommit)

    def test_readme_no_test_on_edit_claim(self):
        readme = (ROOT / "README.md").read_text().lower()
        self.assertNotIn("test on edit", readme)

    def test_init_agent_requires_dynamic_stack_derived_questions(self):
        agent = (ROOT / "agents" / "init.md").read_text().lower()
        self.assertIn("stack-derived question packs", agent)
        self.assertIn("ask only questions that are relevant to detected technologies", agent)
        self.assertIn("capability matrix", agent)
        self.assertIn("fallback behavior when runtime capability is missing", agent)
        self.assertNotIn("next.js full-stack:", agent)
        self.assertNotIn("go backends:", agent)

    def test_cursor_rules_templates_are_always_apply(self):
        paths = [
            ROOT / "templates" / "cursor" / "rules" / "architecture.mdc",
            ROOT / "templates" / "cursor" / "rules" / "api-and-data.mdc",
            ROOT / "templates" / "cursor" / "rules" / "testing.mdc",
            ROOT / "templates" / "cursor" / "rules" / "workflow.mdc",
        ]
        for path in paths:
            text = path.read_text()
            self.assertIn("alwaysApply: true", text)
            self.assertNotIn("globs:", text)


if __name__ == "__main__":
    unittest.main()
