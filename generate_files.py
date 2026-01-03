import re
import os
import json
import xml.etree.ElementTree as ET

from core import WordList

# Downloading open russian corpus
if not os.path.exists("annot.opcorpora.no_ambig_strict.xml"):
    os.system("wget https://opencorpora.org/files/export/annot/annot.opcorpora.no_ambig_strict.xml.zip && unzip *.zip && rm annot.opcorpora.no_ambig_strict.xml.zip")
tree = ET.parse("annot.opcorpora.no_ambig_strict.xml")
root = tree.getroot()

nouns = []

# Generating wordlist
for token in root.findall(".//token"):
    token_text = token.get("text", "")
    has_noun = False
    for g in token.findall(".//g"):
        if g.get("v") == "NOUN":
            has_noun = True
            break
    if has_noun and token_text:
        cleaned_text = re.sub(r'^[^\w]*|[^\w]*$', '', token_text)
        if len(cleaned_text)>=3:
            nouns.append(cleaned_text.lower())
print(f"Generated wordlist of {len(nouns)} nouns")

with open("words.txt", "w", encoding="utf-8") as f:
    for noun in nouns:
        f.write(noun + "\n")

# Generating mappings
w = WordList("words.txt")

for i in range(1, 4):
    combs = w.find_by_depth(i)
    if len(combs) < 255:
        del combs
    else:
        break

if not combs:
    exit("Failed to generate mappings based on words.txt - enchance your dictionary!")

mappings = {i : combs[i] for i in range(256)}

with open("mappings.json", "w", encoding="utf-8") as f:
    json.dump(mappings, f, indent=4)
print("Generated mappings, based on words.txt")
