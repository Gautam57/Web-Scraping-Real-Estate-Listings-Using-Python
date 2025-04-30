# Web Scraping Real Estate Listings Using Python

A modular web scraper built using **Python**, **Selenium**, and **JavaScript** to extract real estate data (price and area) from a dynamic German property website.

## Features

- Scrapes listing data by **postal code** and **property type** (e.g., Apartment, House)
- Uses **JavaScript** for interacting with dynamic web elements
- **Modular code design** for easy scaling and maintenance
- Saves results into a structured **CSV file**

## Technologies Used

- Python
- Selenium WebDriver
- JavaScript (DOM interaction)
- Pandas

## File Structure

```
.
├── WebScraper.py
├── javascripts/
│   ├── clickOnNextPage.js
│   ├── clickOnSearch.js
│   ├── enterPostalCode.js
│   ├── getData.js
│   ├── totalPages.js
│   └── typeSelection.js
└── immobilien.csv (output)
```

## How to Use

1. **Install dependencies**:
   ```bash
   pip install selenium pandas
   ```

2. **Ensure ChromeDriver is installed** and added to your system path.

3. **Place JavaScript helper files** inside the `javascripts/` folder.

4. **Run the script**:
   ```bash
   python WebScraper.py
   ```

## Output

The scraper generates a file named `immobilien.csv` with the following columns:
- PostalCode
- Price
- Area
- Type

## Notes

- Currently configured to scrape data from `https://www.immobilienscout24.de/`
- Can be extended easily by modifying postal codes or property types in the script
- Designed and completed within 5 hours for fast, scalable data collection
