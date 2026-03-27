import argparse
import asyncio
import logging
from pathlib import Path
from organizer import FileOrganizer
from ui import create_summary_table, create_status_panel, console

logging.basicConfig(filename='sort_log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

async def main():
    parser = argparse.ArgumentParser(description="SortMyChaos Pro - File Organizer")
    parser.add_argument('directory', nargs='?', help='Directory to organize (not needed for --undo)')
    parser.add_argument('--undo', action='store_true', help='Undo last organization session')
    args = parser.parse_args()

    organizer = FileOrganizer()

    if args.undo:
        organizer.undo_last_session()
        return
    elif not args.directory:
        parser.error("Directory required for organization (or use --undo)")
    else:
        dir_path = Path(args.directory)
        console.print(create_status_panel("Starting organization..."))

        with console.status("Organizing files...") as status:
            session_id = await organizer.organize_files(str(dir_path))

        # Calculate summary
        files_info = {}
        for cat in list(organizer.categories.keys()) + ['Others']:
            cat_path = dir_path / cat
            if cat_path.exists():
                files = list(cat_path.glob('*'))
                count = len([f for f in files if f.is_file()])
                size = sum(f.stat().st_size for f in files if f.is_file()) / (1024 * 1024)  # MB
                files_info[cat] = {'count': count, 'size': round(size, 2)}

        console.print(create_summary_table(files_info))
        console.print(create_status_panel("Organization complete!"))

if __name__ == '__main__':
    asyncio.run(main())