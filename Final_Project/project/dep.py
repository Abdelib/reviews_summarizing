from flask import Flask
import Copy_of_Summarize_reviews_1
import io
import random
from flask import render_template
import time
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

app = Flask(__name__, template_folder="/Users/abdelrahmanibrahim/Documents/Final_Project/project/static")

@app.route('/')
def displayResults():
    fig = Copy_of_Summarize_reviews_1.run_all()
    fig[1].savefig('/Users/abdelrahmanibrahim/Documents/Final_Project/project/static/images/new_plot.png')
    time.sleep(3)
    return render_template('untitled1.html',  tables=[fig[0].to_html(classes='data')], titles=fig[0].columns.values, name='new_plot', url='/static/images/new_plot.png')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True, threaded=True)
