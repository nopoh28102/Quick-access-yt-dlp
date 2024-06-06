# YT-DLP: Customizable YouTube Video Downloader

![YT-DLP](https://user-images.githubusercontent.com/18350557/176309783-0785949b-9127-417c-8b55-ab5a4333674e.gif)

[![YT-DLP](https://raw.githubusercontent.com/yt-dlp/yt-dlp/master/.github/banner.svg)](#readme)

This Python script hooks you up with downloading YouTube videos, complete with a range of customization options.

---

## Getting Started

1. **Clone the repository:**
    ```bash
    git clone https://github.com/nopoh28102/Quick-access-yt-dlp.git
    ```

2. **Navigate to the downloaded directory:**
    ```bash
    cd Quick-access-yt-dlp
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

---

## Usage
https://github.com/nopoh28102/Quick-access-yt-dlp/assets/150601942/ea69fb71-ab90-4e3b-83af-7a38ca4b0ad9

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
- Download multiple links.
- Download full playlist.

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

# [Mahmoud Nabih](https://github.com/nopoh28102)

<!-- display the social media buttons in your README -->

[![facebook](https://github.com/shikhar1020jais1/Git-Social/blob/master/Icons/Facebook.png (Facebook))][1]
[![instagram](https://github.com/shikhar1020jais1/Git-Social/blob/master/Icons/Instagram.png (Instagram))][2]
[![twitter](https://github.com/shikhar1020jais1/Git-Social/blob/master/Icons/Twitter.png (Twitter))][3]
[![linkedin](https://github.com/shikhar1020jais1/Git-Social/blob/master/Icons/LinkedIn.png (LinkedIn))][4]
[![github](https://github.com/shikhar1020jais1/Git-Social/blob/master/Icons/Github.png (Github))][5]
[![pinterest](https://github.com/shikhar1020jais1/Git-Social/blob/master/Icons/pinterest.png (Pinterest))][6]
[![tumblr](https://github.com/shikhar1020jais1/Git-Social/blob/master/Icons/tumblr.png (Tumblr))][7]

<!-- To Link your profile to the media buttons -->

[1]: https://www.facebook.com/username
[2]: https://www.instagram.com/username
[3]: https://www.twitter.com/username
[4]: https://www.linkedin.com/in/username
[5]: https://www.github.com/nopoh28102
[6]: https://in.pinterest.com/username
[7]: https://username.tumblr.com


<div align="center">
  <a href="https://www.instagram.com/m.nopoh/">
    <img src="https://img.shields.io/badge/Follow%20%40m.nopoh-Follow%20on%20Instagram-833AB4?logo=instagram&style=for-the-badge" alt="Instagram follow button">
  </a>
</div>




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


