from flask import Flask, request
from utils import calculateWR

app = Flask(__name__)

@app.route('/')
def result():
	game = request.args.get('game')
	deck = request.args.get('deck')
	wins = request.args.get('wins')
	losses = request.args.get('losses')

	return calculateWR(game, deck, wins, losses)

if __name__ == '__main__':
	app.run()
