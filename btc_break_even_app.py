
import streamlit as st
import pandas as pd

st.set_page_config(page_title="BTC Break-even Calculator", layout="centered")

st.title("📊 BTC Break-even Calculator")

st.markdown("""
This tool calculates the **break-even BTC price** based on your initial loss, commissions, offset buys, and open positions.
""")

# Input fields
initial_loss = st.number_input("Initial Loss ($)", min_value=0.0, value=200.0, step=10.0)
commission = st.number_input("Commission ($)", min_value=0.0, value=24.0, step=1.0)
offset_buys = st.number_input("Number of Offset Buys", min_value=1, value=4, step=1)
offset_price = st.number_input("Price per Offset Buy ($)", min_value=0.0, value=300.0, step=10.0)
new_buy_price = st.number_input("Price of New Buy ($)", min_value=0.0, value=250.0, step=10.0)
open_positions = st.number_input("# of Open Positions (N)", min_value=1, value=1, step=1)

# Calculation
numerator = initial_loss + commission + (offset_buys * offset_price) + (open_positions * new_buy_price)
denominator = offset_buys + open_positions

if denominator > 0:
    break_even_price = numerator / denominator
else:
    break_even_price = 0

# Display result
st.subheader("📈 Break-even BTC Price")
st.success(f"Break-even price: ${break_even_price:,.2f}")

# Optional table view
if st.checkbox("Show calculation breakdown"):
    breakdown = pd.DataFrame({
        'Component': ['Initial Loss', 'Commission', 'Offset Buys Total', 'New Buy Total', 'Total Units'],
        'Value ($)': [initial_loss, commission, offset_buys * offset_price, open_positions * new_buy_price, denominator]
    })
    st.table(breakdown)
