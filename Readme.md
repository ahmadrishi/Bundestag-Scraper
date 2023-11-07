# Bundestag Scraper

## Overview
The 'Bundestag Scraper' is a Python program designed to scrape information from the official website of the German Bundestag (Federal Parliament). It gathers data about the members of the Bundestag and stores it in a CSV file for further analysis or processing.

## Features
1. Web Scraping: The program uses web scraping techniques to extract data from the Bundestag website.
2. Concurrent Execution: It leverages Python's concurrent.futures module to run multiple scraping tasks concurrently, improving efficiency.
3. Error Handling: The program handles errors gracefully and records failed links in a separate text file.
4. API Integration: An external API (ScraperAPI) is integrated to retrieve data from websites, overcoming potential limitations like rate limiting and IP blocking.
5. Data Storage: The scraped information is stored in a CSV file, making it easy to work with and analyze the data.

## Methods
- `get_links()`: This method scrapes the Bundestag website to obtain links to individual member profiles. It extracts the links using libraries like BeautifulSoup and lxml.
- `get_info(link)`: This method is responsible for scraping the detailed information of a specific member. It uses an external API (ScraperAPI) to fetch the content of the member's profile page, extracts the name and biography using XPath, and stores the data in a CSV file. Error handling is employed to capture and log any failures.
- Concurrent Execution: The program reads a list of URLs from a file and utilizes the ThreadPoolExecutor to concurrently invoke the `get_info()` method on these URLs, allowing multiple member profiles to be scraped simultaneously.

## Technologies Used
- Python: The program is written in Python, a versatile and powerful programming language.
- BeautifulSoup: It utilizes the BeautifulSoup library for parsing and navigating the HTML content of the Bundestag website.
- lxml: The lxml library is used in conjunction with BeautifulSoup for more efficient HTML parsing.
- CSV: The program uses Python's built-in CSV module to create and write data to a CSV file.
- requests: The requests library is employed to make HTTP requests to the Bundestag website and external APIs.
- concurrent.futures: This library is used for concurrent execution of scraping tasks, enhancing performance.
- ScraperAPI: An external API service is integrated to overcome web scraping limitations, such as IP blocking or rate limiting.
- Error Handling: The program handles errors and logs failed links in a separate text file.
- Markup Language: This documentation is written in Markdown, a lightweight markup language for easy readability and formatting.

This 'Bundestag Scraper' program provides an efficient solution for collecting data about Bundestag members for various research or analysis purposes.
