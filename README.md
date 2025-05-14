# PECO-Online-Gas-Price-Scraper

*A Python script to fetch fuel prices from PECO Online*

## How It Works

This script scrapes gas prices from [PECO Online](https://www.peco-online.ro/) by mimicking user's form submission. Instead of scraping static HTML, it sends a `POST` request with filters and extracts the dynamically loaded data.

## Setup

1. Created a virtual environment
`python -m venv prices_scraper`

2. Installed dependencies
`python -m pip install requests`
`python -m pip install beautifulsoup4`

## Execution Flow

- Send a `POST` request with filters
- Parse HTML response with `BeautifulSoup`
- Extract JSON data from `<script>` tag using regex
- Decode escaped characters and convert JSON to Python list
- Display results
