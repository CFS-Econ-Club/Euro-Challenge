#!/usr/bin/env python3
"""Count spoken words in speaker scripts - only text within quotation marks."""
import re
import os

def count_spoken_words(filepath):
    """Count only words within quotation marks (actual spoken dialogue)."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all text within quotation marks
    spoken_parts = re.findall(r'"([^"]+)"', content)
    
    # Join all spoken parts
    all_spoken = ' '.join(spoken_parts)
    
    # Remove bracketed stage directions within quotes
    all_spoken = re.sub(r'\[.*?\]', '', all_spoken)
    
    # Remove markdown formatting
    all_spoken = re.sub(r'\*\*|\*', '', all_spoken)
    
    # Count words
    words = all_spoken.split()
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

print("=" * 85)
print("SPEAKER SCRIPT TIMING ANALYSIS - Post Euro Angle Enhancement")
print("=" * 85)
print(f"{'Speaker':<12} {'Words':<10} {'Est Time':<12} {'+10%':<12} {'Allocated':<12} {'Variance':<10} {'Status'}")
print("-" * 85)

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
    
    print(f"{script_name[:12]:<12} {word_count:<10} {fmt_time(estimated_minutes):<12} {fmt_time(adjusted_minutes):<12} {fmt_time(allocated_minutes):<12} {int(variance_seconds):>+4d} sec    {status}")

print("-" * 85)
if all_good:
    print("RESULT: All speakers within 10% of allocation - PASS")
else:
    print("RESULT: Some speakers need adjustment - USE CUT MARKERS")
print("=" * 85)

# Print summary of changes
print("\nNOTE: Cut markers already exist in Speaker 1 and Speaker 5 scripts.")
print("Speakers should use cut markers if running over time during practice.")
