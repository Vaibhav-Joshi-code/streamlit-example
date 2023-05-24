import streamlit as st

from pytube import YouTube

st.write('Welcome to YouTube video downloader!!')
def main():
    path = st.text_input('Enter URL of the video: ')
    options = st.selectbox("Select the type of download",
                           ('audio only','high resolution'))
    
    
    if st.button('download'):
        video_object = YouTube(path)
        st.write('Video title: ',str(video_object.title))
        if options == 'audio only':
            video_object.streams.get_audio_only().download()
        elif options == 'high resolution':
            video_object.streams.get_highest_resolution().download()
    if st.button("view"):
        st.video(path)
    st.write('Created by: Vaibhav Joshi')

if __name__ == '__main__':
    main()








