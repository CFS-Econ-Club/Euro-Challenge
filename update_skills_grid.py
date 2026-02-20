import re

with open("06-qa-prep/qa-master-document.md", "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace("Q6: How do you ensure green skills training leads to jobs?", "Q6: How do you ensure the Klimaatkorps leads to jobs?")
text = text.replace("grid modernization enables farm solar", "DCOI grid optimization enables farm solar")
text = text.replace("(green skills)", "(the Klimaatkorps)")
text = text.replace("green skills increase employment", "Klimaatkorps hiring increases employment")
text = text.replace("create a severe skills mismatch", "have recruited a Klimaatkorps with no grid projects to work on")
text = text.replace("these skills are immediately transferable", "these workers are immediately transferable")
text = text.replace("Skills accelerate both", "The Klimaatkorps accelerates both")
text = text.replace("labor mobility through skills training.", "labor mobility through the Klimaatkorps.")
text = text.replace("workforce skills", "direct-hire workforce solutions")
text = text.replace("skills training", "the Klimaatkorps")
text = text.replace("skills shortage", "labor shortage")
text = text.replace("grid modernization", "grid optimization (DCOI)")
text = text.replace("Grid Modernization", "DCOI Grid Operations")

with open("06-qa-prep/qa-master-document.md", "w", encoding="utf-8") as f:
    f.write(text)

print("Done")
