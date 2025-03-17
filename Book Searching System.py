import pandas as pd

def load_books(file_path='books.csv'):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print("Error: books.csv not found!")
        return None

def search_books(df):
    search_column = input("Search by (Title, Author, Genre, Publisher): ").strip()
    
    if search_column not in ["Title", "Author", "Genre", "Publisher"]:
        print("Invalid choice! Please choose from Title, Author, Genre, Publisher.")
        return
    
    if search_column == "Genre":
        options = ["signal_processing", "data_science", "mathematics", "economics", "history", "science", "psychology", "fiction", "computer_science", "nonfiction", "philosophy", "comic"]
    elif search_column == "Publisher":
        options = ["Wiley", "Penguin", "HarperCollins", "Springer", "Orient Blackswan", "CRC", "Apress", "Random House", "Bodley Head", "MIT Press", "O'Reilly", "HBA", "Rupa", "Transworld", "Pan", "Hyperion", "Pocket", "Mauj", "BBC", "Elsevier", "Pearson", "Prentice Hall", "TMH", "Picador", "vikas", "Routledge", "FreePress", "Jaico", "Vintage", "HighStakes", "Simon&Schuster", "Fontana", "Dell"]
    else:
        search_query = input(f"Enter {search_column} to search: ").strip()
        results = df[df[search_column].str.contains(search_query, case=False, na=False)]
        print(results if not results.empty else "No books found!")
        return
    
    print("Choose an option:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    try:
        choice = int(input("Enter the serial number: "))
        selected_value = options[choice - 1]
        results = df[df[search_column] == selected_value]
        print(results if not results.empty else "No books found!")
    except (ValueError, IndexError):
        print("Invalid selection!")

if __name__ == "__main__":
    books_df = load_books()
    if books_df is not None:
        search_books(books_df)
