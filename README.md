# File Organizer GUI

This project is a file organizer application that helps users categorize and organize their files into designated folders based on file types. It features a graphical user interface (GUI) for ease of use.

## Project Structure

```
file-organizer-gui
├── src
│   ├── main.py        # Core functionality of the file organizer
│   └── gui.py         # Graphical user interface implementation
├── requirements.txt    # List of dependencies
└── README.md           # Project documentation
```

## Features

- Automatically categorizes files into folders based on their extensions.
- Creates folders for each category if they do not already exist.
- Handles duplicate filenames by renaming them appropriately.
- User-friendly GUI for easy interaction.

## Requirements

To run this project, you need to install the following dependencies:

- Python 3.x
- Tkinter (or PyQt, depending on the GUI framework used)

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd file-organizer-gui
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python src/gui.py
   ```

2. Enter the directory you want to organize in the GUI and click the organize button.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.