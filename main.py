# flask import datetime with single file
import re
from flask import Flask,request,redirect,url_for
import datetime as dt 

app = Flask(__name__)


@app.route("/")
def waktu():
    waktu_sekarang = dt.date.today()
    return f"""
<!DOCTYPE html>
    <html>
    <head>
    <title>Tanggal Lahir Hari Ini</title>
    
    <style type="text/css">
    
    :root {{
    --clr-light-gray: #f7f7f7;
    --clr-medium-gray: #ccc;
    --clr-dark-text: #333;
    --clr-primary-btn: #2c3e50;
    --clr-primary-btn-hover: blueviolet;
    --clr-box-shadow: rgba(0, 0, 0, 0.1);
}}

body {{
    background-color: var(--clr-light-gray); 
    color: var(--clr-dark-text);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    padding: 40px;
    line-height: 1.6;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    min-height: 100vh;
    justify-content: center;
    overflow-x: hidden;
}}

h1 {{
    color: var(--clr-primary-btn);
    margin-bottom: 5px;
    opacity: 0;
    animation: fadeInDown 1s ease-out 0.2s forwards;
}}

p {{
    font-size: 1.1em;
    margin-bottom: 5px;
    color: #555;
    opacity: 0;
    animation: fadeIn 1s ease-out 0.4s forwards;
}}

p:last-of-type {{
    font-size: 1.8em;
    font-weight: bold;
    color: var(--clr-primary-btn);
    padding: 10px 20px;
    border: 1px solid var(--clr-medium-gray);
    border-radius: 5px;
    background-color: #fff;
    margin-top: 20px;
    margin-bottom: 40px;
    opacity: 0;
    animation: zoomIn 0.8s ease-out 1.2s forwards;
}}

img {{
    display: block;
    max-width: 80%;
    height: auto; 
    margin: 15px auto 10px auto; 
    border-radius: 8px;
    box-shadow: 0 6px 12px var(--clr-box-shadow);
    transition: transform 0.4s ease, box-shadow 0.4s ease;
    opacity: 0;
    animation: zoomIn 0.8s ease-out 0.8s forwards;
}}

img:hover {{
    transform: translateY(-3px);
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
}}

button {{
    background-color: var(--clr-primary-btn); 
    border: none;
    border-radius: 5px;
    padding: 0;
    margin-top: 20px;
    transition: background-color 0.3s ease;
    box-shadow: 0 4px 8px var(--clr-box-shadow);
    opacity: 0;
    animation: fadeInUp 1s ease-out 1.6s forwards;
}}

button a {{
    text-decoration: none;
    color: white;
    padding: 12px 25px;
    display: block;
    font-weight: bold;
    font-size: 1.0em;
}}

button:hover {{
    background-color: var(--clr-primary-btn-hover); 
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
}}

@keyframes fadeInDown {{
    0% {{ opacity: 0; transform: translateY(-20px); }}
    100% {{ opacity: 1; transform: translateY(0); }}
}}

@keyframes fadeInUp {{
    0% {{ opacity: 0; transform: translateY(20px); }}
    100% {{ opacity: 1; transform: translateY(0); }}
}}

@keyframes fadeIn {{
    0% {{ opacity: 0; }}
    100% {{ opacity: 1; }}
}}

@keyframes zoomIn {{
    0% {{ opacity: 0; transform: scale(0.8); }}
    100% {{ opacity: 1; transform: scale(1); }}
}}
</style>
    </head>
    <body>
   <h1>PYTHON DATETIME BERBASIS FLASK APP</h1>
    <hr>
    <p>Power By</p>
    <img src="static/flask.png" height="100" width="500">
    <p>Tanggal Sekarang Adalah</p>
    <p>{waktu_sekarang}</p>

<button>
<a href="{url_for('index2_hasil_jarak')}">Cek Jarak Tanggal Lahir Anda</a>
</button>
Atau
<button>
<a href="{url_for('hasil_umur_user')}">Cek Berapa Umur Anda Sekarang</a>
</button>

    </body>
    </html>

  """

