
# P2P File Share System

## Overview

The `P2P-file-share-system` is a peer-to-peer (P2P) file sharing system built in Python. This project aims to provide a simple and effective way for users to share files over a network without needing a centralized server. The system is designed to work efficiently in a distributed environment, allowing multiple users to share and download files simultaneously.

## Features

- **Peer-to-Peer Architecture:** No central server required, making the system resilient and scalable.
- **File Sharing:** Users can upload and download files from other peers in the network.
- **Search Functionality:** Search for specific files available across connected peers.
- **Concurrent Connections:** Supports multiple users sharing and downloading files simultaneously.
- **Logging and Monitoring:** Detailed logs for file transactions and peer activities.
- **Cross-Platform Compatibility:** Works on Windows, Linux, and macOS.

## Requirements

Before running the project, make sure you have the following installed:

- Python 3.7+
- `socket` library (default in Python standard library)
- `threading` library (default in Python standard library)
- `os`, `time`, and `json` (default in Python standard library)

## Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/AhmetNSHN/P2P-file-share-system.git
   cd P2P-file-share-system
   ```

2. **Run the Server and Peer Nodes:**

   Start the main server node using:

   ```bash
   python server.py
   ```

   Then, start peer nodes using:

   ```bash
   python peer.py --port <PORT_NUMBER> --dir <SHARE_DIRECTORY>
   ```

3. **Configuration:**

   Modify the `config.py` file to change server IP, port, or other settings if required.

## Usage

### Command-Line Options

The `peer.py` script supports several command-line options:

- `--port`: Specify the port number for the peer node.
- `--dir`: Specify the directory path for shared files.

Example:

```bash
python peer.py --port 5001 --dir /path/to/shared/files
```

### File Search

Once peers are connected to the network, you can use the following command to search for files:

```bash
search <FILENAME>
```

### Downloading Files

To download a file from a connected peer, use:

```bash
download <FILENAME>
```

The file will be saved to the shared directory specified when starting the peer node.
