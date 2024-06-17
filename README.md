# MP3 to MP4 Converter

This script converts MP3 files with embedded cover images to MP4 videos. Each MP4 video will display the cover image for the duration of the audio.

## Features

- Extracts cover images from MP3 files.
- Converts MP3 files to MP4 videos with the extracted cover image.
- Automatically skips MP3 files that already have corresponding MP4 files in the output directory.
- Handles various image modes and converts them to a compatible format for video encoding.
- Allows optional audio clipping based on start and end times.

## Prerequisites

Ensure you have the following installed:

- Python 3.6 or higher
- pip (Python package installer)

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/conniebecool/mp3-to-mp4.git
    cd mp3-to-mp4
    ```

2. Install the required Python packages:

    ```bash
    pip install moviepy
    pip install mutagen
    pip install pillow
    ```

## Usage

1. Place your MP3 files in the `./input` directory.

2. Run the script:

    ```bash
    python main.py
    ```

3. Converted MP4 files will be saved in the `./output` directory.

### Script Details

#### extract_cover_image(mp3_filepath)

Extracts the cover image from the MP3 file.

- Converts images in 'RGBA' or 'P' mode to 'RGB' mode.
- Saves the cover image as `cover.jpg` in the input directory.
- Returns the path to the saved cover image.

#### mp3_to_mp4(mp3_filename, start_time=None, end_time=None)

Converts a single MP3 file to an MP4 file.

- Checks if the output file already exists and skips conversion if it does.
- Sets the duration of the image to match the audio duration.
- Resizes the video to 720x720 square resolution.
- Saves the output video in the `./output` directory.

#### mp3_to_mp4_folder()

Processes all MP3 files in the `./input` directory.

- Converts each MP3 file to MP4 using the `mp3_to_mp4` function.
- Prints errors if any occur during processing.

## Contributing

Feel free to open issues or submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](LICENSE)

## Contact

For any issues or questions, please contact [conniebecool](https://github.com/conniebecool).
