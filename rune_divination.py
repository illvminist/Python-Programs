import random

# Define the runes and their meanings
runes = {
    'Fehu': 'Wealth, prosperity, abundance',
    'Uruz': 'Strength, health, energy',
    'Thurisaz': 'Conflict, catharsis, breakthrough',
    'Ansuz': 'Communication, wisdom, divine power',
    'Raido': 'Journey, movement, travel',
    'Kenaz': 'Knowledge, creativity, inspiration',
    'Gebo': 'Gift, partnership, generosity',
    'Wunjo': 'Joy, pleasure, harmony',
    'Hagalaz': 'Disruption, challenges, hail',
    'Nauthiz': 'Need, constraint, resistance',
    'Isa': 'Ice, stillness, blockage',
    'Jera': 'Harvest, reward, cycles',
    'Eihwaz': 'Defense, perseverance, yew tree',
    'Perthro': 'Mystery, chance, secrets',
    'Algiz': 'Protection, shield, guardian',
    'Sowilo': 'Success, vitality, the sun',
    'Tiwaz': 'Victory, honor, justice',
    'Berkano': 'Growth, fertility, birth',
    'Ehwaz': 'Movement, progress, horse',
    'Mannaz': 'Human, self, society',
    'Laguz': 'Water, intuition, flow',
    'Ingwaz': 'Fertility, new beginnings, Ing',
    'Dagaz': 'Breakthrough, awakening, day',
    'Othala': 'Inheritance, home, heritage'
}

def draw_rune():
    rune = random.choice(list(runes.keys()))
    meaning = runes[rune]
    return rune, meaning

def main():
    print("Welcome to the Elder Futhark Rune Divination!")
    input("Press Enter to draw a rune...")

    rune, meaning = draw_rune()

    print(f"\nYou drew the rune: {rune}")
    print(f"Meaning: {meaning}")

if __name__ == "__main__":
    main()