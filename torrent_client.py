class TorrentClient:
    def get_info_hash(self, torrent_file):
        with open(torrent_file, 'rb') as f:
            data = f.read()
        
        # Find info dictionary start
        info_start = data.find(b'4:infod')

        # Extract info dict
        info_dict = data[info_start + 6:-1]
        return