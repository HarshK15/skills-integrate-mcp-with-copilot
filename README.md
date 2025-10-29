# Integrate MCP with Copilot

<img src="https://octodex.github.com/images/Professortocat_v2.png" align="right" height="200px" />

Hey HarshK15!

Mona here. I'm done preparing your exercise. Hope you enjoy! 💚

Remember, it's self-paced so feel free to take a break! ☕️

[![](https://img.shields.io/badge/Go%20to%20Exercise-%E2%86%92-1f883d?style=for-the-badge&logo=github&labelColor=197935)](https://github.com/HarshK15/skills-integrate-mcp-with-copilot/issues/1)


&copy; 2025 GitHub &bull; [Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) &bull; [MIT License](https://gh.io/mit)

## Running the example MCP endpoints

This repository includes a minimal MCP-like provider implemented as two HTTP
endpoints in `src/app.py`:

- `GET /mcp/context` — returns a small set of project files (for use as model
	context)
- `GET /mcp/summary` — returns a compact project summary

To run the app locally:

```bash
pip install -r requirements.txt
uvicorn src.app:app --reload --host 0.0.0.0 --port 8000
```

Then try the MCP endpoints:

```bash
curl -s http://localhost:8000/mcp/summary | jq
curl -s http://localhost:8000/mcp/context | jq '.files | keys'
```

This is a small, safe example meant for learning; a production MCP provider
should include authentication, careful filtering of file contents, rate
limiting, and other protections.

