

from flask import Flask,render_template, request
import math
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/index.html")
def index():
    return render_template('index.html')

@app.route('/vucut.html')
def vucut():
    return render_template('vucut.html')


@app.route('/kilo.html')
def kilo():
    return render_template('kilo.html')


@app.route('/pilates.html')
def pilates():
    return render_template('pilates.html')

@app.route('/egzersiz.html')
def egzersiz():
    return render_template('egzersiz.html')

@app.route('/yiyecek.html')
def yiyecek():
    return render_template('yiyecek.html')

@app.route('/onlineKos.html')
def onlineKos():
    return render_template('onlineKos.html')

@app.route('/gallery.html')
def galleryHakkimizda():
    return render_template('gallery.html')

@app.route('/contact.html')
def contactIletsim():
    return render_template('contact.html')

@app.route('/giris.html')
def giris():
    return render_template('giris.html')


@app.route('/kayit.html')
def kayit():
    return render_template('kayit.html')

@app.route('/kol.html')
def kol():
    return render_template('kol.html')

@app.route('/bacak.html')
def bacak():
    return render_template('bacak.html')

@app.route('/karın.html')
def karın():
    return render_template('karın.html')

@app.route('/omuz_egzersiz.html')
def omuz():
    return render_template('omuz_egzersiz.html')

@app.route('/sirt_egzersiz.html')
def sirt():
    return render_template('sirt_egzersiz.html')


@app.route('/gogus_egzersiz.html')
def gogus():
    return render_template('gogus_egzersiz.html')

@app.route('/program.html')
def program():
    return render_template('program.html')

@app.route('/program1', methods=['POST'])
def islem():
    if request.method == 'POST':
        boy = int(request.form['boy'])
        kilo = int(request.form['basen'])
        boyun = int(request.form['boyun'])
        bel = int(request.form['bel'])
        cinsiyet = str(request.form['browser'])
        x=bel-boyun

        if cinsiyet== "Erkek":
            sonuc = float((495 / (1.0324 - 0.19077 * math.log10(x) + 0.15456 * math.log10(boy))) - 450)
            if sonuc >= 25:
                u="static/images/ifelse/erkekobez.jpg"
                u1="static/images/ifelse/diyeto.jpeg"
                return render_template("verileriGoster.html", sonuc=sonuc, kilo=kilo , u=u, u1=u1)
            elif sonuc >18 and sonuc <= 24:
                u = "static/images/ifelse/erkeknormal.jpg"
                u1 = "static/images/ifelse/diyet.png"
                return render_template("verileriGoster.html", sonuc=sonuc, kilo=kilo, u=u, u1=u1)
            elif sonuc >14 and sonuc <= 17:
                u = "static/images/ifelse/erkekfit.jpg"
                u1 = "static/images/ifelse/diyet.png"
                return render_template("verileriGoster.html", sonuc=sonuc, kilo=kilo, u=u, u1=u1)
            elif sonuc >6 and sonuc <= 13:
                u = "static/images/ifelse/erkeksporcu.jpg"
                u1 = "static/images/ifelse/diyet.png"
                return render_template("verileriGoster.html", sonuc=sonuc, kilo=kilo, u=u, u1=u1)
            else:
                u = "static/images/ifelse/erkeksporcu.jpg"
                return render_template("verileriGoster.html", sonuc=sonuc, kilo=kilo, u=u)
        elif cinsiyet=="Kadin":
            r=bel+kilo-boyun
            sonuc = float((495/(1.29579-0.35004*math.log10(r)+0.22100*math.log10(boy)))-450)
            if sonuc >= 32:
                u="static/images/ifelse/kadinobez.jpg"
                u1="static/images/ifelse/diyeto.jpeg"
                return render_template("verileriGoster.html", sonuc=sonuc, kilo=kilo , u=u, u1=u1)
            elif sonuc >25 and sonuc <= 31:
                u = "static/images/ifelse/kadinnormal.jpg"
                u1 = "static/images/ifelse/diyet.png"
                return render_template("verileriGoster.html", sonuc=sonuc, kilo=kilo, u=u, u1=u1)
            else:
                u1 = "static/images/ifelse/diyet.png"
                u = "static/images/ifelse/kadinnormal.jpg"
                return render_template("verileriGoster.html", sonuc=sonuc, kilo=kilo, u=u , u1=u1)
    else:
        return render_template("verileriGoster.html", hata="Formdan veri gelmedi!")
if __name__ == "__main__":
    app.run()