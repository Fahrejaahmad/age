from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    web_title = "halaman utama"
    return render_template('home.html', web_title=web_title)
@app.route("/about")
def about():
    web_title = "halaman about"
    return render_template('about.html',web_title=web_title)
@app.route('/usia', methods=['GEt','POST'])
def cek_usia():
    if request.method == 'POST':
      tahun_lahir = int(request.form['tahun_lahir'])
      tahun_sekarang = 2024
      usia = tahun_sekarang - tahun_lahir
      print(usia)
      return render_template('cek_usia.html', usia=usia)
    return render_template('cek_usia.html', usia=None)

if __name__ == '__main__':
    app.run(debug=True,port=1111)