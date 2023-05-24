import streamlit as st
import os
from pytube import YouTube

st.write('Welcome to YouTube video downloader!!')

def main():
    path = st.text_input('Enter URL of the video: ')
    options = st.selectbox("Select the type of download",
                           ('audio only', 'high resolution'))
    
    if st.button('Download'):
        video_object = YouTube(path)
        st.write('Video title:', str(video_object.title))
        
        if options == 'audio only':
            stream = video_object.streams.get_audio_only()
        elif options == 'high resolution':
            stream = video_object.streams.get_highest_resolution()
        
        if stream:
            filename = stream.download()
            st.write('Download complete:', filename)
            st.success('Video downloaded successfully!')
        else:
            st.error('Failed to retrieve the selected stream.')
    
    if st.button("View"):
        if os.path.exists(filename):
            st.video(filename)
        else:
            st.error('Video file does not exist.')
    
    st.write('Created by: Vaibhav Joshi')

if __name__ == '__main__':
    main()
