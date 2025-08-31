# ComfyUI IP-Adapter Downloader

A simple and robust shell script to download all the official IP-Adapter models for ComfyUI.

This script automates the tedious process of downloading each model and placing it in the correct directory within your ComfyUI installation.

## Features

- **Comprehensive:** Downloads all standard, face, and SDXL IP-Adapter models, including the necessary CLIP Vision encoders and community models.
- **Correct Placement:** Automatically creates the required `models/ipadapter`, `models/clip_vision`, `models/loras`, and `models/insightface` directories.
- **Efficient:** Uses `aria2c` for multi-connection accelerated downloads if it's installed, otherwise falls back to `wget`.
- **Safe:** Checks for existing files and skips them, so you can run the script multiple times without re-downloading everything. It will also resume partially downloaded files.
- **Flexible:** Works with absolute and relative paths, so you can use paths like `/path/to/ComfyUI`, `../ComfyUI`, or `.` with ease.

## Requirements

- A `bash` shell (standard on Linux and macOS).
- `wget` or `aria2c` installed on your system.

## Usage

1.  **Make the script executable:**
    ```bash
    chmod +x download-ipadapters.sh
    ```

2.  **Run the script:**
    Provide the path to your ComfyUI root directory as the only argument.

    ```bash
    ./download-ipadapters.sh /path/to/your/ComfyUI
    ```

    For example:
    ```bash
    # If ComfyUI is in your home directory
    ./download-ipadapters.sh ~/ComfyUI

    # If you are running the script from within your ComfyUI directory
    ./download-ipadapters.sh .
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
