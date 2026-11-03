#!/usr/bin/env python3
"""Build the browser catalog from images stored in the repository."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "catalog.json"
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg"}


def display_name(stem: str) -> str:
    return " ".join(part.capitalize() for part in stem.replace("-", " ").replace("_", " ").split())


def main() -> None:
    items = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in IMAGE_EXTENSIONS:
            continue
        relative = path.relative_to(ROOT)
        category = relative.parts[0] if len(relative.parts) > 1 else "Other"
        items.append(
            {
                "path": relative.as_posix(),
                "filename": path.name,
                "name": display_name(path.stem),
                "category": category,
            }
        )

    items.sort(key=lambda item: (item["category"].casefold(), item["name"].casefold(), item["path"].casefold()))
    OUTPUT.write_text(json.dumps(items, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    print(f"Built catalog with {len(items)} images in {len({item['category'] for item in items})} categories.")


if __name__ == "__main__":
    main()
