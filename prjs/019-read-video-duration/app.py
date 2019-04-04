import subprocess


def get_duration(url):
    """Get the duration of a video using ffprobe."""
    cmd = 'ffprobe -i {} -show_entries format=duration -v quiet -of csv="p=0"'.format(url)
    output = subprocess.check_output(
        cmd,
        shell=True,
        stderr=subprocess.STDOUT
    )
    return float(output)


def main():
    video_urls = [
        "http://i4.chuimg.com/ce94ccea88ae11e89c2402420a000130_720w_720h.mp4",
        "http://i4.chuimg.com/0a7e9af88a4711e89c2402420a000130_720w_720h.mp4",
    ]
    for video_url in video_urls:
        print(video_url, get_duration(video_url))


if __name__ == '__main__':
    main()

# https://stackoverflow.com/questions/26974921/how-to-get-a-online-videos-duration-without-downloading-the-full-video
