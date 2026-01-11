import streamlit as st

# App Configuration
st.set_page_config(page_title="Sustainable Fabric Selector", layout="centered")
st.title("🌿 Sustainable Fabric Recommendation App")

st.write("Get the most suitable **eco-friendly fabric** based on your needs.")

# User Inputs
climate = st.selectbox("Select Climate", ["Hot", "Cold", "Moderate"])
preference = st.selectbox("Fashion Preference", ["Casual", "Formal", "Sportswear", "Traditional"])
budget = st.slider("Budget (₹)", 500, 5000, step=500)
durability = st.selectbox("Durability Required", ["Medium", "High", "Very High"])

# Fabric Recommendation Logic
def recommend_fabric(climate, preference, budget, durability):
    # Budget-based primary filter
    if budget < 1500:
        budget_tier = "budget"
    elif budget < 3000:
        budget_tier = "mid"
    else:
        budget_tier = "premium"
    
    # Climate-based recommendations with budget consideration
    if climate == "Hot":
        if durability == "Very High":
            return "Hemp Fabric" if budget_tier == "premium" else "Organic Cotton"
        else:
            return "Organic Cotton"

    elif climate == "Cold":
        if budget_tier == "premium":
            return "Recycled Wool"
        else:
            return "Hemp Blend"

    elif climate == "Moderate":
        if preference == "Formal":
            return "Tencel (Lyocell)"
        elif budget_tier == "budget":
            return "Upcycled Cotton"
        else:
            return "Linen"

    return "Recycled Polyester"


# Button Action
if st.button("Get Fabric Recommendation"):
    fabric = recommend_fabric(climate, preference, budget, durability)
    st.subheader("✅ Recommended Sustainable Fabric")
    st.success(fabric)

# Footer
st.markdown("---")
st.caption("Circular Fashion Hackathon | Sustainable Textile Selection")


