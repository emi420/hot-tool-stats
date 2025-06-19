# HOT Product Stats

This is a Streamlit application that fetches and displays statistics related to HOT (Humanitarian OpenStreetMap Team) products.
The application allows users to select a date range and then copy&paste Id, Name and Product name directly from a spreadsheet table, receiving corresponding data from Matomo and/or Other sources.

https://hot-tool-stats.streamlit.app

## Prerequisites

Before running the application, make sure you have the following dependencies installed:

- Python 3.x
- pandas
- streamlit
- requests

You can install the required Python packages using pip:
```bash
pip install pandas streamlit requests
```

## Start

```bash
streamlit run streamlit_app.py
```

This will start the Streamlit server and open the application in your default web browser.

## Using the Application

1. **Date and Time Range**: Select the start and end dates for the desired date range.

2. **Table**: Input Id, Name and Product name (required). You can copy&paste your data directly from a spreadsheet table.

3. **Get Statistics**: Click the "Get Statistics" button to fetch the data from the APIs based on the selected options.

The application will display two sections:

- **Summary**: This section shows a summary of the data for the selected options.

## Contributing

Contributions to improve the application are welcome. If you find any issues or have suggestions for enhancements, please open an issue or submit a pull request.

## Authors 

Emilio Mariscal, based on the [HOT Priority Regions and Impact Areas Stats](https://github.com/kshitijrajsharma/ohsome-now-stats-multiple-hashtags) app by Kshitij Raj Sharma.

