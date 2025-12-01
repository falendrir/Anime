import requests
import time
import csv

def scrape_manga_details(manga_id):
    base_url = "https://api.mangadex.org"

    # Fetch manga statistics from the API
    stats_response = requests.get(f"{base_url}/statistics/manga/{manga_id}")
    if stats_response.status_code != 200:
        print(f"Failed to fetch manga statistics. Status code: {stats_response.status_code}")
        return None

    stats_data = stats_response.json()
    manga_stats = stats_data["statistics"].get(manga_id, {})

    # Extract rating and follows
    rating = manga_stats.get("rating", {}).get("average", "Not found")
    follows = manga_stats.get("follows", "Not found")

    # Fetch manga details from the API
    manga_response = requests.get(f"{base_url}/manga/{manga_id}")
    if manga_response.status_code != 200:
        print(f"Failed to fetch manga details. Status code: {manga_response.status_code}")
        return None

    manga_data = manga_response.json()
    manga_attributes = manga_data.get("data", {}).get("attributes", {})

    # Extract title, description, tags, and publication year
    title = manga_attributes.get("title", {}).get("en", "Not found")
    description = manga_attributes.get("description", {}).get("en", "Not found")
    tags = [tag["attributes"]["name"]["en"] for tag in manga_attributes.get("tags", []) if "en" in tag["attributes"]["name"]]
    year = manga_attributes.get("year", "Not found")

    # Compile all details
    manga_details = {
        "name": title,
        "description": description,
        "tags": ", ".join(tags),
        "rating": rating,
        "followers": follows,
        "year": year
    }

    return manga_details

def fetch_all_manga_details(limit=100, output_file="manga_details.csv"):
    base_url = "https://api.mangadex.org/manga"
    offset = 0
    all_manga_details = []

    # Open the CSV file for writing
    with open(output_file, mode="w", newline="", encoding="utf-8") as csv_file:
        fieldnames = ["name", "description", "tags", "rating", "followers", "year"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        while True:
            # Fetch a page of manga
            params = {
                "limit": limit,
                "offset": offset,
            }
            response = requests.get(base_url, params=params)

            # Debugging output
            print(f"Fetching: {response.url}")

            if response.status_code != 200:
                print(f"Failed to fetch manga. Status code: {response.status_code}")
                print(f"Response content: {response.text}")
                break

            data = response.json()
            if not data.get("data"):
                print("No more manga found.")
                break

            # Fetch details for each manga
            for manga in data["data"]:
                manga_id = manga["id"]
                print(f"Fetching details for Manga ID: {manga_id}")
                details = scrape_manga_details(manga_id)
                if details:
                    writer.writerow(details)
                    all_manga_details.append(details)

            # Check if there's more manga to fetch
            total_manga = data["total"]
            offset += limit
            if offset >= total_manga:
                break

            # To avoid hitting rate limits, add a delay
            time.sleep(1)

    print(f"Details saved to {output_file}")
    return all_manga_details

def test_single_manga(manga_id):
    print(f"Testing single manga ID: {manga_id}")
    details = scrape_manga_details(manga_id)
    if details:
        print("Manga Details:")
        for key, value in details.items():
            print(f"{key.capitalize()}: {value}")
    else:
        print("Failed to retrieve manga details.")

# Example usage
if __name__ == "__main__":
    choice = input("Do you want to test a single manga ID or fetch all manga? (single/all): ").strip().lower()
    if choice == "single":
        manga_id = input("Enter the MangaDex manga ID: ").strip()
        test_single_manga(manga_id)
    elif choice == "all":
        all_details = fetch_all_manga_details()
        print(f"Total manga details fetched: {len(all_details)}")
    else:
        print("Invalid choice. Please enter 'single' or 'all'.")