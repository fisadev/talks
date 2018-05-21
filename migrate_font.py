from pathlib import Path

for file_path in Path('.').glob('*.svg'):
    with file_path.open() as original_file:
        contents = original_file.read()

    contents = contents.replace(
        "font-family:CPMono_v07",
        "font-family:'CPMono_v07 Plain for Powerline'",
    )
    contents = contents.replace(
        "-inkscape-font-specification:CPMono_v07 Light",
        "-inkscape-font-specification:'CPMono_v07 Plain for Powerline'",
    )

    with file_path.open('w') as migrated_file:
        migrated_file.write(contents)
