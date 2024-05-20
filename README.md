
# Kotoba Wallpaper App Documentation

## Overview

The Kotoba Wallpaper App is a desktop program designed to help users study Japanese vocabulary. It periodically updates the desktop background with new vocabulary items, including kanji, readings, and meanings. Users can customize the text color, and background color.

## Features

- Periodic wallpaper updates with Japanese vocabulary.
- Customizable text and background colors.
- Countdown timer for the next update.
- Minimize to taskbar functionality with a tray icon.

## Requirements

- Python 3.6 or higher
- Required Python packages:
  - `PyQt5`
  - `Pillow`
  - `pystray`

## Installation

1. **Clone the repository** (or create the necessary files):
   ```bash
   git clone <repository_url>
   cd vocab-wallpaper
   ```

2. **Install the required packages**:
   ```bash
   pip install PyQt5 Pillow pystray
   ```

3. **Create necessary directories and files**:
   Ensure you have the following structure:
   ```
   vocab-wallpaper/
   ├── data/
   │   └── vocab.json
   ├── backgrounds/
   │   └── japstudy_bg.jpg
   ├── icon.png
   ├── main.py
   ├── generate_image.py
   └── change_wallpaper.py
   ```

4. **Prepare the vocabulary file**:
   - `data/vocab.json`: A JSON file containing vocabulary items.
   ```json
   [
     {
       "kanji": "現像",
       "readings": ["げんぞう", "genzou"],
       "meaning": "developing (film)"
     },
     {
       "kanji": "原則",
       "readings": ["げんそく", "gensoku"],
       "meaning": "principle, general rule"
     },
     {
       "kanji": "見地",
       "readings": ["けんち", "kenchi"],
       "meaning": "point of view"
     },
     {
       "kanji": "現地",
       "readings": ["げんち", "genchi"],
       "meaning": "actual place, local"
     },
     {
       "kanji": "限定",
       "readings": ["げんてい", "gentei"],
       "meaning": "limit, restriction"
     },
     {
       "kanji": "原点",
       "readings": ["げんてん", "genten"],
       "meaning": "origin (coordinates, starting point)"
     }
   ]
   ```

## Running the Application

1. **Start the application**:
   ```bash
   python main.py
   ```

## Usage

### Main Window

- **Next update in:** Displays the countdown timer until the next wallpaper update.
- **Choose Text Color:** Opens a color picker to choose the text color.
- **Choose Background Color:** Opens a color picker to choose the background color.
- **Update Now:** Manually triggers an immediate wallpaper update.

### Tray Icon

- **Show:** Brings the application window back into view.
- **Quit:** Exits the application.

## File Descriptions

### `main.py`

The main application file, which sets up the UI, manages timers, and handles interactions.

### `generate_image.py`

Contains functions to generate the wallpaper image with the provided vocabulary.

#### Functions

- **`load_vocab_from_json(filepath)`**: Loads vocabulary from a JSON file.
- **`generate_image(vocab, output_path, text_color='black', bg_color='white')`**: Generates an image with the given vocabulary and saves it to the specified path.

### `change_wallpaper.py`

Contains functions to change the desktop wallpaper.

#### Functions

- **`change_wallpaper(image_path)`**: Changes the desktop wallpaper to the specified image.

## Example

Here’s an example of running the application:

1. **Run the application**:
   ```bash
   python main.py
   ```

2. **Configure settings**:
   - Choose your preferred text and background colors.
   - Use the "Update Now" button to immediately see the changes.

3. **Minimize to taskbar**:
   - Close the application window to minimize it to the taskbar.
   - Use the tray icon to restore the window or quit the application.

## Troubleshooting

- **Wallpaper not updating**: Ensure the `japstudy_bg.jpg` file is being generated correctly and that the path is correct.
- **Application not starting**: Verify all dependencies are installed and the file paths are correct.

## Contributions

Contributions are welcome! Please create a pull request or submit issues on the GitHub repository.

---

This documentation should help you set up, run, and use the Kotoba Wallpaper App. If you have any specific questions or need further customization, feel free to ask!
