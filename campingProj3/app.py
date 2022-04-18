from flask import Flask, render_template
import routes.camping_route as cr
import camping.service as service
app = Flask(__name__)

app.register_blueprint(cr.bp)
cser = service.CampingService()

@app.route('/')
def root():
    pageNo = 1
    clist = cser.getCamping(pageNo)
    return render_template('index.html', clist=clist, pageNo=pageNo)

if __name__ == '__main__':
    app.run(port=5001)













