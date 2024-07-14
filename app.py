from flask import Flask, render_template, request

app = Flask(__name__)

outfits = {
    "happy": [
        {"name": "Blue Dress", "url": "https://www.myntra.com/blue-dress"},
        {"name": "Yellow Top", "url": "https://www.myntra.com/yellow-top"},
        {"name": "Floral Skirt", "url": "https://www.myntra.com/floral-skirt"}
    ],
    "energetic": [
        {"name": "White Sneakers", "url": "https://www.myntra.com/white-sneakers"},
        {"name": "Sporty Tracksuit", "url": "https://www.myntra.com/sporty-tracksuit"},
        {"name": "Running Shorts", "url": "https://www.myntra.com/running-shorts"}
    ],
    "elegant": [
        {"name": "Red Heels", "url": "https://www.myntra.com/red-heels"},
        {"name": "Black Evening Gown", "url": "https://www.myntra.com/black-evening-gown"},
        {"name": "Pearl Necklace", "url": "https://www.myntra.com/pearl-necklace"}
    ],
    "chic": [
        {"name": "Checked Blazer", "url": "https://www.myntra.com/checked-blazer"},
        {"name": "High-Waist Trousers", "url": "https://www.myntra.com/high-waist-trousers"},
        {"name": "Silk Scarf", "url": "https://www.myntra.com/silk-scarf"}
    ],
    "traditional": [
        {"name": "Blue Kurta", "url": "https://www.myntra.com/blue-kurta"},
        {"name": "Gold Bangles", "url": "https://www.myntra.com/gold-bangles"},
        {"name": "Embroidered Dupatta", "url": "https://www.myntra.com/embroidered-dupatta"}
    ],
    "relaxed": [
        {"name": "Grey Hoodie", "url": "https://www.myntra.com/grey-hoodie"},
        {"name": "Comfy Sweatpants", "url": "https://www.myntra.com/comfy-sweatpants"},
        {"name": "Slip-On Shoes", "url": "https://www.myntra.com/slip-on-shoes"}
    ],
    "confident": [
        {"name": "Black Blazer", "url": "https://www.myntra.com/black-blazer"},
        {"name": "Leather Boots", "url": "https://www.myntra.com/leather-boots"},
        {"name": "Statement Necklace", "url": "https://www.myntra.com/statement-necklace"}
    ],
    "adventurous": [
        {"name": "Cargo Pants", "url": "https://www.myntra.com/cargo-pants"},
        {"name": "Hiking Boots", "url": "https://www.myntra.com/hiking-boots"},
        {"name": "Utility Jacket", "url": "https://www.myntra.com/utility-jacket"}
    ],
    "romantic": [
        {"name": "Lace Dress", "url": "https://www.myntra.com/lace-dress"},
        {"name": "Rose Gold Ring", "url": "https://www.myntra.com/rose-gold-ring"},
        {"name": "Heart-Shaped Earrings", "url": "https://www.myntra.com/heart-shaped-earrings"}
    ],
    "professional": [
        {"name": "Grey Suit", "url": "https://www.myntra.com/grey-suit"},
        {"name": "Oxford Shoes", "url": "https://www.myntra.com/oxford-shoes"},
        {"name": "Leather Briefcase", "url": "https://www.myntra.com/leather-briefcase"}
    ]
}

@app.route("/", methods=["GET", "POST"])
def index():
    selected_mood = None
    mood_outfits = []

    if request.method == "POST":
        selected_mood = request.form.get("mood")
        mood_outfits = outfits.get(selected_mood, [])

    return render_template("index.html", outfits=mood_outfits, selected_mood=selected_mood)

if __name__ == "__main__":
    app.run(debug=True)
