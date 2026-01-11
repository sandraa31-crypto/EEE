import tkinter as tk
import pandas as pd

data = {
    "Material": ["Organic Cotton", "Hemp", "Bamboo", "Recycled Polyester", "Linen", "Tencel"],
    "Carbon": [2.1, 1.5, 2.8, 3.0, 1.8, 2.0],
    "Water": [2500, 1800, 3000, 1200, 2000, 1500],
    "Biodegradable": [1, 1, 1, 0, 1, 1],
    "Durability": [3, 3, 2, 3, 3, 2],
    "Recyclable": [1, 1, 1, 1, 1, 1],
    "Cost": [3, 2, 2, 1, 3, 2]
}

df = pd.DataFrame(data)

def efficiency(row):
    score = 100
    score -= row["Carbon"] * 10
    score -= row["Water"] / 100
    score += row["Biodegradable"] * 15
    score += row["Durability"] * 5
    score += row["Recyclable"] * 10
    score -= row["Cost"] * 5
    return round(score, 2)

df["Efficiency"] = df.apply(efficiency, axis=1)
df = df.sort_values(by="Efficiency", ascending=False)

best = df.iloc[0]

root = tk.Tk()
root.title("Smart Sustainable Material Selector")
root.geometry("600x500")
text = tk.Text(root, font=("Arial", 12))
text.pack(expand=True, fill="both")

text.insert("end", "SMART SUSTAINABLE MATERIAL SELECTOR\n\n")
text.insert("end", "Best Recommended Material\n\n")
text.insert("end", "Material: " + best["Material"] + "\n")
text.insert("end", "Cost Level: " + str(best["Cost"]) + "\n")
text.insert("end", "Efficiency Score: " + str(best["Efficiency"]) + "\n\n")
text.insert("end", "All Materials Comparison\n\n")

for _, row in df.iterrows():
    line = f'{row["Material"]} | Cost: {row["Cost"]} | Efficiency: {row["Efficiency"]}\n'
    text.insert("end", line)

text.config(state="disabled")
root.mainloop()

