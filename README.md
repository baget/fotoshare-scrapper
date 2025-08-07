# Get Photos - Fotoshare Image Scraper

A Python script that automatically downloads images from fotoshare.co using web scraping techniques. The script navigates through web pages, finds images, and downloads them to your local machine.

Built with modern Python tooling using [UV](https://github.com/astral-sh/uv) for fast dependency management.



## 🔧 How It Works

Think of this script like a digital assistant that:
1. **Opens a web browser** (using Playwright) to visit fotoshare.co pages
2. **Looks for image containers** with special `data-url` attributes
3. **Follows links** to find more images on related pages  
4. **Downloads images** (skipping thumbnails and SVG files) to keep full-quality versions
5. **Organizes everything** into a local `photos` folder

## 📋 Prerequisites

- Python 3.12 or higher
- [UV](https://github.com/astral-sh/uv) package manager
- Windows, macOS, or Linux

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/baget/fotoshare-scrapper.git
cd fotoshare-scrapper
```

### 2. Install Dependencies with UV
```bash
# Install all dependencies (including development dependencies)
uv sync

# Or install only production dependencies
uv install
```

### 3. Install Playwright Browser
```bash
uv run playwright install chromium
```

### 4. Create Photos Directory
```bash
mkdir photos
```

## 🎯 Usage

### Basic Setup
1. Open `main.py` in your text editor
2. Replace `WHAT_EVER_YOU_WANT_TO_SCRAPE` with the actual page path you want to scrape:
   ```python
   INDEX_PAGE = "/gallery/your-target-page"  # Example
   ```

### Run the Script
```bash
# Using UV to run the script
uv run python main.py

# Or activate the virtual environment and run directly
uv shell
python main.py
```

### What Happens Next
- The script will open a browser and navigate to your specified page
- It will find all image containers and follow their links
- Images will be downloaded to the `photos/` folder
- Progress will be shown in the terminal
- A small delay (0.3 seconds) between downloads prevents server overload

## 📁 Project Structure

```
get-photos/
├── main.py          # Main scraping script
├── pyproject.toml   # UV project configuration and dependencies
├── photos/          # Downloaded images folder (created automatically)
├── README.md        # This file
├── LICENSE          # MIT license file
└── .python-version  # Python version specification (created by UV)
```

## ⚙️ Configuration Options

You can modify these variables in `main.py`:

| Variable | Description | Default |
|----------|-------------|---------|
| `BASE_URL` | The base website URL | `"https://fotoshare.co"` |
| `INDEX_PAGE` | Starting page path | `"WHAT_EVER_YOU_WANT_TO_SCRAPE"` |
| `PHOTOS_FOLDER` | Download destination | `"photos"` |

### Adjusting Download Speed
To be more respectful of the server, you can increase the delay between downloads:
```python
time.sleep(1.0)  # Wait 1 second instead of 0.3
```

## 🔍 How the Script Works (Technical Details)

### Step-by-Step Process:
1. **Browser Launch**: Uses Playwright's Chromium browser in headless mode
2. **Page Navigation**: Visits the specified fotoshare.co page
3. **Element Discovery**: Finds `<div data-url="...">` elements containing page references
4. **Link Following**: Navigates to each discovered page
5. **Image Extraction**: Locates all `<img>` elements on each page
6. **URL Cleaning**: Removes query parameters from image URLs
7. **Filtering**: Skips SVG files and thumbnail images (`_thumb`)
8. **Download**: Uses requests library to fetch and save images

### Key Functions:
- `main()`: Entry point, coordinates the scraping process
- `get_images()`: Navigates to URLs and extracts image links  
- `download_image()`: Downloads individual images to local storage

## 🛠️ Troubleshooting

### Common Issues:

**"uv not found"**
- Install UV following the installation instructions above
- Restart your terminal after installation

**"playwright not found"**
```bash
uv add playwright
uv run playwright install chromium
```

**Virtual environment issues**
```bash
# Reset the environment
uv sync --reinstall
```

**"Permission denied" when creating photos folder**
- Make sure you have write permissions in the current directory
- Try running as administrator (Windows) or with sudo (Linux/Mac)

**Images not downloading**
- Check your internet connection
- Verify the `INDEX_PAGE` path is correct
- The target page might have changed its structure

**Script runs but finds no images**
- The website might have updated its HTML structure
- Check if the page requires JavaScript to load images
- Verify you're targeting the correct page

## 📝 Dependencies

This project uses UV for dependency management, with all dependencies defined in `pyproject.toml`:

**Runtime Dependencies:**
- **requests**: HTTP library for downloading images
- **playwright**: Browser automation for web scraping  

**Development Dependencies:**
- **pytest-playwright**: Testing framework integration

**Built-in Python Modules:**
- **urllib.parse**: URL manipulation
- **time**: Adding delays between requests

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔄 Version History

- **v0.1.0**: Initial release with basic scraping functionality

## 📞 Support

If you encounter issues:
1. Check the troubleshooting section above
2. Search existing issues on GitHub
3. Create a new issue with detailed error messages and steps to reproduce

## 📄 Legal Notice

This software is provided for educational purposes. Users are responsible for:
- Respecting website terms of service
- Following robots.txt guidelines  
- Respecting copyright and intellectual property rights
- Using reasonable request rates to avoid server strain

The authors are not responsible for misuse of this tool.
