# QR-Phish

A simple Python tool that generates QR codes as HTML files. This tool creates QR codes using div elements, allowing for potential manipulation of the QR code appearance through CSS.

## Features

- Generate QR codes from URLs
- Output as HTML file with customizable styling
- Minimal dependencies
- Command-line interface

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/qr-phish.git
   cd qr-phish
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
## Usage

Basic usage:
```bash
python qr-phish.py -u https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

Customize output:
```bash
python qr-phish.py -u https://www.youtube.com/watch?v=dQw4w9WgXcQ -o custom-qr.html
```


