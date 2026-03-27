# SortMyChaos Pro

![SortMyChaos Pro](image-0.png)

[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://github.com/yourusername/SortMyChaos/actions/workflows/python-app.yml/badge.svg)](https://github.com/yourusername/SortMyChaos/actions)

> A high-performance, asynchronous file management engine that organizes your chaotic directories with lightning speed and professional-grade features.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Undo Functionality](#undo-functionality)
- [Logging](#logging)
- [Contributing](#contributing)
- [License](#license)
- [Developer](#developer)

## Features

✨ **Asynchronous Engine**: Utilizes `asyncio` and `pathlib` for blazing-fast file operations, handling thousands of files efficiently without blocking.

🔄 **Undo Functionality**: Maintains a local SQLite database to track all moves, allowing you to seamlessly undo the last organization session.

⚙️ **Customizable Configuration**: Uses a `config.yaml` file for defining file categories and extensions. Automatically creates a default config if none exists.

🎨 **Modern Terminal UI**: Features a professional dashboard built with the Rich library, including:
  - Real-time progress indicators
  - Summary tables showing file types, counts, and sizes
  - Status panels for system feedback

📝 **Comprehensive Logging**: Logs all activities and errors to `sort_log.txt` for debugging and auditing purposes.

🚀 **Cross-Platform**: Works on Windows, macOS, and Linux.

## Installation

### Prerequisites
- Python 3.9 or higher
- pip package manager

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/SortMyChaos.git
   cd SortMyChaos
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify installation**:
   ```bash
   python main.py --help
   ```

## Usage

### Organize a Directory
```bash
python main.py /path/to/your/directory
```

This command will:
- Scan the specified directory for files
- Move files into categorized subfolders based on extensions
- Display a live progress indicator
- Show a summary table with file counts and sizes

### Undo the Last Organization
```bash
python main.py --undo
```

This will reverse all moves from the most recent organization session.

### Example Output
```
System Status
─────────────
Starting organization...

Organizing files... ✓

File Organization Summary
─────────────────────────
Category    Count    Total Size (MB)
Images      15       245.67
Documents   8        12.34
Videos      3        1024.56
Others      2        5.78

System Status
─────────────
Organization complete!
```

## Configuration

SortMyChaos Pro uses a `config.yaml` file to define file categories and their associated extensions. If the file doesn't exist, a default configuration is automatically created.

### Default Configuration
```yaml
categories:
  Images:
    - .jpg
    - .jpeg
    - .png
    - .gif
    - .bmp
    - .tiff
    - .svg
  Videos:
    - .mp4
    - .avi
    - .mkv
    - .mov
    - .wmv
  Documents:
    - .pdf
    - .doc
    - .docx
    - .txt
    - .rtf
    - .odt
  Audio:
    - .mp3
    - .wav
    - .flac
    - .aac
    - .ogg
  Archives:
    - .zip
    - .rar
    - .7z
    - .tar
    - .gz
  Code:
    - .py
    - .js
    - .html
    - .css
    - .java
    - .cpp
    - .c
  Others: []  # Files not matching any category
```

### Customizing Categories
1. Edit `config.yaml` in your project root
2. Add new categories or modify existing ones
3. Restart the application to apply changes

**Note**: Extensions are case-insensitive. Files without matching extensions go to the "Others" folder.

## Undo Functionality

The undo feature uses a SQLite database (`history.db`) to track all file moves. Each organization session creates a new entry, allowing precise reversal.

- **Automatic Tracking**: Every move is logged with source and destination paths
- **Session-Based**: Undo affects only the last complete organization session
- **Safe Reversal**: Moves files back to their original locations
- **Database Cleanup**: Undone sessions are removed from the database

## Logging

All operations are logged to `sort_log.txt` with timestamps:

```
2026-03-27 10:30:15 - INFO - Moved /path/to/file.jpg to /path/to/Images/file.jpg
2026-03-27 10:30:16 - ERROR - Failed to move /path/to/locked_file.txt: Permission denied
```

Log levels include:
- **INFO**: Successful operations
- **ERROR**: Failed operations with details
- **WARNING**: Non-critical issues

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup
```bash
git clone https://github.com/yourusername/SortMyChaos.git
cd SortMyChaos
pip install -r requirements.txt
pip install flake8  # For linting
```

### Code Style
- Follow PEP 8 guidelines
- Use type hints where appropriate
- Ensure all code passes flake8 linting
- Add tests for new features

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Developer

**Yazan Ayasrah** - Senior DevOps & Python Engineer  
Specializing in Pearson BTEC IT Systems with Triple-Certified Gemini AI Specialist status.

---

*Built with ❤️ using Python, asyncio, and Rich*