# Email Scraper - Efficient Web Crawler

This project is an optimized email scraper written in Python. It crawls through websites starting from a user-provided URL and extracts email addresses. The script has been refactored for improved efficiency, modularity, and maintainability.

## Features

- **Modular Design:** Separated logic into functions for clarity and reusability.
- **Efficient URL Handling:** Uses `urllib.parse.urljoin` for robust URL building.
- **Robust Error Handling:** Manages connection errors and unexpected interruptions.
- **Command-Line Interface:** Simple prompts for user inputs.

## Prerequisites

- **Python 3.x**
- The following Python packages (see `requirements.txt`):
  - `beautifulsoup4`
  - `requests`
  - `pyfiglet`

## Installation

1. **Clone the repository:**

   ```bash
   git clone [https://github.com/Irfan3006/email-scraper.git](https://github.com/Irfan3006/emailscraper.git)
   cd emailscraper
   ```

2. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the email scraper, execute the script:

```bash
python3 emailscraper.py
```

You will be prompted to enter:
- The starting URL.
- The number of pages to crawl.

The program will then display the emails it finds during the crawl.

### Example Output
![image](https://github.com/user-attachments/assets/921c196b-c074-4e9c-9afb-f79cb0115188)


## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

Distributed under the MIT License. See the [LICENSE](LICENSE) file for more information.


Feel free to modify this tutorial to suit your project and add any additional details you find necessary!
