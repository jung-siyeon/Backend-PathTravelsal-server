from flask import Flask, request, render_template, abort

app = Flask(__name__)

dir_name = "babo/"

@app.errorhandler(404)
def page_not_found(error):
   return render_template('404.html', title = '404'), 404

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_file', methods=["POST"])
def parse_request():
    try : 
        name = request.get_json()['name']
        f = open(dir_name+name, 'r')
        data = f.read() 
        f.close()   
        return data
    except:
        abort(404)
        

if __name__ == '__main__':
    app.run(debug=True)
