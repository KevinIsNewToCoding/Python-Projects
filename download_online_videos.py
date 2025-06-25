#!/usr/bin/env python3
"""Simple utility to download a YouTube video using ``yt_dlp``."""

import argparse
import os
import yt_dlp


def download_youtube_video(url: str, save_path: str) -> bool:
    """Download ``url`` to ``save_path``.

    The target directory is created if it does not already exist.

    Returns ``True`` on success and ``False`` if an error occurs.
    """

    os.makedirs(save_path, exist_ok=True)
    ydl_opts = {
        "outtmpl": os.path.join(save_path, "%(title)s.%(ext)s"),
        "format": "best",
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download completed!")
    except Exception as e:  # pragma: no cover - rely on yt_dlp error handling
        print(f"An error occurred: {e}")
        return False
    return True


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        description="Download a YouTube video using yt_dlp"
    )
    parser.add_argument("url", help="URL of the video to download")
    parser.add_argument("save_path", help="Directory to save the video")
    args = parser.parse_args(argv)

    download_youtube_video(args.url, args.save_path)


if __name__ == "__main__":  # pragma: no cover
    main()
