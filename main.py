from db import create_tables
from snippets import add_snippet, export_snippets_to_json, import_snippets_from_json, list_snippets, search_snippets

def main():
    create_tables()  # Ensure SQLite tables exist

    while True:
        print("\n1. Add Snippet")
        print("2. List Snippets")
        print("3. Search Snippets")
        print("4. Exit")
        print("5. Export Snippets to JSON")
        print("6. Import Snippets from JSON")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            snippet = {}
            snippet['title'] = input("Title: ").strip()
            snippet['description'] = input("Description: ").strip()
            snippet['code'] = input("Code:\n")
            snippet['language'] = input("Language: ").strip()
            snippet['category'] = input("Category: ").strip()
            snippet['tags'] = input("Tags (comma separated): ").strip().split(',')
            add_snippet(snippet)
            print("✅ Snippet added successfully!")

        elif choice == '2':
            list_snippets()

        elif choice == '3':
            query = input("Enter search query: ").strip()
            search_snippets(query)  # RapidFuzz search integrated in snippets.py

        elif choice == '4':
            print("Exiting...")
            break

        elif choice == '5':
            export_snippets_to_json()
            print("✅ Snippets exported successfully!")

        elif choice == '6':
            import_snippets_from_json()
            print("✅ Snippets imported successfully!")

        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
