import json

with open("json_output/sneheil_response_uniform.json", "r") as f:
    data = json.load(f)
print(type(data))
with open("sneheil_uni.json","w") as f:
    json.dump(data,f,indent = 2)

print(len(data))