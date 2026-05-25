---
description: "View recent application logs and CI/CD output."
---

# View Logs

Show recent logs or CI/CD output.

## Instructions

Check for and display available logs:

### Application Logs
```bash
{{LOG_COMMAND}}
```

<!-- Examples:
  Node: tail -50 logs/app.log or npm run logs
  Python: tail -50 logs/app.log
  Docker: docker-compose logs --tail=50
  Systemd: journalctl -u <service> -n 50
-->

### CI/CD Status
```bash
{{CI_STATUS_COMMAND}}
```

<!-- Examples:
  GitHub Actions: gh run list --limit 5 && gh run view <latest>
  GitLab CI: glab ci list
-->

### Git Log
```bash
git log --oneline -20
```

Present the most relevant logs based on what's available in this project. If specific logs are requested via arguments, show those.

$ARGUMENTS
