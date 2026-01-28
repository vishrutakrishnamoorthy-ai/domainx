import streamlit as st
import pandas as pd
from datetime import date


st.set_page_config(
    page_title="Shopping List App",
    page_icon="🛒",
    layout="centered"
)

st.title("🛒 Shopping List")


st.subheader("👤 User Details")

user_name = st.text_input("Enter your name")
shopping_date = st.date_input("Select date", value=date.today())

st.divider()


if "shopping_list" not in st.session_state:
    st.session_state.shopping_list = []


st.subheader("➕ Add Item")

item_name = st.text_input("Item Name")
quantity = st.number_input("Quantity", min_value=1, step=1)

col1, col2 = st.columns(2)

with col1:
    add_btn = st.button("Add Item")

with col2:
    clear_btn = st.button("Clear List")


if add_btn:
    if item_name.strip() == "":
        st.warning("⚠️ Please enter an item name")
    else:
        st.session_state.shopping_list.append({
            "S.No": len(st.session_state.shopping_list) + 1,
            "Item Name": item_name,
            "Quantity": quantity
        })
        st.success("✅ Item added")

if clear_btn:
    st.session_state.shopping_list = []
    st.info("🗑️ Shopping list cleared")


if st.session_state.shopping_list:
    st.subheader("📋 Shopping List")

    df = pd.DataFrame(st.session_state.shopping_list)

    st.dataframe(df, use_container_width=True)

    total_items = df["Quantity"].sum()

    st.markdown(f"""
    ### 📦 Summary
    - **User Name:** {user_name if user_name else "Not entered"}
    - **Date:** {shopping_date}
    - **Total Items:** **{total_items}**
    """)

else:
    st.info("📝 No items added yet")
