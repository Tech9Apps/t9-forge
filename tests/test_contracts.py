import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ToolkitContractsTest(unittest.TestCase):

    # -- Config contracts --

    def test_rules_schema_has_required_keys(self):
        schema_path = ROOT / "config" / "rules-schema.json"
        self.assertTrue(schema_path.exists(), "rules schema must exist")

        schema = json.loads(schema_path.read_text())
        required = set(schema.get("required", []))
        for key in ("schemaVersion", "testingRules", "workflowRules", "projectProfile"):
            self.assertIn(key, required)

        properties = schema.get("properties", {})
        project_profile = properties.get("projectProfile", {}).get("properties", {})
        workflow_rules = properties.get("workflowRules", {}).get("properties", {})
        self.assertIn("runtimeCapabilities", project_profile)
        self.assertIn("workflowCapabilities", workflow_rules)
        self.assertIn("fallbackPolicy", workflow_rules)

    def test_target_configs_exist_and_valid(self):
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

    # -- Plugin manifests --

    def test_claude_plugin_manifest(self):
        manifest = ROOT / ".claude-plugin" / "plugin.json"
        self.assertTrue(manifest.exists())
        data = json.loads(manifest.read_text())
        self.assertEqual(data["name"], "claude-code-toolkit")

    def test_cursor_plugin_manifest(self):
        manifest = ROOT / ".cursor-plugin" / "plugin.json"
        self.assertTrue(manifest.exists())
        data = json.loads(manifest.read_text())
        self.assertEqual(data["name"], "claude-code-toolkit")
        self.assertIn("skills", data)
        self.assertIn("agents", data)

    # -- Entrypoint skills --

    def test_setup_and_alias_skills_exist(self):
        for skill in ("init", "setup", "claude-setup", "cursor-setup", "project-setup"):
            path = ROOT / "skills" / skill / "SKILL.md"
            self.assertTrue(path.exists(), f"missing entrypoint skill: {skill}")

    # -- Template integrity (dynamic — no hardcoded lists to drift) --

    def test_every_skill_template_dir_has_skill_md(self):
        skills_dir = ROOT / "templates" / "skills"
        dirs = [d for d in skills_dir.iterdir() if d.is_dir()]
        self.assertGreater(len(dirs), 0, "no skill template directories found")
        for d in dirs:
            self.assertTrue(
                (d / "SKILL.md").exists(),
                f"skill template dir {d.name}/ missing SKILL.md",
            )

    def test_every_command_template_is_markdown(self):
        commands_dir = ROOT / "templates" / "commands"
        files = list(commands_dir.iterdir())
        self.assertGreater(len(files), 0, "no command templates found")
        for f in files:
            self.assertTrue(
                f.suffix == ".md",
                f"command template {f.name} is not .md",
            )

    def test_every_hook_template_is_json(self):
        hooks_dir = ROOT / "templates" / "hooks"
        files = list(hooks_dir.iterdir())
        self.assertGreater(len(files), 0, "no hook templates found")
        for f in files:
            self.assertTrue(f.suffix == ".json", f"hook template {f.name} is not .json")
            json.loads(f.read_text())

    def test_agent_templates_exist(self):
        agents_dir = ROOT / "templates" / "agents"
        files = [f for f in agents_dir.iterdir() if f.suffix == ".md"]
        self.assertGreater(len(files), 0, "no agent templates found")

    # -- Minimum template counts (catch accidental mass deletion) --

    def test_minimum_skill_template_count(self):
        skills_dir = ROOT / "templates" / "skills"
        count = len([d for d in skills_dir.iterdir() if d.is_dir()])
        self.assertGreaterEqual(count, 15, f"expected >= 15 skill templates, found {count}")

    def test_minimum_command_template_count(self):
        commands_dir = ROOT / "templates" / "commands"
        count = len(list(commands_dir.iterdir()))
        self.assertGreaterEqual(count, 5, f"expected >= 5 command templates, found {count}")

    def test_minimum_hook_template_count(self):
        hooks_dir = ROOT / "templates" / "hooks"
        count = len(list(hooks_dir.iterdir()))
        self.assertGreaterEqual(count, 5, f"expected >= 5 hook templates, found {count}")

    # -- Cursor templates --

    def test_cursor_templates_exist(self):
        for path in (
            ROOT / "templates" / "cursor" / "AGENTS.md",
            ROOT / "templates" / "cursor" / "rules" / "architecture.mdc",
            ROOT / "templates" / "cursor" / "rules" / "api-and-data.mdc",
            ROOT / "templates" / "cursor" / "rules" / "testing.mdc",
            ROOT / "templates" / "cursor" / "rules" / "workflow.mdc",
        ):
            self.assertTrue(path.exists(), f"missing cursor template: {path}")

    def test_cursor_rules_templates_are_always_apply(self):
        for name in ("architecture.mdc", "api-and-data.mdc", "testing.mdc", "workflow.mdc"):
            text = (ROOT / "templates" / "cursor" / "rules" / name).read_text()
            self.assertIn("alwaysApply: true", text)
            self.assertNotIn("globs:", text)

    # -- Hook-specific contracts --

    def test_precommit_typecheck_chain_placeholder(self):
        precommit = (ROOT / "templates" / "hooks" / "pre-commit.json").read_text()
        self.assertIn("{{TYPECHECK_CHAIN}}", precommit)
        self.assertNotIn("&& {{TYPECHECK_COMMAND}} ||", precommit)

    # -- Doc/README contracts --

    def test_readme_no_test_on_edit_claim(self):
        readme = (ROOT / "README.md").read_text().lower()
        self.assertNotIn("test on edit", readme)

    # -- Init agent contracts --

    def test_init_agent_requires_dynamic_stack_derived_questions(self):
        agent = (ROOT / "agents" / "init.md").read_text().lower()
        self.assertIn("stack-derived question packs", agent)
        self.assertIn("ask only questions that are relevant to detected technologies", agent)
        self.assertIn("capability matrix", agent)
        self.assertIn("fallback behavior when runtime capability is missing", agent)
        self.assertNotIn("next.js full-stack:", agent)
        self.assertNotIn("go backends:", agent)


if __name__ == "__main__":
    unittest.main()
