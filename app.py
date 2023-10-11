from flask import Flask, render_template, request

app = Flask(__name__)

counter = 0

@app.route("/image")
def image():
    global counter
    return render_template('image.html', counter=counter)

@app.route('/button', methods=['GET', 'POST'])
def button():
    global counter
    if request.method == 'POST':
        counter += 1
        counter %= 3
    return render_template('button.html')

if __name__ == '__main__':
    app.run(debug=True)





