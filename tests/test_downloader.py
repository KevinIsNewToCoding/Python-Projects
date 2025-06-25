import importlib.util
import importlib.machinery
import sys
import types
from pathlib import Path
from unittest import mock

MODULE_PATH = Path(__file__).resolve().parents[1] / "Download Online Videos"


def load_downloader():
    if 'yt_dlp' not in sys.modules:
        sys.modules['yt_dlp'] = types.ModuleType('yt_dlp')
        sys.modules['yt_dlp'].YoutubeDL = mock.MagicMock()
    loader = importlib.machinery.SourceFileLoader('downloader', str(MODULE_PATH))
    spec = importlib.util.spec_from_loader('downloader', loader)
    module = importlib.util.module_from_spec(spec)
    loader.exec_module(module)
    return module


def test_download_youtube_video():
    downloader = load_downloader()
    with mock.patch('yt_dlp.YoutubeDL') as MockYT:
        mock_instance = MockYT.return_value.__enter__.return_value
        downloader.download_youtube_video('http://example.com', '/tmp')
        MockYT.assert_called_once_with({'outtmpl': '/tmp/%(title)s.%(ext)s', 'format': 'best'})
        mock_instance.download.assert_called_once_with(['http://example.com'])
