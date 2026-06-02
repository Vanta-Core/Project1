import pandas as pd
info = {
    "Name": "Neel",
    "Age": 20,
    "Course": "Engineering"
}

df = pd.DataFrame([info])

print("Keys:")
for key in info.keys():
    print(key)

print("Values:")
for value in info.values():
    print(value)


