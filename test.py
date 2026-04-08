import streamlit as st

# --- 1. LAYOUT & TEXT ELEMENTS ---
# This sets up the webpage tab title
st.set_page_config(page_title="Petcare Dosth", page_icon="🐾", layout="wide")

st.title("🐾 Petcare Dosth")
st.subheader("Emergency Vet & Pet Taxi Dispatch")
st.markdown("---") # Adds a visual divider line

# --- 2. LAYOUT CONTROL (Sidebar) ---
# We put the input form in a sidebar to keep the main screen clean
st.sidebar.header("📋 Booking Details")

# --- 3. INPUT WIDGETS ---
# Radio button for main service selection
service_type = st.sidebar.radio("What do you need?", ["Emergency Vet", "Pet Taxi"])

# Dropdown for Pet Type
pet_type = st.sidebar.selectbox("Who is the patient/passenger?", ["Dog", "Cat", "Other"])

# Dynamic Widget: Only show breed sizes if it's a dog!
if pet_type == "Dog":
    breed = st.sidebar.selectbox("Dog Size/Type:", ["Small (e.g., Pug)", "Medium (e.g., Indie)", "Large (e.g., Lab)", "Giant"])
elif pet_type == "Cat":
    breed = st.sidebar.selectbox("Cat Type:", ["Persian", "Indie", "Other"])
else:
    breed = "Other"

# Location input (Using Chennai areas for your testing!)
location = st.sidebar.selectbox("Pickup/Clinic Location:", ["Thoraipakkam", "Adyar", "Oragadam", "Anna Nagar"])

# Checkbox for extra requirements (Only shows if they want a taxi)
extra_handler = False
if service_type == "Pet Taxi":
    extra_handler = st.sidebar.checkbox("Do you need an extra handler to ride with the pet?")

# --- 4. ACTION BUTTON & DATA DISPLAY ---
st.write(f"### Available {service_type}s near {location}")

# The button triggers the search
if st.sidebar.button("Search Available Services 🚀"):
    
    # We use 'info', 'success', and 'warning' boxes for beautiful UI feedback
    st.info("Scanning network for available partners...")
    
    # --- MOCK RESULTS (Later, this will connect to your Flask API!) ---
    if service_type == "Emergency Vet":
        st.success("**Dr. Rao's 24/7 Animal Hospital** is accepting emergencies.")
        st.write("📍 Distance: 2.5 km away")
        st.button("🏥 Confirm Vet Appointment") # A button to finalize
        
    elif service_type == "Pet Taxi":
        st.success("**Paws & Wheels Pet Transport** is 15 minutes away.")
        if extra_handler:
            st.write("✅ *Driver is bringing an experienced pet handler.*")
        st.write(f"🚙 Vehicle sized for: {breed} {pet_type}")
        st.write("💰 Estimated Fare: ₹450")
        st.button("🚕 Dispatch Taxi Now")
else:
    st.write("👈 Fill out the details in the sidebar and click Search!")
    


