# FBShareBoost - Installation Guide for Termux

## Prerequisites
First, make sure your Termux is up to date:

```bash
pkg update && pkg upgrade
```

## Installation Steps

1. Install required packages in Termux:
```bash
pkg install python
pkg install git
```

2. Clone the repository:
```bash
git clone https://github.com/yourusername/fbshareboost.git
cd fbshareboost
```

3. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Running the Tool

1. Run the script:
```bash
python fbshare.py
```

## Troubleshooting

If you encounter any errors during installation:

1. Make sure all packages are up to date:
```bash
pkg update && pkg upgrade
```

2. Install Python pip if not installed:
```bash
pkg install python-pip
```

3. If you get SSL errors, install certificates:
```bash
pkg install openssl
```

4. If aiohttp installation fails, install these first:
```bash
pkg install build-essential
pkg install python-dev
```

## File Structure
```
fbshareboost/
├── fbshare.py          # Main script
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Notes
- Make sure you have a stable internet connection
- Some packages might take time to install
- If you get permission errors, try using `termux-setup-storage`

## Credits
- Developer: Ryo Evisu
- Version: 1.0.0
- Owned by: Thoss
