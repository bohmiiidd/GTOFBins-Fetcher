# GTOFBins-Fetcher
A simple and fast Python tool to quickly check for known exploits related to binaries listed on GTFOBins. It's easy to use and adds fun color animations and emoji effects while you work in your terminal. Perfect for speeding up your workflow when you're testing binaries and looking for privilege escalation techniques  💻🚀

## Features

- **Fast and Simple**: Quickly check binaries for known exploits.
- **Single or Batch Checking**: Check one binary at a time or use a file to check multiple binaries.
- **Colorful Terminal Output**: Enjoy terminal output with colored text and fun emoji animations.
- **A tool created to speed up your workflow while you’re working on privilege escalation techniques :)**

## Requirements

- `Python 3.x`
- `requests`
- `beautifulsoup4`
- `colorama`

To install the dependencies, run:

```bash
pip install -r requirements.txt
```

## Usage

### Check a single binary

To check suite of binaries, use the `--bin` option followed by the binary name (e.g., `find,base64,vim`):

```bash
python3 GTOFBins.py --bin find
```

### Check multiple binaries from a file

To check multiple binaries listed in a file, use the `--file` option:

```bash
python3 GTOFBins.py --file binaries.txt
```

Where `binaries.txt` is a text file containing a list of binaries (one per line).

## Example Output

When you run the tool, it will display colored text and emojis as it checks the binary.

## Developer

This tool is developed by **Ahmed Abd**.

## License

This project is open-source. Feel free to fork, modify, and contribute!

---

This README is designed to be easy to understand, with clear instructions for installation, usage, and what the project is about. You can expand on any section if needed, but it should be a great starting point!
