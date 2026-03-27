#!/usr/bin/env python3
"""Render mcp/evals.json as a formatted markdown table in mcp-evals.md."""

import json
import sys
from pathlib import Path

EVALS_PATH = Path(__file__).parent / "mcp" / "evals.json"
OUTPUT_PATH = Path(__file__).parent / "mcp-evals.md"


def format_json_for_cell(output: object) -> str:
    """Pretty-print JSON for use inside a markdown table cell."""
    formatted = json.dumps(output, indent=2)
    lines = []
    for line in formatted.splitlines():
        # Count leading spaces and replace with &nbsp; to preserve indentation
        stripped = line.lstrip(" ")
        spaces = len(line) - len(stripped)
        lines.append("&nbsp;" * spaces + stripped)
    return "<code>" + "<br>".join(lines) + "</code>"


def tool_calls_summary(tool_calls: list) -> str:
    parts = []
    for tc in tool_calls:
        tool = tc.get("tool", "")
        output = tc.get("output", {})
        parts.append(f"`{tool}` →<br>{format_json_for_cell(output)}")
    return "<br><br>".join(parts)


def escape_pipe(text: str) -> str:
    return text.replace("|", "\\|")


def render_markdown(categories: list) -> str:
    lines = []
    lines.append("# MCP Atlas Search Evals\n")

    total_evals = sum(
        len(feat["evals"])
        for cat in categories
        for feat in cat["features"]
    )
    lines.append(f"**{total_evals} evals** across **{len(categories)} categories**\n")

    for cat in categories:
        lines.append(f"## {cat['name']}\n")
        lines.append("| Feature ID | Feature | Description | Prompt | Expected Tool Calls |")
        lines.append("|------------|---------|-------------|--------|---------------------|")

        for feat in cat["features"]:
            feat_id = feat["id"]
            feat_name = escape_pipe(feat["name"])
            feat_desc = escape_pipe(feat.get("description", ""))

            for i, ev in enumerate(feat["evals"]):
                prompt = escape_pipe(ev["nl_prompt"])
                calls = escape_pipe(tool_calls_summary(ev["expected_tool_calls"]))

                # Only show feature id/name/desc on the first row for that feature
                if i == 0:
                    lines.append(f"| `{feat_id}` | {feat_name} | {feat_desc} | {prompt} | {calls} |")
                else:
                    lines.append(f"| | | | {prompt} | {calls} |")

        lines.append("")  # blank line between sections

    return "\n".join(lines)


def main():
    if not EVALS_PATH.exists():
        print(f"Error: {EVALS_PATH} not found", file=sys.stderr)
        sys.exit(1)

    with open(EVALS_PATH) as f:
        categories = json.load(f)

    md = render_markdown(categories)

    with open(OUTPUT_PATH, "w") as f:
        f.write(md)

    print(f"Written {OUTPUT_PATH} ({OUTPUT_PATH.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
