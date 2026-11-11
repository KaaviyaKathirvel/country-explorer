import requests

def fetch_countries():
    url = "https://countries.dev/countries"

    try:
        response = requests.get(url)
        response.raise_for_status()

        countries = response.json()
        return countries
    
    except requests.exceptions.JSONDecodeError:
        print("The API returned invalid JSON data.")
        return []

    except requests.exceptions.RequestException:
        print("Unable to retrieve country data.")
        return []

def display_countries(countries):
    for country in countries:
        capital = country.get("capital") or "Not available"
        population = country.get("population")
        if population is not None:
            population = f"{population:,}"
        else:
            population = "Not available"
        region = country.get("region") or "Not available"
        area = country.get("area")
        if area is not None:
            area = f"{area:,}"
        else:
            area = "Not available"
        print(f"Country: {country.get('name')} | Capital: {capital} | Population: {population} | Region: {region} | Area: {area}")

def search_country(countries, search_term):
    search_term_lower = search_term.lower()
    matching_countries = []
    for country in countries:
        if search_term_lower == country.get("name", "").lower():
            matching_countries.append(country)
    return matching_countries

def run_country_search(countries):
    search_term = input("Enter a country name to search: ")
    search_term = search_term.strip()
    if not search_term:
        print("Please enter a country name.")
        return

    results = search_country(countries, search_term)

    if results:
        display_countries(results)
    else:
        print("No matching countries found.")

def filter_by_region(countries, region):
    region_term_lower = region.lower()
    matching_countries = []
    for country in countries:
        if region_term_lower == country.get("region", "").lower():
            matching_countries.append(country)
    return matching_countries

def run_region_filter(countries):
    region = input("Enter a region (Asia, Africa, Europe, Americas, Oceania, Polar): ")
    region = region.strip()
    if not region:
        print("Please enter a region name.")
        return

    results = filter_by_region(countries, region)

    if results:
        display_countries(results)
    else:
        print("No countries found in this region.")

def top_five_by_population(countries):
    sorted_countries = sorted(countries, key=lambda country: country.get("population", 0), reverse=True)
    return sorted_countries[:5]

def run_top_five(countries):
    results = top_five_by_population(countries)
    print("Top 5 Most Populous Countries")
    for rank, country in enumerate(results, start=1):
        print(rank, country.get("name"), f"{country.get('population'):,}")

def compare_countries(countries, country1, country2):
    country1_data = search_country(countries, country1)
    country2_data = search_country(countries, country2)

    if not country1_data or not country2_data:
        print("One or both countries not found.")
        return
    country1_info = country1_data[0]
    country2_info = country2_data[0]

    population1 = country1_info.get("population")
    population2 = country2_info.get("population")
    if population1 is not None:
        population1 = f"{population1:,}"
    else:
        population1 = "Not available"

    if population2 is not None:
        population2 = f"{population2:,}"
    else:
        population2 = "Not available"
        
    area1 = country1_info.get("area")
    area2 = country2_info.get("area")
    if area1 is not None:
        area1 = f"{area1:,}"
    else:
        area1 = "Not available"

    if area2 is not None:
        area2 = f"{area2:,}"
    else:
        area2 = "Not available"

    print(f"\nComparison: {country1_info.get('name')} vs {country2_info.get('name')}")
    print(f"Name: {country1_info.get('name')} | {country2_info.get('name')}")
    print(f"Capital: {country1_info.get('capital')} | {country2_info.get('capital')}")
    print(f"Population: {population1} | {population2}")
    print(f"Region: {country1_info.get('region')} | {country2_info.get('region')}")
    print(f"Area: {area1} | {area2}")

def run_country_comparison(countries):
    country1 = input("Enter the first country name: ").strip()
    country2 = input("Enter the second country name: ").strip()

    if not country1 or not country2:
        print("Please enter both country names.")
        return
    compare_countries(countries, country1, country2)

def main_menu(countries):
    while True:
        print("\nWelcome to Country Explorer!")
        print("1. Search for a country")
        print("2. Filter countries by region")
        print("3. View top 5 most populous countries")
        print("4. Compare two countries")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            run_country_search(countries)
        elif choice == "2":
            run_region_filter(countries)
        elif choice == "3":
            run_top_five(countries)
        elif choice == "4":
            run_country_comparison(countries)
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

def main():
    print("Welcome to Country Explorer!")
    countries = fetch_countries()

    if not countries:
        print("No country data available. Exiting.")
        return

    print(f"Total countries retrieved: {len(countries)}")
    main_menu(countries)

if __name__ == "__main__":
    main()