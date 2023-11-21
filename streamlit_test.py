import streamlit as st
import pandas as pd

# Sample data: list of dictionaries
list_of_dicts = [
    {"Name": "Alice", "Age": 25, "Country": "USA"},
    {"Name": "Bob", "Age": 30, "Country": "Canada"},
    {"Name": "Charlie", "Age": 28, "Country": "UK"}
]

# Sample data: Pandas DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 28],
    "Country": ["USA", "Canada", "UK"]
}
df = pd.DataFrame(data)

def display_data(data_to_display):
    if isinstance(data_to_display, list):
        st.write("Displaying List of Dictionaries:")
        st.write(pd.DataFrame(data_to_display))
    elif isinstance(data_to_display, pd.DataFrame):
        st.write("Displaying Pandas DataFrame:")
        st.write(data_to_display)

# Streamlit app
def main():
    st.title("Display Data")
    data_option = st.radio("Select data to display:", ("List of Dicts", "Pandas DataFrame"))

    if data_option == "List of Dicts":
        display_data(list_of_dicts)
    elif data_option == "Pandas DataFrame":
        display_data(df)

if __name__ == "__main__":
    main()
