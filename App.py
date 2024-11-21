import streamlit as st

# Utility functions
def calculate_total(items):
    """Calculate the total price of items in the cart."""
    return sum(item['price'] for item in items)

def add_to_cart(cart, item_name, price, customizations=None):
    """Add an item to the cart."""
    cart.append({"name": item_name, "price": price, "customizations": customizations or []})

def display_cart(cart):
    """Display cart details and calculate total."""
    if cart:
        st.subheader("Your Cart")
        for i, item in enumerate(cart):
            st.write(f"**{item['name']}** - ${item['price']:.2f}")
            if item["customizations"]:
                st.write(f"  - Customizations: {', '.join(item['customizations'])}")
        total = calculate_total(cart)
        st.markdown(f"### Total: ${total:.2f}")
        if st.button("Checkout"):
            st.success("Thank you for your order! We'll prepare it shortly.")
            cart.clear()
    else:
        st.info("Your cart is empty. Add some items to start your order!")

# Initialize session state for cart and loyalty points
if "cart" not in st.session_state:
    st.session_state.cart = []
if "loyalty_points" not in st.session_state:
    st.session_state.loyalty_points = 0

# Sidebar navigation
st.sidebar.title("Mobile Food Truck")
menu = st.sidebar.radio("Navigate to:", ["Home", "Philly Cheesesteaks", "Water Ice", "Coffee", "Feedback"])

# --- Home Page ---
if menu == "Home":
    st.title("🚚 Welcome to Our Mobile Food Truck!")
    st.image("https://example.com/food_truck.jpg", use_column_width=True)
    st.markdown(
        """
        **Menu Highlights**:
        - 🥩 Delicious **Philly Cheesesteaks**
        - 🍧 Refreshing **Water Ice**
        - ☕ Gourmet **Coffee**

        🌟 **Loyalty Program**: Earn points on every order and redeem them for discounts!
        """
    )
    st.markdown("---")
    st.subheader("How It Works")
    st.markdown(
        """
        1. Explore our menu and customize your order.
        2. Add items to your cart and view the total in real-time.
        3. Checkout and earn loyalty points for every dollar spent!
        """
    )
    st.sidebar.markdown("💳 **Loyalty Points:** Earned so far: **{:.2f}**".format(st.session_state.loyalty_points))

# --- Philly Cheesesteaks Page ---
elif menu == "Philly Cheesesteaks":
    st.title("🥩 Philly Cheesesteaks")
    st.image("https://example.com/philly_cheesesteak.jpg", use_column_width=True)
    st.subheader("Customize Your Cheesesteak")

    # Cheesesteak options and addons
    cheesesteak_options = {
        "Classic Philly": 10.99,
        "Chicken Philly": 11.99,
        "Veggie Philly": 9.99,
    }
    cheesesteak_addons = {
        "Extra Cheese": 1.50,
        "Mushrooms": 1.00,
        "Peppers": 1.00,
        "Onions": 0.75,
    }

    selected_cheesesteak = st.selectbox("Choose your cheesesteak:", cheesesteak_options.keys())
    selected_addons = st.multiselect("Add extras:", cheesesteak_addons.keys())

    # Calculate price
    cheesesteak_base_price = cheesesteak_options[selected_cheesesteak]
    cheesesteak_addon_price = sum(cheesesteak_addons[addon] for addon in selected_addons)
    cheesesteak_total = cheesesteak_base_price + cheesesteak_addon_price

    st.markdown(f"### Total: ${cheesesteak_total:.2f}")
    if st.button("Add to Cart"):
        add_to_cart(
            st.session_state.cart,
            selected_cheesesteak,
            cheesesteak_total,
            customizations=selected_addons,
        )
        st.success(f"{selected_cheesesteak} added to cart!")

# --- Water Ice Page ---
elif menu == "Water Ice":
    st.title("🍧 Water Ice")
    st.image("https://example.com/water_ice.jpg", use_column_width=True)
    st.subheader("Pick Your Favorite Flavor")

    # Water ice options and sizes
    water_ice_flavors = {
        "Cherry": 3.50,
        "Blue Raspberry": 3.50,
        "Mango": 4.00,
        "Lemon": 3.50,
    }
    water_ice_sizes = {"Small": 0, "Medium": 1.00, "Large": 2.00}

    selected_flavor = st.selectbox("Choose a flavor:", water_ice_flavors.keys())
    selected_size = st.radio("Choose a size:", water_ice_sizes.keys())

    # Calculate price
    flavor_price = water_ice_flavors[selected_flavor]
    size_price = water_ice_sizes[selected_size]
    total_price = flavor_price + size_price

    st.markdown(f"### Total: ${total_price:.2f}")
    if st.button("Add to Cart"):
        add_to_cart(
            st.session_state.cart,
            f"{selected_size} {selected_flavor} Water Ice",
            total_price,
        )
        st.success(f"{selected_size} {selected_flavor} Water Ice added to cart!")

# --- Coffee Page ---
elif menu == "Coffee":
    st.title("☕ Coffee")
    st.image("https://example.com/coffee.jpg", use_column_width=True)
    st.subheader("Craft Your Perfect Cup")

    # Coffee options and add-ons
    coffee_options = {
        "Espresso": 3.00,
        "Latte": 4.00,
        "Cappuccino": 4.50,
        "Cold Brew": 3.75,
    }
    coffee_addons = {
        "Extra Shot": 1.00,
        "Almond Milk": 0.50,
        "Caramel Syrup": 0.75,
        "Whipped Cream": 0.50,
    }

    selected_coffee = st.selectbox("Choose your coffee:", coffee_options.keys())
    selected_customizations = st.multiselect("Customize your coffee:", coffee_addons.keys())

    # Calculate price
    coffee_base_price = coffee_options[selected_coffee]
    coffee_customization_price = sum(coffee_addons[addon] for addon in selected_customizations)
    coffee_total = coffee_base_price + coffee_customization_price

    st.markdown(f"### Total: ${coffee_total:.2f}")
    if st.button("Add to Cart"):
        add_to_cart(
            st.session_state.cart,
            selected_coffee,
            coffee_total,
            customizations=selected_customizations,
        )
        st.success(f"{selected_coffee} added to cart!")

# --- Feedback Page ---
elif menu == "Feedback":
    st.title("📋 Customer Feedback")
    st.subheader("We Value Your Feedback!")
    name = st.text_input("Your Name:")
    feedback = st.text_area("Share your experience with us:")
    if st.button("Submit Feedback"):
        st.success("Thank you for your feedback!")
        st.balloons()

# --- Display Cart ---
display_cart(st.session_state.cart)

# --- Loyalty Points ---
if st.session_state.cart:
    st.session_state.loyalty_points += calculate_total(st.session_state.cart)
