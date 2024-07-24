from pytube import YouTube
from moviepy.editor import VideoFileClip

def download_youtube_video(url, output_path='video.mp4'):
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=False, file_extension='mp4').first()
    stream.download(filename=output_path)
    return output_path

def extract_audio_from_video(video_path, output_audio_path='audio.mp3'):
    video_clip = VideoFileClip(video_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(output_audio_path)
    audio_clip.close()
    video_clip.close()
    return output_audio_path

if __name__ == "__main__":
    video_url = 'https://www.youtube.com/watch?v=eIf3-aDTOOA&t=2633s'
    video_path = download_youtube_video(video_url)
    audio_path = extract_audio_from_video(video_path)
    print(f"Audio extracted and saved to {audio_path}")
