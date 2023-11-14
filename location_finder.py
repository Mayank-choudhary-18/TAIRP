from geopy.geocoders import Nominatim
import tkinter as tk
from tkinter import messagebox

def find_location():
    address = entry.get()
    
    try:
        geolocator = Nominatim(user_agent="location_finder")
        location = geolocator.geocode(address)
        
        if location is not None:
            latitude = location.latitude
            longitude = location.longitude
            
            messagebox.showinfo("Location", f"Latitude: {latitude}\nLongitude: {longitude}")
        else:
            messagebox.showerror("Error", "Location not found!")
    
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create GUI interface for user input
root = tk.Tk()
root.title("Location Finder")

label = tk.Label(root, text="Enter address:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Find Location", command=find_location)
button.pack()

root.mainloop()