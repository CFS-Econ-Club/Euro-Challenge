#!/usr/bin/env python3
"""
Combine all markdown files in the repository into one file and count tokens.
"""

import os
from pathlib import Path
from typing import List, Tuple

# Files/directories to exclude
EXCLUDE_PATTERNS = [
    '.git',
    'node_modules',
    '__pycache__',
    '.qwen',
    'combine_markdown.py',
    'combined_output.md',
    '~$',  # Temporary Office files
]

# Files to always include first (in order)
PRIORITY_FILES = [
    'README.md',
    'TIMELINE.md',
    'CHECKLIST.md',
    'CLAUDE.md',
    'META.md',
]


def should_exclude(path: Path) -> bool:
    """Check if a path should be excluded."""
    path_str = str(path)
    for pattern in EXCLUDE_PATTERNS:
        if pattern in path_str:
            return True
    return False


def find_markdown_files(root: Path) -> List[Path]:
    """Find all markdown files in the repository."""
    md_files = []
    for path in root.rglob('*.md'):
        if not should_exclude(path):
            md_files.append(path)
    
    # Sort: priority files first, then alphabetically by path
    def sort_key(p: Path):
        rel_path = str(p.relative_to(root))
        if p.name in PRIORITY_FILES:
            return (0, PRIORITY_FILES.index(p.name) if p.name in PRIORITY_FILES else 999, '')
        return (1, 0, str(p))
    
    md_files.sort(key=sort_key)
    return md_files


def count_tokens(text: str) -> int:
    """
    Estimate token count using a simple heuristic.
    For more accurate counting, install tiktoken: pip install tiktoken
    """
    # Try to use tiktoken if available
    try:
        import tiktoken
        encoder = tiktoken.get_encoding('cl100k_base')  # GPT-4, GPT-3.5-turbo
        return len(encoder.encode(text))
    except ImportError:
        # Fallback: rough estimate (1 token ≈ 4 characters or 0.75 words)
        words = len(text.split())
        return int(words * 0.75) + len(text) // 4


def combine_markdown_files(root: Path, output_file: Path) -> Tuple[str, dict]:
    """Combine all markdown files into one."""
    md_files = find_markdown_files(root)
    
    combined_content = []
    file_stats = {}
    total_tokens = 0
    
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            rel_path = md_file.relative_to(root)
            tokens = count_tokens(content)
            
            # Add file header
            combined_content.append(f"\n\n{'='*80}")
            combined_content.append(f"## FILE: {rel_path.as_posix()}")
            combined_content.append(f"## TOKENS: {tokens}")
            combined_content.append(f"{'='*80}\n\n")
            combined_content.append(content)
            
            file_stats[str(rel_path)] = tokens
            total_tokens += tokens
            
        except Exception as e:
            print(f"Error reading {md_file}: {e}")
    
    # Write combined file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"# Combined Markdown Repository\n")
        f.write(f"**Total Files:** {len(file_stats)}\n")
        f.write(f"**Total Tokens:** {total_tokens}\n\n")
        f.write(f"## Table of Contents\n\n")
        for path, tokens in file_stats.items():
            f.write(f"- `{path}` ({tokens:,} tokens)\n")
        f.write('\n'.join(combined_content))
    
    return output_file.read_text(encoding='utf-8'), file_stats


def main():
    root = Path(__file__).parent.resolve()
    output_file = root / 'combined_output.md'
    
    print(f"Searching for markdown files in: {root}")
    print(f"Output file: {output_file}\n")
    
    combined_text, file_stats = combine_markdown_files(root, output_file)
    
    # Recount total including headers
    total_tokens = count_tokens(combined_text)
    
    print(f"✓ Combined {len(file_stats)} markdown files")
    print(f"\n📊 Token Count:")
    print(f"   Total tokens (including headers): {total_tokens:,}")
    print(f"\n📁 Files included:")
    
    # Sort by token count for display
    sorted_stats = sorted(file_stats.items(), key=lambda x: x[1], reverse=True)
    for path, tokens in sorted_stats:
        print(f"   {tokens:>8,} tokens  -  {path}")
    
    print(f"\n✅ Output written to: {output_file}")
    print(f"\n💡 Note: Token count uses tiktoken (cl100k_base) if available.")
    print(f"   Install with: pip install tiktoken")


if __name__ == '__main__':
    main()
