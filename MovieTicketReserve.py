import tkinter as tk
import sqlite3

# Database initialization
conn = sqlite3.connect("movies.db")
cur = conn.cursor()

# Create table if it doesn't exist
cur.execute("CREATE TABLE IF NOT EXISTS movies (movie_name TEXT, available_seats INTEGER)")

# Function to reserve tickets
def reserve_tickets():
    movie = movie_entry.get()
    seats = int(seats_entry.get())
    
    # Check if movie exists in the database
    cur.execute("SELECT * FROM movies WHERE movie_name=?", (movie,))
    result = cur.fetchone()
    
    if result:
        available_seats = result[1]
        if seats <= available_seats:
            updated_seats = available_seats - seats
            cur.execute("UPDATE movies SET available_seats=? WHERE movie_name=?", (updated_seats, movie))
            conn.commit()
            status_label.config(text="Tickets reserved successfully.")
        else:
            status_label.config(text="Not enough seats available.")
    else:
        status_label.config(text="Movie not found.")
        

# Function to display available movies
def display_movies():
    cur.execute("SELECT * FROM movies")
    movies = cur.fetchall()
    if movies:
        for movie in movies:
            print(movie)
    else:
        print("No movies available.")
        

# GUI initialization
root = tk.Tk()
root.title("Movie Ticket Reservation System")

# Movie Label and Entry
movie_label = tk.Label(root, text="Movie:")
movie_label.grid(row=0, column=0, padx=10, pady=10)
movie_entry = tk.Entry(root)
movie_entry.grid(row=0, column=1, padx=10, pady=10)

# Seats Label and Entry
seats_label = tk.Label(root, text="Seats:")
seats_label.grid(row=1, column=0, padx=10, pady=10)
seats_entry = tk.Entry(root)
seats_entry.grid(row=1, column=1, padx=10, pady=10)

# Reserve Button
reserve_button = tk.Button(root, text="Reserve Tickets", command=reserve_tickets)
reserve_button.grid(row=2, column=0, padx=10, pady=10)

# Display Button
display_button = tk.Button(root, text="Display Movies", command=display_movies)
display_button.grid(row=2, column=1, padx=10, pady=10)

# Status Label
status_label = tk.Label(root, text="")
status_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()

# Close database connection
conn.close()
