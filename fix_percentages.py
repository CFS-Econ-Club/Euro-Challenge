with open("06-qa-prep/qa-master-document.md", "r", encoding="utf-8") as f:
    text = f.read()
    
text = text.replace("24% of our package", "49% of our package")

with open("06-qa-prep/qa-master-document.md", "w", encoding="utf-8") as f:
    f.write(text)

print("Done")
