# SortMyChaos Pro

A high-performance, asynchronous file management engine that organizes your chaotic directories with lightning speed.

## Features

- **Asynchronous Engine**: Utilizes asyncio and pathlib for blazing-fast file operations, handling thousands of files efficiently.
- **Undo Functionality**: Maintains a local SQLite database to track moves, allowing you to undo the last organization session.
- **Customizable Configuration**: Uses a config.yaml file for defining file categories and extensions. Creates a default config if none exists.
- **Modern Terminal UI**: Features a professional dashboard with Rich library, including progress indicators, summary tables, and status panels.
- **Comprehensive Logging**: Logs all activities and errors to sort_log.txt for debugging and auditing.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/SortMyChaos.git
   cd SortMyChaos
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Organize a directory:
```bash
python main.py /path/to/your/directory
```

Undo the last organization:
```bash
python main.py /path/to/your/directory --undo
```

## Configuration

Edit `config.yaml` to customize file categories and extensions:

```yaml
categories:
  Images: ['.jpg', '.png', '.gif']
  Documents: ['.pdf', '.docx', '.txt']
  # Add your own categories
```

## Developer

**Yazan Ayasrah** - Senior DevOps & Python Engineer  
Specializing in Pearson BTEC IT Systems with Triple-Certified Gemini AI Specialist status.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.