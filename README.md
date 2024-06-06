# YouTube Video Downloader

This Python script hooks you up with downloading YouTube videos, complete with a range of customization options.

---

## Getting Started

1. **Clone the repository:**
    ```bash
    git clone https://github.com/nopoh28102/yt-dlp.git
    ```

2. **Navigate to the downloaded directory:**
    ```bash
    cd yt-dlp
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

---

## Usage

1. **Run the script:**
    ```bash
    python youtube_downloader.py
    ```

2. **Follow the prompts to enter the YouTube video links and customize your download options.**

3. **Enjoy downloading your favorite YouTube videos!**

---

## Features

- Download videos in the best quality available.
- Customize output path, video quality, resolution, and more.
- Download audio only or extract subtitles.
- Progress bar shows the download progress.

---

## Quick Access Menu

The script provides a quick access menu with the following options:

1. Select Quality
2. Select Output Path
3. Select Audio Only Download
4. Select Resolution
5. Select Compressed Video Download
6. Select Subtitles Download
7. Select Start and End
8. Select Encoding
9. Ignore Certificate Check
10. Select Proxy Settings
11. Start Download
12. Exit

---

## Dependencies

- `yt_dlp`: For downloading videos from YouTube.
- `requests`: For checking internet connection.
- `termcolor`: For colored text output.
- `colorama`: For colored text output on Windows.

---

## Author

[mahmoud nabih](https://github.com/nopoh28102)

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## YouTube Downloader Code

```python
# -*- coding: utf-8 -*-
from yt_dlp import YoutubeDL
import os
import sys
import requests
from termcolor import colored
from colorama import init

# YouTube Downloader code goes here...
