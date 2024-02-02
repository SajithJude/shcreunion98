import streamlit as st
import json
# import youtube_dl


category_to_emoji = {
    # "Exasperation or Frustration": "😤",
    # "Sarcasm or Mocking": "😜",
    # "Bewilderment or Surprise": "😲",
    # "Dismissive or Indifferent": "🙄",
    # "Humorous or Light-hearted": "😂",
    # "Philosophical or Reflective": "🤔",
    # "Criticism or Warning": "⚠️",
    # "Joy or Satisfaction": "😊",
    # "Friendship and Companionship": "👫",
    # "Surprise or Disbelief": "😱",
    # "Defiance or Challenge": "😡",
    # "Mysticism or Superstition": "🤔",
    "Light-hearted Teasing or Self-deprecation": "😂",
"Friendship and Companionship": "👫",
"Frustration or Resignation": "😤",
"Mysticism or Superstition": "🤔",
"Surprise or Disbelief": "😱",
"Sarcasm or Mocking": "😜",
"Defiance or Challenge": "😡",
"Encouragement or Support": "😊",
"Exasperation or Frustration": "😤",
"Joy or Satisfaction": "😊"
}
# Function to extract audio from YouTube URL dialogue JSON data
# Assuming the JSON file is stored in the same directory as the app
def load_data(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data

# Display categories and dialogues
def display_categories(data):
    selected_category =  list(data.keys())
    if selected_category:
        dialogues = data[selected_category]
        for dialogue in dialogues:
            if st.button(dialogue['dialog']):
                # audio_url = extract_audio(dialogue['url'])
                st.video(dialogue['url'])

# Main app function
def main():
    st.title("SHC 98 reunion background music app")
    st.caption("situation க்கு ஏத்த stickerah அமத்தினால் நீயும் dj-black தான்...")

    # Assuming the JSON file is named 'dialogues.json' and located in the same directory
    file_name = "dialogues.json"  # Change this to your actual file path
    data = load_data(file_name)
    
    # display_categories(data)
    # Display emojis for categories
    # col1, col2, col3, col4 , col5, col6, col7, col8, col9, col10 = st.columns(10)
    # columns = [col1, col2, col3, col4, col5, col6, col7, col8, col9, col10]
    # col1, col2 = st.columns(2)
    # columns = [col1] * 5 + [col2] * (len(category_to_emoji) - 5)  # First 5 in col1, rest in col2

        # Split the categories into two rows
    categories_list = list(category_to_emoji.items())
    first_row_categories = categories_list[:5]
    second_row_categories = categories_list[5:]

    # Creating first row
    row1 = st.columns(5)
    for i, (category, emoji) in enumerate(first_row_categories):
        tile = row1[i].container()
        if tile.button(emoji, key=f"row1_{category}"):
            st.session_state['selected_category'] = category
            # st.write(f"You selected: {category}")

    # Creating second row
    row2 = st.columns(5)
    for i, (category, emoji) in enumerate(second_row_categories):
        tile = row2[i].container()
        if tile.button(emoji, key=f"row2_{category}"):
            st.session_state['selected_category'] = category
            # st.write(f"You selected: {category}")

    # If a category is selected, display its dialogues
    if 'selected_category' in st.session_state:
        # st.write(f"Category: {st.session_state['selected_category']}")
        for dialogue in data.get(st.session_state['selected_category'], []):
            buton = st.expander(dialogue['dialog'])
            with buton:
                # Here you would play the audio from the dialogue's URL
                st.video(dialogue['url'],format="audio/mp3")  # Placeholder for audio playing functionality
                


if __name__ == "__main__":
    main()
