import random

locations = [
    "Coogee Beach", "South Coogee", "Randwick", "Clovelly", "Bondi Junction", "Bondi Beach",
    "Maroubra", "Malabar", "Little Bay", "Newtown", "Alexandria", "Matraville", "Mascot",
    "Pagewood", "Kingsford", "Kensington", "Moore Park", "Redfern", "Surry Hills", "Central",
    "Haymarket", "Glebe", "Annandale", "Leichhardt", "Tempe", "Marrickville", "Darlinghurst",
    "Double Bay", "Rose Bay", "Vaucluse", "Watsons Bay", "Dover Heights", "Mascot", "Rosebery",
    "Botany", "Rockdale", "Royal Botanic Garden Sydney", "Barangaroo", "Town Hall", "The Rocks",
    "Circular Quay", "Pyrmont", "Johnstons Bay", "Darling Harbour", "Sydney Opera House",
    "Harbour Bridge"
]

selected_location = random.choice(locations)
print(f"Go to: {selected_location}")
