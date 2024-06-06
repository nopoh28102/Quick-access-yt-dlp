# -*- coding: utf-8 -*-
from yt_dlp import YoutubeDL
import os
import sys
import requests
from termcolor import colored
from colorama import init

init()  # Initialize colorama for Windows

def check_internet_connection():
    try:
        requests.get('http://www.google.com', timeout=1)
        return True
    except requests.ConnectionError:
        return False

def check_youtube_link(url):
    if 'youtube.com' in url:
        return True
    else:
        return False

def progress_hook(d):
    if d['status'] == 'downloading':
        downloaded_percent = d['_percent_str']
        downloaded_size = d['_total_bytes_str']
        speed = d['_speed_str']
        eta = d['_eta_str']
        sys.stdout.write("\rDownloading: {} ({}) at {} - ETA: {}".format(downloaded_percent, downloaded_size, speed, eta))
        sys.stdout.flush()

def download_videos(urls, options):
    ydl_opts = {
        'format': 'bestvideo+bestaudio',
        'outtmpl': '%(title)s.%(ext)s',
        'quiet': False,
        'no_warnings': True,
        'retries': 3,
        'progress_hooks': [progress_hook],  # Add this line for progress bar
    }
    if 'quality' in options:
        ydl_opts['format'] = options['quality']
    if 'output_path' in options:
        ydl_opts['outtmpl'] = os.path.join(options['output_path'], '%(title)s.%(ext)s')
    if 'audio_only' in options and options['audio_only']:
        ydl_opts['postprocessors'] = [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'}]
    if 'resolution' in options:
        ydl_opts['format'] = f'bestvideo[height<={options["resolution"]}]+bestaudio/best[height<={options["resolution"]}]'
    if 'compressed' in options and options['compressed']:
        ydl_opts['format'] = 'bestvideo[ext=mp4]+bestaudio/best[ext=mp4]'
    if 'subtitles' in options and options['subtitles']:
        ydl_opts['writesubtitles'] = True
        ydl_opts['allsubtitles'] = True
    if 'start' in options and 'end' in options:
        ydl_opts['postprocessors'] = [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'}]
        ydl_opts['start'] = options['start']
        ydl_opts['end'] = options['end']
    if 'encoding' in options:
        ydl_opts['encoding'] = options['encoding']
    if 'no_check_certificate' in options and options['no_check_certificate']:
        ydl_opts['no_check_certificate'] = True
    if 'proxy' in options:
        ydl_opts['proxy'] = options['proxy']

    with YoutubeDL(ydl_opts) as ydl:
        for url in urls:
            ydl.download([url])

def get_video_info(url):
    with YoutubeDL({}) as ydl:
        info_dict = ydl.extract_info(url, download=False)
    return info_dict

def print_menu():
    print("╔════════════════════════════════════════════════════════╗")
    print("║            Quick Access Menu (nabih)                   ║")
    print("╠════════════════════════════════════════════════════════╣")
    print("║ 1. " + colored("Select Quality", "green") + "          ║")
    print("║ -----------------------------------------------------  ║")
    print("║ 2. " + colored("Select Output Path", "green") + "       ║")
    print("║ -----------------------------------------------------  ║")
    print("║ 3. " + colored("Select Audio Only Download", "green") + " ║")
    print("║ ----------------------------------------------------- ║")
    print("║ 4. " + colored("Select Resolution", "green") + "       ║")
    print("║ ----------------------------------------------------- ║")
    print("║ 5. " + colored("Select Compressed Video Download", "green") + "║")
    print("║ ----------------------------------------------------- ║")
    print("║ 6. " + colored("Select Subtitles Download", "green") + "║")
    print("║ ----------------------------------------------------- ║")
    print("║ 7. " + colored("Select Start and End", "green") + "   ║")
    print("║ ----------------------------------------------------- ║")
    print("║ 8. " + colored("Select Encoding", "green") + "         ║")
    print("║ ----------------------------------------------------- ║")
    print("║ 9. " + colored("Ignore Certificate Check", "yellow") + "   ║")
    print("║ ----------------------------------------------------- ║")
    print("║ 10. " + colored("Select Proxy Settings", "green") + "  ║")
    print("║ ----------------------------------------------------- ║")
    print("║ 11. " + colored("Start Download", "green") + "      ║")
    print("║ ----------------------------------------------------- ║")
    print("║ 12. " + colored("Exit", "red") + "                     ║")
    print("╚════════════════════════════════════════════════════════╝")

if __name__ == "__main__":
    video_urls = []
    while True:
        url = input("Enter a YouTube video link (press enter to finish): ")
        if url.strip() == "":
            break
        video_urls.append(url.strip())

    if not check_internet_connection():
        print("No internet connection. Please check your connection and try again.")
        sys.exit()

    invalid_urls = [url for url in video_urls if not check_youtube_link(url)]
    if invalid_urls:
        print("The following entered links are not YouTube video links:")
        for invalid_url in invalid_urls:
            print(invalid_url)
        print("Please make sure all entered links are valid video links and try again.")
        sys.exit()

    options = {}
    while True:
        print_menu()
        choice = input("\nChoose option number: ")
        
        if choice == '1':
            options['quality'] = input("Enter desired quality (best/worst/etc): ")
        elif choice == '2':
            options['output_path'] = input("Enter output path (leave blank for current directory): ")
        elif choice == '3':
            options['audio_only'] = input("Download audio only? (yes/no): ").lower() == 'yes'
        elif choice == '4':
            options['resolution'] = input("Enter maximum resolution (e.g., 720): ")
        elif choice == '5':
            options['compressed'] = input("Download compressed video (mp4)? (yes/no): ").lower() == 'yes'
        elif choice == '6':
            options['subtitles'] = input("Download subtitles? (yes/no): ").lower() == 'yes'
        elif choice == '7':
            options['start'] = input("Enter start time (in seconds, leave blank for full video): ")
            options['end'] = input("Enter end time (in seconds, leave blank for full video): ")
        elif choice == '8':
            options['encoding'] = input("Enter desired encoding (leave blank for default): ")
        elif choice == '9':
            options['no_check_certificate'] = input("Ignore certificate check? (yes/no): ").lower() == 'yes'
        elif choice == '10':
            options['proxy'] = input("Enter proxy settings (leave blank if not required): ")
        elif choice == '11':
            download_videos(video_urls, options)
        elif choice == '12':
            print("Exiting.")
            sys.exit()
        else:
            print("Invalid choice. Please select a valid option from the menu.")