# INPUT TANGGAL LAHIR LALU HASIL NYA AKAN KE RUTE HASIL_JARAK_INPUT
@app.route('/index2',methods=["GET","POST"])
def index2_hasil_jarak():
        waktu_sekarang = dt.date.today()
        if request.method == 'POST':
            tahun = int(request.form['Tahun']) 
            bulan = int(request.form['Bulan'])
            tanggal = int(request.form['Tanggal'])

            full_data = dt.date(tahun,bulan,tanggal) 
            data_jarak = waktu_sekarang - full_data
            return redirect(url_for("hasil_jarak_input",data_jarak=data_jarak,tahun=tahun,bulan=bulan,tanggal=tanggal,waktu_sekarang=waktu_sekarang))
            # mengirim data_jarak,tahun,bulan,tanggal,waktu_sekarang ke rute hasil_jarak beserta data lahir 
        
        return f"""
    <!DOCTYPE html>
    <html>
    <head><title>Input Tanggal Lahir</title></head>
    
    <style type="text/css">
     :root {{
    --clr-light-gray: #f7f7f7;
    --clr-medium-gray: #ccc;
    --clr-dark-text: #333;
    --clr-box-shadow: rgba(0, 0, 0, 0.1);

    --clr-primary-btn: #2c3e50;
    --clr-primary-btn-hover: blueviolet;

    --clr-content-bg: #ffffff;
    --animation-duration: 1s;
}}

/* ===============================
   BODY (❗ TANPA FLEX)
================================ */
body {{
    background-color: var(--clr-light-gray);
    color: var(--clr-dark-text);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    padding: 20px;
    line-height: 1.6;
    overflow-x: hidden;
    text-align: center;
}}

/* ===============================
   HEADINGS
================================ */
h1 {{
    color: var(--clr-primary-btn);
    opacity: 0;
    animation: fadeInDown var(--animation-duration) ease-out 0.2s forwards;
}}

h2 {{
    color: #666;
    font-weight: normal;
    font-size: 1.1em;
    margin: 10px auto 20px auto;
    opacity: 0;
    animation: fadeInDown var(--animation-duration) ease-out 0.4s forwards;
}}

/* ===============================
   HR
================================ */
hr {{
    border: 0;
    height: 1px;
    background-color: var(--clr-medium-gray);
    margin: 25px auto;
    width: 100%;
}}

/* ===============================
   DATE
================================ */
.current-date {{
    font-size: 1.1em;
    font-weight: 600;
    margin: 30px auto 20px auto;
    opacity: 0;
    animation: fadeInDown var(--animation-duration) ease-out 0.6s forwards;
}}

/* ===============================
   IMAGE
================================ */
img {{
    display: block;
    max-width: 80%;
    height: auto;
    margin: 15px auto 10px auto;
    border-radius: 8px;
    box-shadow: 0 6px 12px var(--clr-box-shadow);
    opacity: 0;
    animation: zoomIn 0.8s ease-out 0.8s forwards;
}}

/* ===============================
   FORM (PUSAT & RESPONSIF)
================================ */
form {{
    background-color: var(--clr-content-bg);
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0 4px 8px var(--clr-box-shadow);
    max-width: 400px;
    width: 100%;
    margin: 30px auto;
    opacity: 0;
    animation: fadeInUp var(--animation-duration) ease-out 0.8s forwards;
    text-align: center;
}}

/* ===============================
   INPUT
================================ */
input[type="number"] {{
    width: 100%;
    padding: 10px;
    margin: 8px auto 15px auto;
    border: 1px solid var(--clr-medium-gray);
    border-radius: 5px;
    box-sizing: border-box;
    text-align: center;
}}

/* ===============================
   BUTTON
================================ */
input[type="submit"] {{
    width: 100%;
    padding: 10px;
    background-color: var(--clr-primary-btn);
    color: white;
    border: none;
    border-radius: 5px;
}}

/* ===============================
   LINK BUTTON
================================ */
button {{
    background: none;
    border: none;
    padding: 0;
    width: 100%;
    margin-top: 15px;
}}

button a {{
    display: block;
    background-color: var(--clr-primary-btn);
    color: white;
    padding: 10px;
    border-radius: 5px;
    text-decoration: none;
}}

/* ===============================
   ANIMATION
================================ */
@keyframes fadeInDown {{
    from {{ opacity: 0; transform: translateY(-20px); }}
    to   {{ opacity: 1; transform: translateY(0); }}
}}

@keyframes fadeInUp {{
    from {{ opacity: 0; transform: translateY(20px); }}
    to   {{ opacity: 1; transform: translateY(0); }}
}}

@keyframes zoomIn {{
    from {{ opacity: 0; transform: scale(0.85); }}
    to   {{ opacity: 1; transform: scale(1); }}
}}

/* ===============================
   MOBILE
================================ */
@media (max-width: 600px) {{
    body {{
        padding: 10px;
    }}

    form {{
        padding: 20px;
    }}

    img {{
        max-width: 90%;
    }}
}}
    
    </style>
    <body>
    <h1>Input Tanggal Lahir Anda</h1>
     <hr>
     <h2>Program Mengecek Jarak Tanggal Lahir Dan Tanggal Sekarang Power By</h2>
     <img src="static/flask.png" height="100" width="500">
    <p>Hari Ini Tanggal : {waktu_sekarang}</p>
    <p>Silahkan Input Tanggal Lahir Anda Untuk Melihat Hasil Jarak Antara Tanggal Lahir Anda Dengan Hari Ini</p>
    
    <form method="POST">
    Masukan Tahun:<input type="number" name="Tahun"><br>
    Masukan Bulan:<input type="number" name="Bulan"><br>
    Masukan Tanggal:<input type="number" name="Tanggal"><br>
    <input type="submit" value="Kirim"> 
     <hr>
     <button>
     <a href="{url_for('hasil_umur_user')}">Cek Berapa Umur Anda Sekarang</a>
     </button>
    </form>
    </body>
    </html>
    """



