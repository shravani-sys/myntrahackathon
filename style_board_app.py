from flask import Flask, render_template

app = Flask(__name__)

# Sample data for style boards (you can replace this with your database or storage solution)
style_boards = {
    "summer_vibes": {
        "name": "Summer Vibes",
        "items": [
            {"id": 1, "name": "Blue Floral Dress", "image_url": "https://myntra.com/blue_floral_dress.jpg", "link": "https://myntra.com/blue_floral_dress"},
            {"id": 2, "name": "White Sneakers", "image_url": "https://myntra.com/white_sneakers.jpg", "link": "https://myntra.com/white_sneakers"}
        ]
    },
    "urban_chic": {
        "name": "Urban Chic",
        "items": [
            {"id": 3, "name": "Black Leather Jacket", "image_url": "https://myntra.com/black_leather_jacket.jpg", "link": "https://myntra.com/black_leather_jacket"}
        ]
    },
    "boho_chic": {
        "name": "Boho Chic",
        "items": [
            {"id": 4, "name": "Boho Maxi Dress", "image_url": "https://myntra.com/boho_maxi_dress.jpg", "link": "https://myntra.com/boho_maxi_dress"}
        ]
    },
    "formal_wear": {
        "name": "Formal Wear",
        "items": [
            {"id": 5, "name": "Formal Suit", "image_url": "https://myntra.com/formal_suit.jpg", "link": "https://myntra.com/formal_suit"}
        ]
    }
}

# Home route
@app.route('/')
def index():
    return render_template('index.html', style_boards=style_boards)

# Style board detail route
@app.route('/style_board/<board_id>')
def style_board(board_id):
    board = style_boards.get(board_id)
    if board:
        return render_template('style_board.html', board=board)
    return "Style board not found", 404

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
