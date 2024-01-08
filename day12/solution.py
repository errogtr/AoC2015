import json
import re

with open("data") as f:
    raw_json = f.read()

# ==== PART 1 ====
print(sum(map(int, re.findall(r"-*\d+", raw_json))))

parsed_json = json.loads(raw_json)
