from flask import Flask, render_template, render_template_string, url_for
app = Flask(__name__)

IMAGES = {
    "merchant": "ic_merchant-web.png", 
    "lr": "ic_longest_road-web.png",
    "green_metropolis": "ic_green_metropolis-web.png",
    "yellow_metropolis": "ic_yellow_metropolis-web.png",
    "blue_metropolis": "ic_blue_metropolis-web.png"
}

class Player:
    def __init__(self, i):
        self.name = "Player {0}".format(i)
        self.score = 0
        self.images = ['merchant', 'lr', 'blue_metropolis']

    def get_images(self):
        for image in self.images:
            link=url_for('static', filename='images/{0}'.format(IMAGES[image]))
            print(link)
            yield link


@app.route("/")
def render_homepage():
    n_players = 4
    players = [Player(i+1) for i in range(n_players)]
    return render_template('template.html', players=players)


if __name__ == '__main__':
    app.run(debug=True)
