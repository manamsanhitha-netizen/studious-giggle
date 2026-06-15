# pages/1_Support_Chatbot.py

import streamlit as st

st.set_page_config(
    page_title="Support Chatbot",
    page_icon="💬",
    layout="wide"
)

# ---------------------------------------------------
# PRODUCT KNOWLEDGE BASE
# ---------------------------------------------------
products = {
    "wireless headphones": {
        "price": "₹2999",
        "description": "Premium noise-cancelling Bluetooth headphones."
    },
    "smart watch": {
        "price": "₹4999",
        "description": "Fitness tracking and notifications on your wrist."
    },
    "gaming mouse": {
        "price": "₹1499",
        "description": "High precision RGB gaming mouse."
    },
    "laptop backpack": {
        "price": "₹1299",
        "description": "Water-resistant backpack."
    },
    "coffee mug": {
        "price": "₹399",
        "description": "Stylish ceramic mug."
    },
    "mechanical keyboard": {
        "price": "₹3499",
        "description": "Durable keyboard with tactile switches."
    }
}

# ---------------------------------------------------
# PAGE TITLE
# ---------------------------------------------------
st.title("💬 MiniStore Support Chatbot")

st.write("""
Ask me about:

• Products

• Delivery

• Refunds

• Returns

• Payment methods

• Order status
""")

# ---------------------------------------------------
# CHAT HISTORY
# ---------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! Welcome to MiniStore Support. How can I help you today?"
        }
    ]

# ---------------------------------------------------
# DISPLAY CHAT HISTORY
# ---------------------------------------------------
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------------------------------------------------
# RULE-BASED BOT
# ---------------------------------------------------
def chatbot_response(user_text):

    text = user_text.lower()

    # Product Questions
    for product_name, details in products.items():

        if product_name in text:

            return (
                f"📦 {product_name.title()}\n\n"
                f"Price: {details['price']}\n\n"
                f"{details['description']}"
            )

    # Delivery
    if any(word in text for word in
           ["delivery", "shipping", "ship"]):

        return (
            "🚚 Standard delivery takes "
            "3-5 business days."
        )

    # Refunds
    if "refund" in text:

        return (
            "💰 Refunds are processed "
            "within 5-7 business days."
        )

    # Returns
    if "return" in text:

        return (
            "↩️ Products can be returned "
            "within 30 days of purchase."
        )

    # Payment
    if any(word in text for word in
           ["payment", "pay", "upi", "card"]):

        return (
            "💳 We accept UPI, Credit Cards, "
            "Debit Cards and Net Banking."
        )

    # Order Status
    if any(word in text for word in
           ["order", "status", "tracking"]):

        return (
            "📦 Your order is currently "
            "being processed."
        )

    return (
        "I'm not sure about that. "
        "Please ask about products, "
        "delivery, returns, refunds, "
        "payments, or order status."
    )

# ---------------------------------------------------
# CHAT INPUT
# ---------------------------------------------------
prompt = st.chat_input(
    "Type your message..."
)

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    response = chatbot_response(prompt)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    with st.chat_message("assistant"):
        st.markdown(response)