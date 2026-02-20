with open("06-qa-prep/qa-master-document.md", "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace("created a severe skills mismatch", "recruited a Klimaatkorps with no grid capacities to manage")

with open("06-qa-prep/qa-master-document.md", "w", encoding="utf-8") as f:
    f.write(text)

