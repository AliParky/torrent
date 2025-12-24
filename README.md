# torrent

A minimal implementation of a BitTorrent client written in Python.

## Overview

This project implements a basic BitTorrent client that can download files using the BitTorrent protocol. The client handles torrent file parsing, peer discovery, and file downloading.

## Features

- Torrent file parsing (.torrent files)
- Info hash calculation
- Peer discovery via trackers
- File downloading from peers
- Basic BitTorrent protocol implementation

## Requirements

- Python 3.7+
- Required packages:
    - `hashlib` - for SHA-1 hash calculations
    - `requests` - for HTTP tracker communication
    - `struct` - for binary data packing and unpacking
    - `socket` - for TCP network connections to peers

## Installation

1. Clone this repository

```bash
git clone git clone https://github.com/AliParky/torrent
```
2. Install required dependencies
```bash
pip install hashlib requests struct socket
```
3. Navigate to the project directory
```bash
cd torrent
```
4. Run the client with a torrent file

## How It Works

1. The client reads .torrent files and decodes bencoded data format
2. Extracts metadata and calculates info hash (SHA-1) for torrent identification
2. Generates unique identifiers for torrents
3. Contacts trackers to discover peers
4. Establishes connections with other peers
5. Downloads file pieces from first available peer