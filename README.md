# Country Explorer

A Python command-line application that retrieves live country information from the Countries API.

## Features

- **Search by country name:** Find a country using its exact name (case-insensitive).
- **Filter by region:** Display countries belonging to a selected region.
- **Top 5 most populous countries:** View the five countries with the largest populations.
- **Compare two countries:** Compare their names, capitals, populations, regions, and land areas.
- **Formatted output:** Display population and area values with thousands separators.
- **Error handling:** Handle API request failures, invalid JSON responses, empty input, invalid menu selections, and searches with no matching results.

## Technologies Used

- Python 3
- Requests library
- Countries API: https://countries.dev/countries

## Project Structure

```text
country-explorer/
├── main.py
├── requirements.txt
└── README.md
```

## Installation and Setup

1. Clone this repository:

   ```bash
   git clone <your-repository-url>
   ```

2. Navigate to the project directory:

   ```bash
   cd country-explorer
   ```

3. Create a virtual environment:

   ```bash
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   **macOS/Linux:**

   ```bash
   source venv/bin/activate
   ```

   **Windows:**

   ```bash
   venv\Scripts\activate
   ```

5. Install the required dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

## Running the Application

Run the following command from the project directory:

```bash
python main.py
```

The application retrieves country data from the API and displays a menu with five options:

1. Search for a country
2. Filter countries by region
3. View the top 5 most populous countries
4. Compare two countries
5. Exit

Select an option and follow the prompts to explore country information.

## Data Source

Country information is retrieved from the [Countries API](https://countries.dev/).

The application uses fields such as country name, capital, population, region, and area to provide its search, filtering, ranking, and comparison features.