# HASIL JARAK TANGGAL LAHIR HARI INI DAN TANGGAL HARI INI          
@app.route('/hasil_jarak')
def hasil_jarak_input():
   Tahun =  request.args.get('tahun') # hasil data dari rute index2 
   Bulan =  request.args.get('bulan') # ini 
   Tanggal =  request.args.get('tanggal') # dan ini juga
   Data_jarak = request.args.get('data_jarak') # dan ini dari index2 
   return f"""
    <!DOCTYPE html>
    <html>
    <head>
    <title>Hasil Input Tanggal Lahir</title>
    <style type="text/css">
    
    :root {{
    --clr-light-gray: #f7f7f7;
    --clr-medium-gray: #ccc;
    --clr-dark-text: #333;
    --clr-box-shadow: rgba(0, 0, 0, 0.1);

    --clr-primary-btn: #2c3e50;
    --clr-primary-btn-hover: blueviolet;

    --clr-content-bg: #ffffff;
    --animation-duration: 1s;
}}

/* ===============================
   BODY (❗ TANPA FLEX)
================================ */
body {{
    background-color: var(--clr-light-gray);
    color: var(--clr-dark-text);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    padding: 20px;
    line-height: 1.6;
    overflow-x: hidden;
    text-align: center;
}}

/* ===============================
   HEADINGS
================================ */
h1 {{
    color: var(--clr-primary-btn);
    opacity: 0;
    animation: fadeInDown var(--animation-duration) ease-out 0.2s forwards;
}}

h2 {{
    color: #666;
    font-weight: normal;
    font-size: 1.1em;
    margin: 10px auto 20px auto;
    opacity: 0;
    animation: fadeInDown var(--animation-duration) ease-out 0.4s forwards;
}}

/* ===============================
   HR
================================ */
hr {{
    border: 0;
    height: 1px;
    background-color: var(--clr-medium-gray);
    margin: 25px auto;
    width: 100%;
}}

/* ===============================
   DATE
================================ */
.current-date {{
    font-size: 1.1em;
    font-weight: 600;
    margin: 30px auto 20px auto;
    opacity: 0;
    animation: fadeInDown var(--animation-duration) ease-out 0.6s forwards;
}}

/* ===============================
   IMAGE
================================ */
img {{
    display: block;
    max-width: 80%;
    height: auto;
    margin: 15px auto 10px auto;
    border-radius: 8px;
    box-shadow: 0 6px 12px var(--clr-box-shadow);
    opacity: 0;
    animation: zoomIn 0.8s ease-out 0.8s forwards;
}}

/* ===============================
   FORM (PUSAT & RESPONSIF)
================================ */
form {{
    background-color: var(--clr-content-bg);
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0 4px 8px var(--clr-box-shadow);
    max-width: 400px;
    width: 100%;
    margin: 30px auto;
    opacity: 0;
    animation: fadeInUp var(--animation-duration) ease-out 0.8s forwards;
    text-align: center;
}}

/* ===============================
   INPUT
================================ */
input[type="number"] {{
    width: 100%;
    padding: 10px;
    margin: 8px auto 15px auto;
    border: 1px solid var(--clr-medium-gray);
    border-radius: 5px;
    box-sizing: border-box;
    text-align: center;
}}

/* ===============================
   BUTTON
================================ */
input[type="submit"] {{
    width: 100%;
    padding: 10px;
    background-color: var(--clr-primary-btn);
    color: white;
    border: none;
    border-radius: 5px;
}}

/* ===============================
   LINK BUTTON
================================ */
button {{
    background: none;
    border: none;
    padding: 0;
    width: 100%;
    margin-top: 15px;
}}

button a {{
    display: block;
    background-color: var(--clr-primary-btn);
    color: white;
    padding: 10px;
    border-radius: 5px;
    text-decoration: none;
}}

/* ===============================
   ANIMATION
================================ */
@keyframes fadeInDown {{
    from {{ opacity: 0; transform: translateY(-20px); }}
    to   {{ opacity: 1; transform: translateY(0); }}
}}

@keyframes fadeInUp {{
    from {{ opacity: 0; transform: translateY(20px); }}
    to   {{ opacity: 1; transform: translateY(0); }}
}}

@keyframes zoomIn {{
    from {{ opacity: 0; transform: scale(0.85); }}
    to   {{ opacity: 1; transform: scale(1); }}
}}

/* ===============================
   MOBILE
================================ */
@media (max-width: 600px) {{
    body {{
        padding: 10px;
    }}

    form {{
        padding: 20px;
    }}

    img {{
        max-width: 90%;
    }}
}}

    
    </style>
    </head>
    <body>
    <h1>Hasil Jarak Tanggal Lahir Anda Dan Tanggal Hari Ini</h1>
    <p>Anda Lahir Pada tahun {Tahun} Bulan {Bulan} Tanggal {Tanggal}</p>
    <p>Jarak Antara Tanggal Lahir Anda Dengan Tahun Sekarang {Data_jarak}</p>
    <button>
    <a href="{url_for('waktu')}">Kembali Ke Menu Awal?</a>
    </button>
    </body>
    </html>
    """
      
