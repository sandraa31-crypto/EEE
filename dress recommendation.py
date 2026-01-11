import tkinter as tk
from tkinter import ttk, messagebox

# ------------------ Recommendation Logic ------------------
def get_recommendation():
    gender = gender_var.get()
    occasion = occasion_var.get()
    weather = weather_var.get()

    if gender == "" or occasion == "" or weather == "":
        messagebox.showwarning("Input Error", "Please select all fields!")
        return

    recommendations = {
        ("Female", "Casual", "Sunny"):
            "Floral Top + Jeans\nWhite Sneakers\nSunglasses",
        ("Female", "Casual", "Rainy"):
            "T-shirt + Dark Jeans\nFlat Sandals\nLight Jacket",
        ("Female", "Formal", "Sunny"):
            "Cotton Saree / Kurti\nComfortable Flats",
        ("Male", "Casual", "Sunny"):
            "Cotton Shirt + Jeans\nSneakers",
        ("Male", "Formal", "Rainy"):
            "Formal Shirt + Trousers\nLeather Shoes\nUmbrella",
    }

    result = recommendations.get(
        (gender, occasion, weather),
        "Simple Outfit\nNeutral Colors\nComfortable Footwear"
    )

    result_label.config(text="👗 Recommended Outfit:\n\n" + result)

# ------------------ Reset Function ------------------
def reset_fields():
    gender_var.set("")
    occasion_var.set("")
    weather_var.set("")
    result_label.config(text="")

# ------------------ Background Change ------------------
def change_bg(color):
    root.configure(bg=color)
    main_frame.configure(bg=color)


def change_background(image_path):
    if os.path.exists(image_path):
        try:
            bg_image = Image.open(image_path)
            bg_image = bg_image.resize((500, 450))
            bg_photo = ImageTk.PhotoImage(bg_image)
            background_label.config(image=bg_photo)
            background_label.image = bg_photo
        except Exception as e:
            print("Error loading background:", e)
    else:
        print(f"Background image not found: {image_path}")


# -------------------- Main Window --------------------
root = tk.Tk()
root.title("AI Dress Recommendation App")
root.geometry("450x520")
root.configure(bg="#f2f6f9")
# Default background
# ------------------ UI Layout ------------------
main_frame = tk.Frame(root, bg="#f2f6f9")
main_frame.pack(pady=20)

title = tk.Label(
    main_frame,
    text="👕 AI-Based Dress Recommendation",
    font=("Segoe UI", 16, "bold"),
    bg="#2f80ed",
    fg="white",
    width=35,
    pady=10
)
title.pack(pady=10)

# ------------------ Input Fields ------------------
gender_var = tk.StringVar()
occasion_var = tk.StringVar()
weather_var = tk.StringVar()

def create_dropdown(label, variable, options):
    tk.Label(main_frame, text=label, bg="#f2f6f9", font=("Segoe UI", 11)).pack(pady=5)
    ttk.Combobox(
        main_frame,
        textvariable=variable,
        values=options,
        state="readonly",
        width=25
    ).pack()

create_dropdown("Select Gender:", gender_var, ["Male", "Female"])
create_dropdown("Select Occasion:", occasion_var, ["Casual", "Formal", "Party"])
create_dropdown("Select Weather:", weather_var, ["Sunny", "Rainy", "Winter"])

# ------------------ Buttons ------------------
tk.Button(
    main_frame,
    text="Get Suggestions",
    bg="#27ae60",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    width=20,
    command=get_recommendation
).pack(pady=15)

tk.Button(
    main_frame,
    text="Reset",
    bg="#e74c3c",
    fg="white",
    width=15,
    command=reset_fields
).pack()

# ------------------ Output ------------------
result_label = tk.Label(
    main_frame,
    text="",
    bg="#ecf0f1",
    fg="#2c3e50",
    font=("Segoe UI", 11),
    width=35,
    height=6,
    relief="ridge"
)
result_label.pack(pady=15)

# ------------------ Background Options ------------------
tk.Label(main_frame, text="Change Background:", bg="#f2f6f9").pack(pady=5)

bg_frame = tk.Frame(main_frame, bg="#f2f6f9")
bg_frame.pack()

tk.Button(bg_frame, text="Light", command=lambda: change_bg("#f2f6f9")).grid(row=0, column=0, padx=5)
tk.Button(bg_frame, text="Blue", command=lambda: change_bg("#d6eaf8")).grid(row=0, column=1, padx=5)
tk.Button(bg_frame, text="Green", command=lambda: change_bg("#d5f5e3")).grid(row=0, column=2, padx=5)

root.mainloop()