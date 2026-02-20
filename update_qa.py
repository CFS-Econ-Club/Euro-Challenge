import re

with open("06-qa-prep/qa-master-document.md", "r", encoding="utf-8") as f:
    text = f.read()

# Core numbers
text = text.replace("€17 billion", "€8.1 billion")
text = text.replace("€17B", "€8.1B")
text = text.replace("17 billion", "8.1 billion")
text = text.replace("€2.8 billion annually is just 0.25%", "€1.6 billion annually is just 0.15%")
text = text.replace("€2.8 billion annual cost", "€1.6 billion annual cost")
text = text.replace("0.25% to the deficit", "0.15% to the deficit")

# Specific sentences & policy explanations
text = text.replace("€10 billion grid investment", "€600 million grid optimization investment")
text = text.replace("€10 billion grid allocation", "€600 million DCOI allocation")
text = text.replace("€10B for grid modernization (based on TenneT's €30B investment plan)", "€600M for the Dutch Capacity Operations Initiative (GOPACS, non-firm contracts, DLR)")
text = text.replace("€2B for skills training (based on MBO costs and employer tax credits)", "€2.5B for the Klimaatkorps & Sectoral Job Guarantees")
text = text.replace("skills training (Policy 3)", "The Klimaatkorps (Policy 3)")
text = text.replace("Green Skills Training", "The Klimaatkorps")
text = text.replace("skills program", "Klimaatkorps")
text = text.replace("MBO training programs in Policy 3", "Klimaatkorps direct-hires in Policy 3")
text = text.replace("actual MBO enrollment data", "standard public sector hiring costs for the Klimaatkorps")

# NQ3
text = text.replace("your 'green skills' workers will be trained for jobs", "your Klimaatkorps workers will be hired for jobs")

# FC1 Follow up
text = text.replace("First, €8.1 billion over 5-7 years is €2.8 billion annually—just 0.25% of GDP", "First, €8.1 billion over 5 years is €1.6 billion annually—just 0.15% of GDP")

# FC15 Follow up
text = text.replace("Second, our €600 million DCOI allocation is focused specifically on the *acceleration* components—permitting, smart grid tech, and storage—rather than just raw material costs which are more volatile.", "Second, our €600 million DCOI allocation avoids physical construction overrun risk entirely because it focuses on software, non-firm contracts, and Dynamic Line Rating.")

# NQ8
text = text.replace("Our Policy 1 focuses on immediate relief—smart grids, battery storage, and accelerated permitting for renewables—which can be deployed in 2-3 years.", "Our Policy 1 focuses on immediate relief—smart grids, non-firm contracts (GOPACS), and Dynamic Line Rating—which unlock capacity immediately.")

# NQ3 body
text = text.replace("grid modernization isn't just about laying new high-voltage cables (which takes years to permit). It involves deploying smart meters, battery storage, and local distribution upgrades", "DCOI isn't just about laying cables. It involves deploying smart grid solutions, GOPACS coordination, and Dynamic Line Rating")

# Policy 3 specific job QA
text = text.replace("Three mechanisms: (1) employer co-design of curriculum, (2) employer tax credit (€5,000 per graduate hired), (3) guaranteed interviews with partner companies.", "Three mechanisms: (1) direct hiring through the Klimaatkorps ensures immediate deployment, (2) Transition Accords create binding green hiring quotas for TenneT and SDE++ recipients, (3) farmer green co-ops create local jobs.")

# Q11 Category D
text = text.replace("employer tax credits don't burden consumers", "direct Klimaatkorps hiring doesn't burden consumers")

# Q12 Category D
text = text.replace("(1) regional focus—Groningen and farming provinces prioritized for skills funding, (2) worker protection—80% wage during training, (3) community benefits—local hiring for grid projects.", "(1) regional focus—Groningen and farming provinces prioritized for Klimaatkorps deployment, (2) job security—direct government employment and Transition Accords, (3) community benefits—farmer green co-ops.")

# NQ10
text = text.replace("Policy 1 (Grid Modernization)", "Policy 1 (DCOI Grid Operations)")

with open("06-qa-prep/qa-master-document.md", "w", encoding="utf-8") as f:
    f.write(text)

print("Done")
