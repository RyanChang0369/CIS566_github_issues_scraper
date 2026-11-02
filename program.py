"""
program.py

Authors: rchang
Created: 2026-11-01
"""

import json
import re
import sys
from pathlib import Path
from typing import Any

from requests_cache import CachedSession


def main() -> int:
    """
    Main execution entry point for the program.
    :return: Exit code of the program.
    """

    cfg: dict[str, Any] = load_config()
    filtered_data = []

    for proj in cfg["projects"]:
        p_str = "/".join(proj)
        base_path = Path("issues") / p_str
        base_path.mkdir(parents=True, exist_ok=True)

        for issue in get_all_issues(p_str, base_path):
            issue_filtered = filter_issue(cfg, issue, base_path)

            if issue_filtered is None:
                continue

            filtered_data.append(issue_filtered)

        with open(base_path / "issues_filtered.json", "wt") as fh:
            json.dump(filtered_data, fh, indent="  ")

    return 0


def load_config() -> dict[str, Any]:
    """
    Load config from config.json
    :return: The program configuration.
    """
    with open("config.json", "rt") as fh:
        cfg: dict[str, Any] = json.load(fh)
    return cfg


def get_all_issues(project_id: str, base_path: Path) -> list[dict]:
    """
    Get issues from the `project_id`.
    :param project_id: The project id.
    :param base_path: Base path to write the json file.
    :return: The issue data in json form.
    """
    s = CachedSession()
    r = s.get(f"https://api.github.com/repos/{project_id}/issues")
    data: list[dict] = r.json()

    with open(base_path / "issues_all.json", "wt") as fh:
        json.dump(data, fh)

    return data


def filter_issue(cfg: dict[str, Any], issue: dict, base_path: Path):
    """
    Filters fields within an issue. Also filters which issues to include.
    :param cfg: The configuration `dict`.
    :param issue: The issue.
    :param base_path: The base path where the files will be written.
    :return: The issue with select fields, or `None` if that issue wasn't
    selected.
    """
    title: str = issue["title"]
    body: str = issue["body"]
    fields: list[str] = cfg["field_select"]

    for rx in cfg["issue_select"]["regex"]:
        rx = re.compile(rx)
        if rx.search(title) or rx.search(body):
            filtered: dict[str, Any] = {}
            for f in fields:
                filtered[f] = issue[f]

            # Write to Markdown file
            path = base_path / str(filtered["id"]) / "document.md"
            path.parent.mkdir(parents=True, exist_ok=True)

            with open(path, "wt") as fh:
                fh.write(f"# {title}\n\n")
                fh.write(body)

            return filtered

    return None

if __name__ == "__main__":
    sys.exit(main())
