import json
import streamlit as st

st.set_page_config(page_title="AI Recipe Preparation Agent", layout="wide")

st.title("🍳 Agentic AI Recipe Preparation Assistant")
st.caption("Powered by IBM Granite & RAG Architecture | IBM SkillsBuild Internship Project")

@st.cache_data
def load_recipes():
    with open("recipe_data.json") as f:
        return json.load(f)

recipes = load_recipes()

user_input = st.text_input("Enter ingredients on hand (e.g., tomatoes, garlic, pasta):")

if st.button("Generate Recipe"):
    if user_input:
        input_list = [i.strip().lower() for i in user_input.split(",")]
        matched = []
        for r in recipes:
            if any(ing in input_list for ing in r["ingredients"]):
                matched.append(r)
        
        if matched:
            for item in matched:
                st.subheader(f"📖 {item['title']}")
                st.write("**Ingredients:**", ", ".join(item['ingredients']))
                st.write("**Instructions:**", item['instructions'])
                st.info(f"**Substitutions:** {item['substitutions']}")
                st.success(f"**Cooking Tips:** {item['tips']}")
        else:
            st.warning("No direct match found. Try entering common staples like tomatoes, garlic, or pasta.")
    else:
        st.error("Please enter at least one ingredient.")