from pytube import YouTube
from pytube.exceptions import RegexMatchError
from termcolor import colored
import os
import ssl
from tqdm import tqdm
import time

# Define global variables
video_urls = []
output_path = None
selected_quality = None
audio_only = None
selected_resolution = None
compressed_video = None
start_time = None
end_time = None
encoding = None
proxy_settings = None


def print_menu():
    print("╔════════════════════════════════════════════════════════╗")
    print("║                   Quick Access Menu                    ║")
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






def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    stars = int(percentage / 2)
    progress_bar = '[' + colored('*' * stars, 'green') + ' ' * (50 - stars) + ']'
    print(f"\rDownloaded {bytes_downloaded} bytes out of {total_size} bytes ({percentage:.2f}%) {progress_bar}", end='', flush=True)




def get_video_urls():
    global video_urls
    while True:
        url = input("Enter a YouTube video link (press enter to finish): ")
        if url.strip() == "":
            break
        video_urls.append(url.strip())



def select_quality():
    global selected_quality
    yt = YouTube(video_urls[0], on_progress_callback=on_progress)
    video_streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()

    print("Available video qualities:")
    for i, stream in enumerate(video_streams):
        print(f"{i+1}. Resolution: {stream.resolution}, Format: {stream.mime_type}")

    choice = int(input("Enter the number of the desired quality: "))
    if 1 <= choice <= len(video_streams):
        selected_quality = video_streams[choice - 1]
        print(f"You selected {selected_quality.resolution} resolution.")
    else:
        print("Invalid choice. Please try again.")


def select_output_path():
    global output_path
    output_path = input("Enter output path: ")
    if os.path.isdir(output_path):
        print("Output path is valid.")
    else:
        print("Invalid output path. Please try again.")


def select_audio_only():
    global audio_only
    choice = input("Do you want to download audio only? (yes/no): ").lower()
    if choice == 'yes':
        print("Downloading audio only.")
        audio_only = True
    elif choice == 'no':
        print("Downloading full video.")
        audio_only = False
    else:
        print("Invalid choice. Please try again.")


def select_resolution():
    global selected_resolution
    yt = YouTube(video_urls[0], on_progress_callback=on_progress)
    video_streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()

    print("Available video resolutions:")
    for i, stream in enumerate(video_streams):
        print(f"{i+1}. Resolution: {stream.resolution}, Format: {stream.mime_type}")

    choice = int(input("Enter the number of the desired resolution: "))
    if 1 <= choice <= len(video_streams):
        selected_resolution = video_streams[choice - 1]
        print(f"You selected {selected_resolution.resolution} resolution.")
    else:
        print("Invalid choice. Please try again.")


def select_compressed_video():
    global compressed_video
    choice = input("Do you want to download compressed video? (yes/no): ").lower()
    if choice == 'yes':
        print("Downloading compressed video.")
        compressed_video = True
    elif choice == 'no':
        print("Downloading full quality video.")
        compressed_video = False
    else:
        print("Invalid choice. Please try again.")


def download_subtitles():
    global output_path
    yt = YouTube(video_urls[0])
    subtitles = yt.captions.all()

    if subtitles:
        print("Available subtitles:")
        for subtitle in subtitles:
            print("- Language: {}, Code: {}".format(subtitle.name, subtitle.code))
        
        choice = input("Enter subtitle code to download (leave empty to skip): ").strip()
        if choice:
            try:
                selected_subtitle = yt.captions.get_by_language_code(choice)
                selected_subtitle.download(output_path, srt=True)
                print("Subtitles downloaded successfully!")
            except:
                print("Error downloading subtitles. Please try again.")
    else:
        print("No subtitles available for this video.")


def select_start_end():
    global start_time, end_time
    start_time = input("Enter start time (format: HH:MM:SS): ")
    end_time = input("Enter end time (format: HH:MM:SS): ")


def select_encoding():
    global encoding
    encoding = input("Enter encoding (leave empty for default): ").strip()


def ignore_certificate_check():
    # Ignore certificate verification
    ssl._create_default_https_context = ssl._create_unverified_context
    print("Certificate check will be ignored.")


def select_proxy_settings():
    global proxy_settings
    proxy_type = input("Enter proxy type (http, https, socks4, socks5): ")
    proxy_ip = input("Enter proxy IP address: ")
    proxy_port = input("Enter proxy port number: ")
    # يمكنك هنا إضافة مزيد من الإعدادات للوكيل إذا لزم الأمر
    proxy_settings = {
        "proxy_type": proxy_type,
        "proxy_ip": proxy_ip,
        "proxy_port": proxy_port
    }


def get_video_information(url):
    yt = YouTube(url)
    print("Title:", yt.title)
    print("Author:", yt.author)
    print("Length (seconds):", yt.length)
    print("Views:", yt.views)
    print("Rating:", yt.rating)



def extract_video_id(url):
    # تقوم هذه الدالة بإستخراج معرف الفيديو من العنوان URL
    if "youtube.com/watch?v=" in url:
        video_id_index = url.index("=") + 1
        video_id = url[video_id_index:]
    elif "youtu.be/" in url:
        video_id_index = url.index("be/") + 3
        video_id = url[video_id_index:]
    else:
        raise ValueError("Invalid YouTube URL")
    return video_id



def download_video():
    global output_path, selected_quality, audio_only, selected_resolution, compressed_video, start_time, end_time, encoding, proxy_settings

    try:
        select_quality()
    except ValueError:
        print("Invalid YouTube URL. Please enter a valid URL.")
        return

    try:
        yt = YouTube(video_urls[0], on_progress_callback=on_progress)
    except RegexMatchError:
        print("Error: Unable to fetch video information.")
        return

    if selected_resolution:
        video = selected_resolution
    else:
        video = selected_quality

    if audio_only is not None and audio_only:
        video = yt.streams.filter(only_audio=True).first()

    if start_time and end_time:
        video = video.streams.filter(subtype='mp4').first()
        video.download(output_path, filename_prefix=f'{start_time}-{end_time}')

    if encoding:
        video.download(output_path, filename_prefix=encoding)

    if proxy_settings:
        tqdm.write("Downloading video...")
        video.download(output_path, filename_prefix='proxy')
    else:
        tqdm.write("Downloading video...")
        video.download(output_path)

    tqdm.write("Download completed.")


def exit_program():
    print("Exiting...")
    return

def main():
    global selected_quality, output_path, audio_only, selected_resolution, compressed_video, start_time, end_time, encoding, proxy_settings
    
    get_video_urls()
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            select_quality()
        elif choice == '2':
            select_output_path()
        elif choice == '3':
            select_audio_only()
        elif choice == '4':
            select_resolution()
        elif choice == '5':
            select_compressed_video()
        elif choice == '6':
            download_subtitles()
        elif choice == '7':
            select_start_end()
        elif choice == '8':
            select_encoding()
        elif choice == '9':
            ignore_certificate_check()
        elif choice == '10':
            select_proxy_settings()
        elif choice == '11':
            if output_path:
                download_video()
            else:
                print("Please select output path first.")
        elif choice == '12':
            exit_program()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
