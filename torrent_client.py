import hashlib

class TorrentClient:
    def get_info_hash(self, torrent_file):
        """Extract and hash the info dictionary from a torrent file"""
        with open(torrent_file, 'rb') as f:
            data = f.read()
        
        # Find info dictionary start
        info_start = data.find(b'4:infod')

        # Extract info dict
        info_dict = data[info_start + 6:-1]
        
        return hashlib.sha1(info_dict).hexdigest()
    
    def verify_piece(self, piece_data, expected_hash):
        """Verify a downloaded piece matches expected hash"""
        return hashlib.sha1(piece_data).digest() == expected_hash
    
    def download(self, torrent_file):
        with open(torrent_file, 'rb') as f:
            data = f.read()
        return
        
    def _decode_bencode(self, data):
        """Decode bencoded data"""
        def decode_next(data, index):
            if data[index:index+1] == b'i':
                return int(data[index+1:data.index(b'e', index)]), data.index(b'e', index) + 1
            return
        return