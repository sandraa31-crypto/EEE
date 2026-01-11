import pandas as pd

data = {
    "Material": ["Organic Cotton", "Hemp", "Bamboo", "Recycled Polyester"],
    "Carbon": [2.1, 1.5, 2.8, 3.0],
    "Water": [2500, 1800, 3000, 1200],
    "Biodegradable": [1, 1, 1, 0],
    "Durability": [3, 3, 2, 3],
    "Recyclable": [1, 1, 1, 1]
}

df = pd.DataFrame(data)

def sustainability_score(row):
    score = 100
    score -= row["Carbon"] * 10
    score -= row["Water"] / 100
    score += row["Biodegradable"] * 15
    score += row["Durability"] * 5
    score += row["Recyclable"] * 10
    return round(score, 2)

df["SustainabilityScore"] = df.apply(sustainability_score, axis=1)

best_material = df.sort_values(by="SustainabilityScore", ascending=False).iloc[0]

print("Smart Sustainable Material Selector Result\n")
print("Recommended Material:", best_material["Material"])
print("Sustainability Score:", best_material["SustainabilityScore"])
print("\nMaterial Analysis:")
print(df[["Material", "SustainabilityScore"]])
