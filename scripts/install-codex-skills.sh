#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source_dir="$repo_root/.codex/skills"
target_dir="${CODEX_HOME:-$HOME/.codex}/skills"

if [[ ! -d "$source_dir" ]]; then
  echo "No repo skills found at: $source_dir" >&2
  exit 1
fi

mkdir -p "$target_dir"

for skill_path in "$source_dir"/*; do
  [[ -d "$skill_path" ]] || continue
  skill_name="$(basename "$skill_path")"

  if command -v rsync >/dev/null 2>&1; then
    mkdir -p "$target_dir/$skill_name"
    rsync -a --delete "$skill_path"/ "$target_dir/$skill_name"/
  else
    rm -rf "$target_dir/$skill_name"
    cp -R "$skill_path" "$target_dir/$skill_name"
  fi
done

echo "Installed Codex skills from:"
echo "  $source_dir"
echo "to:"
echo "  $target_dir"
echo
echo "Restart Codex so newly installed skills are discovered."