# HASIL UMUR
@app.route("/umur_user",methods=["GET","POST"])
def hasil_umur_user():
    hari_ini = dt.date.today()
    if request.method == "POST":
        tahun = int(request.form['Tahun'])
        bulan = int(request.form['Bulan'])
        tanggal = int(request.form['Tanggal'])
        
        full_data = dt.date(tahun,bulan,tanggal)
        jarak = hari_ini - full_data
        umur_anda = jarak.days // 365
        return redirect(url_for('Umur_user',umur_anda=umur_anda))  # mengirim data umur_anda ke rute hasil_umur
    return f""" 
        <!DOCTYPE html>
        <html>
        <head>
        <title>Hasil Umur Anda</title>
      <style type="text/css">
     :root {{
    --clr-light-gray: #f7f7f7;
    --clr-medium-gray: #ccc;
    --clr-dark-text: #333;
    --clr-box-shadow: rgba(0, 0, 0, 0.1);

    --clr-primary-btn: #2c3e50;
    --clr-primary-btn-hover: blueviolet;

    --clr-content-bg: #ffffff;
    --animation-duration: 1s;
}}

/* ===============================
   BODY (❗ TANPA FLEX)
================================ */
body {{
    background-color: var(--clr-light-gray);
    color: var(--clr-dark-text);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    padding: 20px;
    line-height: 1.6;
    overflow-x: hidden;
    text-align: center;
}}

/* ===============================
   HEADINGS
================================ */
h1 {{
    color: var(--clr-primary-btn);
    opacity: 0;
    animation: fadeInDown var(--animation-duration) ease-out 0.2s forwards;
}}

h2 {{
    color: #666;
    font-weight: normal;
    font-size: 1.1em;
    margin: 10px auto 20px auto;
    opacity: 0;
    animation: fadeInDown var(--animation-duration) ease-out 0.4s forwards;
}}

/* ===============================
   HR
================================ */
hr {{
    border: 0;
    height: 1px;
    background-color: var(--clr-medium-gray);
    margin: 25px auto;
    width: 100%;
}}

/* ===============================
   DATE
================================ */
.current-date {{
    font-size: 1.1em;
    font-weight: 600;
    margin: 30px auto 20px auto;
    opacity: 0;
    animation: fadeInDown var(--animation-duration) ease-out 0.6s forwards;
}}

/* ===============================
   IMAGE
================================ */
img {{
    display: block;
    max-width: 80%;
    height: auto;
    margin: 15px auto 10px auto;
    border-radius: 8px;
    box-shadow: 0 6px 12px var(--clr-box-shadow);
    opacity: 0;
    animation: zoomIn 0.8s ease-out 0.8s forwards;
}}

/* ===============================
   FORM (PUSAT & RESPONSIF)
================================ */
form {{
    background-color: var(--clr-content-bg);
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0 4px 8px var(--clr-box-shadow);
    max-width: 400px;
    width: 100%;
    margin: 30px auto;
    opacity: 0;
    animation: fadeInUp var(--animation-duration) ease-out 0.8s forwards;
    text-align: center;
}}

/* ===============================
   INPUT
================================ */
input[type="number"] {{
    width: 100%;
    padding: 10px;
    margin: 8px auto 15px auto;
    border: 1px solid var(--clr-medium-gray);
    border-radius: 5px;
    box-sizing: border-box;
    text-align: center;
}}

/* ===============================
   BUTTON
================================ */
input[type="submit"] {{
    width: 100%;
    padding: 10px;
    background-color: var(--clr-primary-btn);
    color: white;
    border: none;
    border-radius: 5px;
}}

/* ===============================
   LINK BUTTON
================================ */
button {{
    background: none;
    border: none;
    padding: 0;
    width: 100%;
    margin-top: 15px;
}}

button a {{
    display: block;
    background-color: var(--clr-primary-btn);
    color: white;
    padding: 10px;
    border-radius: 5px;
    text-decoration: none;
}}

/* ===============================
   ANIMATION
================================ */
@keyframes fadeInDown {{
    from {{ opacity: 0; transform: translateY(-20px); }}
    to   {{ opacity: 1; transform: translateY(0); }}
}}

@keyframes fadeInUp {{
    from {{ opacity: 0; transform: translateY(20px); }}
    to   {{ opacity: 1; transform: translateY(0); }}
}}

@keyframes zoomIn {{
    from {{ opacity: 0; transform: scale(0.85); }}
    to   {{ opacity: 1; transform: scale(1); }}
}}

/* ===============================
   MOBILE
================================ */
@media (max-width: 600px) {{
    body {{
        padding: 10px;
    }}

    form {{
        padding: 20px;
    }}

    img {{
        max-width: 90%;
    }}
}}
    
    </style>
     
       <body>
        <h1>Input Tanggal Lahir Anda</h1>
     <hr>
     <h2>Program Mengecek Berapa Umur Anda Power By</h2>
     <img src="static/flask.png" height="100" width="500">
    <p>Silahkan Input Tanggal Lahir Anda Untuk Melihat Berapa Umur Anda</p>
    
    <form method="POST">
    Masukan Tahun:<input type="number" name="Tahun"><br>
    Masukan Bulan:<input type="number" name="Bulan"><br>
    Masukan Tanggal:<input type="number" name="Tanggal"><br>
    <input type="submit" value="Kirim"> 
     <hr>
    <button>
<a href="{url_for('index2_hasil_jarak')}">Cek Jarak Antara Umur Anda Dan Hari Ini</a>
</button>
<button>
<a href="{url_for('waktu')}">Kembali Ke Menu Awal?</a>
</button>
        </body>
        </html>
        """

