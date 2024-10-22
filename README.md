# YouTube Transcript Generator

This tool allows you to fetch and display the transcript of a YouTube video in a user-friendly format. It uses the `youtube_transcript_api` library to retrieve the transcript and `streamlit` for the user interface.

## Features

- Extracts the video ID from a YouTube URL
- Fetches the transcript for the video
- Displays the transcript with or without timestamps

## Installation

### 1. Clone the repository:

- git clone https://github.com/MuhammadAhmed-0/youtube-transcript-generator.git
- cd youtube-transcript-generator

### 2. Install the necessary libraries:
- pip install streamlit youtube-transcript-api

### 3. Run the application:
- streamlit run youtube-transcript-generator.py
OR
- python -m streamlit run youtube-transcript-generator.py

## How It Works:
- The user inputs the YouTube URL and clicks the "Fetch Transcript" button.
- The app fetches the transcript. If it is successful, the transcript is displayed.
- Based on the user's choice (using the checkbox), either the transcript with timestamps or just the plain text is displayed.

