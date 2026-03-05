#!/usr/bin/env python3
"""Count spoken words in speaker scripts (excluding stage directions and metadata)."""
import re
import os

def count_spoken_words(filepath):
    """Count words that would actually be spoken (exclude bracketed directions, headers, etc.)."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove bracketed stage directions like [PAUSE], [SLIDE X], [EYE CONTACT]
    content = re.sub(r'\[.*?\]', '', content)
    
    # Remove markdown headers
    content = re.sub(r'^#+\s.*$', '', content, flags=re.MULTILINE)
    
    # Remove table rows
    content = re.sub(r'^\|.*\|$', '', content, flags=re.MULTILINE)
    
    # Remove bullet points
    content = re.sub(r'^\s*[-*]\s+', '', content, flags=re.MULTILINE)
    
    # Remove numbered list items
    content = re.sub(r'^\s*\d+\.\s+', '', content, flags=re.MULTILINE)
    
    # Remove code blocks
    content = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
    
    # Remove section headers we don't want to count
    content = re.sub(r'^---$', '', content, flags=re.MULTILINE)
    content = re.sub(r'^Key Data Points.*$', '', content, flags=re.MULTILINE)
    content = re.sub(r'^Sources.*$', '', content, flags=re.MULTILINE)
    content = re.sub(r'^Files Modified:.*$', '', content, flags=re.MULTILINE)
    content = re.sub(r'^Files Created:.*$', '', content, flags=re.MULTILINE)
    
    # Count remaining words
    words = content.split()
    return len(words)

# Speaker scripts and their allocated times
scripts = [
    ('speaker-1-script.md', 3.5),   # 3:30 = 3.5 minutes
    ('speaker-2-script.md', 2.5),   # 2:30 = 2.5 minutes
    ('speaker-3-script.md', 3.5),   # 3:30 = 3.5 minutes
    ('speaker-4-script.md', 3.5),   # 3:30 = 3.5 minutes
    ('speaker-5-script.md', 2.0),   # 2:00 = 2.0 minutes
]

base_path = r'C:\Users\user\Documents\Euro-Challenge\04-presentation'

print("=" * 80)
print("SPEAKER SCRIPT TIMING ANALYSIS")
print("=" * 80)
print(f"{'Speaker':<10} {'Words':<10} {'Est. Time':<12} {'+10%':<12} {'Allocated':<12} {'Variance':<12} {'Status'}")
print("-" * 80)

all_good = True
for script_name, allocated_minutes in scripts:
    filepath = os.path.join(base_path, script_name)
    word_count = count_spoken_words(filepath)
    
    # Calculate time at 150 words/minute
    estimated_minutes = word_count / 150
    adjusted_minutes = estimated_minutes * 1.10  # Add 10% for pauses
    
    allocated_seconds = allocated_minutes * 60
    adjusted_seconds = adjusted_minutes * 60
    variance_seconds = adjusted_seconds - allocated_seconds
    
    # Determine status
    variance_pct = (adjusted_seconds - allocated_seconds) / allocated_seconds * 100
    if abs(variance_pct) <= 5:
        status = "OK"
    elif abs(variance_pct) <= 10:
        status = "MARGIN"
    elif variance_pct > 10:
        status = "OVER"
        all_good = False
    else:
        status = "UNDER"
    
    def fmt_time(minutes):
        mins = int(minutes)
        secs = int((minutes - mins) * 60)
        return f"{mins}:{secs:02d}"
    
    print(f"{script_name[:10]:<10} {word_count:<10} {fmt_time(estimated_minutes):<12} {fmt_time(adjusted_minutes):<12} {fmt_time(allocated_minutes):<12} {variance_seconds:+>5.0f} sec   {status}")

print("-" * 80)
if all_good:
    print("RESULT: All speakers within 10% of allocation - PASS")
else:
    print("RESULT: Some speakers need adjustment - NEEDS WORK")
print("=" * 80)