@app.route('/hasil_umur')
def Umur_user():
    umur_anda = request.args.get('umur_anda')
    return f"""
      <!DOCTYPE html>
        <html>
        <head>
        <title>Hasil Umur Anda</title>
         <style type="text/css">
    
    :root {{
    --clr-light-gray: #f7f7f7;
    --clr-medium-gray: #ccc;
    --clr-dark-text: #333;
    --clr-box-shadow: rgba(0, 0, 0, 0.1);

    --clr-primary-btn: #2c3e50;
    --clr-primary-btn-hover: blueviolet;

    --clr-content-bg: #ffffff;
    --animation-duration: 1s;
}}

/* ===============================
   BODY (❗ TANPA FLEX)
================================ */
body {{
    background-color: var(--clr-light-gray);
    color: var(--clr-dark-text);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    padding: 20px;
    line-height: 1.6;
    overflow-x: hidden;
    text-align: center;
}}

/* ===============================
   HEADINGS
================================ */
h1 {{
    color: var(--clr-primary-btn);
    opacity: 0;
    animation: fadeInDown var(--animation-duration) ease-out 0.2s forwards;
}}

h2 {{
    color: #666;
    font-weight: normal;
    font-size: 1.1em;
    margin: 10px auto 20px auto;
    opacity: 0;
    animation: fadeInDown var(--animation-duration) ease-out 0.4s forwards;
}}

/* ===============================
   HR
================================ */
hr {{
    border: 0;
    height: 1px;
    background-color: var(--clr-medium-gray);
    margin: 25px auto;
    width: 100%;
}}

/* ===============================
   DATE
================================ */
.current-date {{
    font-size: 1.1em;
    font-weight: 600;
    margin: 30px auto 20px auto;
    opacity: 0;
    animation: fadeInDown var(--animation-duration) ease-out 0.6s forwards;
}}

/* ===============================
   IMAGE
================================ */
img {{
    display: block;
    max-width: 80%;
    height: auto;
    margin: 15px auto 10px auto;
    border-radius: 8px;
    box-shadow: 0 6px 12px var(--clr-box-shadow);
    opacity: 0;
    animation: zoomIn 0.8s ease-out 0.8s forwards;
}}

/* ===============================
   FORM (PUSAT & RESPONSIF)
================================ */
form {{
    background-color: var(--clr-content-bg);
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0 4px 8px var(--clr-box-shadow);
    max-width: 400px;
    width: 100%;
    margin: 30px auto;
    opacity: 0;
    animation: fadeInUp var(--animation-duration) ease-out 0.8s forwards;
    text-align: center;
}}

/* ===============================
   INPUT
================================ */
input[type="number"] {{
    width: 100%;
    padding: 10px;
    margin: 8px auto 15px auto;
    border: 1px solid var(--clr-medium-gray);
    border-radius: 5px;
    box-sizing: border-box;
    text-align: center;
}}

/* ===============================
   BUTTON
================================ */
input[type="submit"] {{
    width: 100%;
    padding: 10px;
    background-color: var(--clr-primary-btn);
    color: white;
    border: none;
    border-radius: 5px;
}}

/* ===============================
   LINK BUTTON
================================ */
button {{
    background: none;
    border: none;
    padding: 0;
    width: 100%;
    margin-top: 15px;
}}

button a {{
    display: block;
    background-color: var(--clr-primary-btn);
    color: white;
    padding: 10px;
    border-radius: 5px;
    text-decoration: none;
}}

/* ===============================
   ANIMATION
================================ */
@keyframes fadeInDown {{
    from {{ opacity: 0; transform: translateY(-20px); }}
    to   {{ opacity: 1; transform: translateY(0); }}
}}

@keyframes fadeInUp {{
    from {{ opacity: 0; transform: translateY(20px); }}
    to   {{ opacity: 1; transform: translateY(0); }}
}}

@keyframes zoomIn {{
    from {{ opacity: 0; transform: scale(0.85); }}
    to   {{ opacity: 1; transform: scale(1); }}
}}

/* ===============================
   MOBILE
================================ */
@media (max-width: 600px) {{
    body {{
        padding: 10px;
    }}

    form {{
        padding: 20px;
    }}

    img {{
        max-width: 90%;
    }}
}}

    
    </style>
        </head>
        <h1>Hasil Umur Anda</h1>
        <p>Umur Anda Adalah {umur_anda}</p>
        <button>
<a href="{url_for('waktu')}">Kembali Ke Menu Awal?</a>
</button>
        </body>
        </html>
    """


if __name__=="__main__":
    app.run(debug=True)
