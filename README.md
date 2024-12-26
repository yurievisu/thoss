# THOSS AUTO SHARE TOOL

An efficient tool for automated Facebook post sharing with persistent session support.

![Thoss Banner](https://raw.githubusercontent.com/yurievisu/thoss/main/img/thoss.png)

## Termux Installation

```bash
pkg update && pkg upgrade
pkg install python git
git clone https://github.com/yurievisu/thoss.git
cd thoss
pip install -r requirements.txt
python runshare-ENC.py
```

## Key Features

- 🔄 Continuous share automation
- 🕒 Real-time PH timezone tracking
- 🔐 Cookie persistence
- 🔄 Auto-retry mechanism
- 📊 Live share count display
- ⚡ Fast execution
- 📱 Mobile-friendly

## How to Get Facebook Cookie

1. Login to Facebook (Chrome/Firefox)
2. Open DevTools (F12)
3. Go to Network tab
4. Select any facebook.com request
5. Find 'cookie' in request headers
6. Copy complete cookie value

## Important Notes

- 🔒 Never share your cookies
- 🔗 Use HTTPS links only
- 📈 Share count must be > 0
- 🔑 Keep cookies private
- 🌐 Post must be public

## Troubleshooting

✅ Check internet connection
✅ Verify cookie validity
✅ Confirm post URL format
✅ Ensure post is shareable
✅ Validate share count

## Support

For issues or queries:
- Create an issue on GitHub
- Contact: @yurievisu

## Credits

Created with ❤️ by Yuri

## License

This project is open source.
