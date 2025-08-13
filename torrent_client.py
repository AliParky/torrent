class TorrentClient:
    def get_info_hash(self, torrent_file):
        with open(torrent_file, 'rb') as f:
            data = f.read()
        info_start = data.find(b'4:infod')
        return