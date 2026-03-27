#!/usr/bin/env python3
"""Render mcp/evals.json as a formatted markdown table in mcp-evals.md."""

import json
import sys
from pathlib import Path

EVALS_PATH = Path(__file__).parent / "mcp" / "evals.json"
OUTPUT_PATH = Path(__file__).parent / "mcp-evals.md"


def render_tool_calls(tool_calls: list) -> list[str]:
    lines = []
    for i, tc in enumerate(tool_calls, start=1):
        tool = tc.get("tool", "")
        output = tc.get("output", {})
        formatted = json.dumps(output, indent=2)
        lines.append(f"{i}. `{tool}`")
        lines.append("   ```json")
        for ln in formatted.splitlines():
            lines.append(f"   {ln}")
        lines.append("   ```")
    return lines


def render_markdown(categories: list) -> list[str]:
    lines = []
    lines.append("# MCP Atlas Search Evals\n")

    total_evals = sum(
        len(feat["evals"])
        for cat in categories
        for feat in cat["features"]
    )
    lines.append(f"**{total_evals} evals** across **{len(categories)} categories**\n")

    for cat in categories:
        lines.append(f"---\n")
        lines.append(f"## {cat['name']}\n")

        # Summary table at top of each category
        lines.append("| Feature ID | Feature | Description | Evals |")
        lines.append("|------------|---------|-------------|-------|")
        for feat in cat["features"]:
            feat_id = feat["id"]
            feat_name = feat["name"].replace("|", "\\|")
            feat_desc = feat.get("description", "").replace("|", "\\|")
            lines.append(f"| `{feat_id}` | {feat_name} | {feat_desc} | {len(feat['evals'])} |")
        lines.append("")

        # Detail sections
        for feat in cat["features"]:
            lines.append(f"### `{feat['id']}` — {feat['name']}\n")
            if feat.get("description"):
                lines.append(f"> {feat['description']}\n")

            for j, ev in enumerate(feat["evals"], start=1):
                label = f"**Eval {j}**" if len(feat["evals"]) > 1 else "**Prompt**"
                lines.append(f"{label}: {ev['nl_prompt']}\n")
                lines.append("**Expected tool calls:**\n")
                lines.extend(render_tool_calls(ev["expected_tool_calls"]))
                lines.append("")

            lines.append("")

    return lines


def main():
    if not EVALS_PATH.exists():
        print(f"Error: {EVALS_PATH} not found", file=sys.stderr)
        sys.exit(1)

    with open(EVALS_PATH) as f:
        categories = json.load(f)

    md = "\n".join(render_markdown(categories))

    with open(OUTPUT_PATH, "w") as f:
        f.write(md)

    print(f"Written {OUTPUT_PATH} ({OUTPUT_PATH.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
