import PIL
from moviepy.editor import *
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC
import os
from PIL import Image
import io

# Monkey patch PIL to add the deprecated ANTIALIAS attribute
if not hasattr(PIL.Image, 'ANTIALIAS'):
    PIL.Image.ANTIALIAS = PIL.Image.LANCZOS

INPUT_DIR = "./input"
OUTPUT_DIR = "./output"

def extract_cover_image(mp3_filepath):
    try:
        audio = MP3(mp3_filepath, ID3=ID3)
        for tag in audio.tags.values():
            if isinstance(tag, APIC):
                image = Image.open(io.BytesIO(tag.data))
                # Convert non-RGB images to RGB
                if image.mode in ['RGBA', 'P']:
                    image = image.convert('RGB')
                cover_image_path = os.path.join(INPUT_DIR, "cover.jpg")
                image.save(cover_image_path)
                return cover_image_path
    except Exception as e:
        print(f"Error extracting cover image: {e}")
    return None

def mp3_to_mp4(mp3_filename, start_time=None, end_time=None):
    try:
        mp3_filepath = os.path.join(INPUT_DIR, mp3_filename)
        cover_image_path = extract_cover_image(mp3_filepath)
        if not cover_image_path:
            raise FileNotFoundError("Cover image not found in MP3 file")

        output_filepath = os.path.join(
            OUTPUT_DIR,
            mp3_filename.replace(".mp3", ".mp4")
            .replace(".MP3", ".mp4")
            .replace(".Mp3", ".mp4")
            .replace(".mP3", ".mp4"),
        )

        # Check if the output file already exists
        if os.path.exists(output_filepath):
            return

        # Load the audio file
        audioclip = AudioFileClip(mp3_filepath)

        # If start and end times are specified, subclip the audio
        if start_time and end_time:
            audioclip = audioclip.subclip(start_time, end_time)

        # Load the extracted cover image
        imgclip = ImageClip(cover_image_path)

        # Set the duration of the image to the duration of the audio
        imgclip = imgclip.set_duration(audioclip.duration)

        # Set the audio of the image clip to our audio
        videoclip = imgclip.set_audio(audioclip)

        # Set fps and resize video to 720x720 square resolution
        videoclip.fps = 30
        videoclip = videoclip.resize((720, 720))

        # Ensure output directory exists
        os.makedirs(OUTPUT_DIR, exist_ok=True)

        # Export the video clip as an MP4 file
        videoclip.write_videofile(output_filepath, codec="libx264", fps=30)
        print(f"Successfully created video: {output_filepath}")

    except Exception as e:
        print(f"Error occurred while processing {mp3_filename}: {e}")

def mp3_to_mp4_folder():
    try:
        # List all files in the INPUT_DIR
        all_files = os.listdir(INPUT_DIR)

        # Filter out only the MP3 files
        mp3_files = [f for f in all_files if f.lower().endswith(".mp3")]

        if not mp3_files:
            print("No MP3 files found in the input directory.")
            return

        # Convert each MP3 file to MP4
        for mp3_file in mp3_files:
            mp3_to_mp4(mp3_file)

    except Exception as e:
        print(f"Error occurred while processing the folder: {e}")

def main():
    mp3_to_mp4_folder()
    input("Press Enter to exit...")  # Keeps the console window open

if __name__ == '__main__':
    main()
