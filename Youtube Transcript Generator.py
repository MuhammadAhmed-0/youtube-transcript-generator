import streamlit as st
import re
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound

# Extract video ID from the YouTube URL
def get_video_id(url):
    """
    Extracts the video ID from the given YouTube URL.
    """
    regex = r'(?:https?://)?(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})'
    match = re.search(regex, url)
    if match:
        return match.group(1)
    else:
        st.error("Invalid YouTube URL. Please try again.")
        return None

# Fetch transcript using the video ID
def fetch_transcript(video_id):
    """
    Fetches the transcript for a given YouTube video ID.
    Handles cases where no transcript is available.
    """
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
        return transcript
    except TranscriptsDisabled:
        st.error("Transcripts are disabled for this video.")
    except NoTranscriptFound:
        st.error("No transcript found for this video.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
    return None

# Remove timestamps from the transcript
def remove_timestamps(transcript):
    """
    Removes timestamps from the transcript and returns plain text.
    """
    plain_text = "\n".join([entry['text'] for entry in transcript])
    return plain_text

# Display the transcript in the UI
def display_transcript(transcript, with_timestamps=True):
    """
    Displays the fetched transcript in a user-friendly format.
    If with_timestamps is False, it shows only plain text without timestamps.
    """
    if transcript:
        if with_timestamps:
            st.subheader("Transcript with Timestamps:")
            for entry in transcript:
                start_time = entry['start']
                end_time = entry['start'] + entry['duration']
                text = entry['text']
                st.write(f"{start_time:.2f} - {end_time:.2f}: {text}")
        else:
            st.subheader("Transcript (Plain Text):")
            plain_text = remove_timestamps(transcript)
            st.write(plain_text)
    else:
        st.info("No transcript available for this video.")

# Main function to handle the Streamlit UI
def main():
    st.title("YouTube Transcript Fetcher")

    # Input field for YouTube URL
    url = st.text_input("Enter the YouTube video URL:", "")

    # Checkbox to allow user to choose whether they want timestamps
    with_timestamps = st.checkbox("Display with timestamps", value=True)

    # Button to fetch transcript
    if st.button("Fetch Transcript"):
        video_id = get_video_id(url)
        if video_id:
            transcript = fetch_transcript(video_id)
            display_transcript(transcript, with_timestamps)

# Run the main function
if __name__ == "__main__":
    main()
