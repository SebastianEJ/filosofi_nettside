from flask import render_template
from app import app

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',title="Home")

@app.route("/sokrates")
def sokrates():
    return render_template('sokrates.html', title="sokrates")

@app.route("/laeringstoeri")
def laeringstoeri():
    return render_template('laeringsteori.html', title="læringsteori")

@app.route("/allmenn_enkel")
def allmenn_enkel():
    return render_template('allmenn_enkel.html', title="allmennbegreper og enkeltting")

@app.route("/arsaker")
def arsaker():
    return render_template('arsaker.html', title="årsaksbegrepet")

@app.route("/bio_og_sosi_kjonn")
def bio_og_sosi_kjonn():
    return render_template('bio_og_sosi_kjonn.html', title="biologiske og sosiale kjønn")

@app.route("/bullshit")
def bullshit():
    return render_template('bullshit.html', title="Bullshit, politikk og uvitenhet")

@app.route("/evolusjon")
def evolusjon():
    return render_template('evolusjon.html', title="evolusjon")

@app.route("/fire_arsaker")
def fire_arsaker():
    return render_template('fire_arsaker.html', title="fire årsaker")

@app.route("/folelser_hinder_for_kunnskap")
def folelser_hinder_for_kunnskap():
    return render_template('folelser_hinder_for_kunnskap.html', title="følelser hinder for kunnskap")

@app.route("/gud")
def gud():
    return render_template('gud.html', title="finnes Gud")

@app.route("/hvorfor_noe")
def hvorfor_noe():
    return render_template('hvorfor_noe.html', title="hvorfor noe")

@app.route("/kunnskapsresistens")
def kunnskapsresistens():
    return render_template('kunnskapsresistens.html', title="kunnskapsresistens")

@app.route("/laeringsteori")
def laeringsteori():
    return render_template('laeringsteori.html', title="læringsteori")

@app.route("/platon")
def platon():
    return render_template('platon.html', title="platon")

@app.route("/pre_sokrates")
def pre_sokrates():
    return render_template('pre_sokrates.html', title="før sokratikerne")

@app.route("/realisme_idealisme")
def realisme_idealisme():
    return render_template('realisme_idealisme.html', title="realisme og idealisme")

@app.route("/rom_og_geometri")
def rom_og_geometri():
    return render_template('rom_og_geometri.html', title="rom og geometri")

@app.route("/sinnet_i_naturen")
def sinnet_i_naturen():
    return render_template('sinnet_i_naturen.html', title="sinnets plass i naturen")

@app.route("/tenk_selv")
def tenk_selv():
    return render_template('tenk_selv.html', title="tenk selv")

@app.route("/vaere")
def vaere():
    return render_template('vaere.html', title="væren")

@app.route("/virkeligheten")
def virkeligheten():
    return render_template('virkeligheten.html', title="virkeligheten")

@app.route("/vitenskapelig_metode")
def vitenskapelig_metode():
    return render_template('vitenskapelig_metode.html', title="vitenskapelig metode")

@app.route("/aristoteles")
def aristoteles():
    return render_template('aristoteles.html', title="aristoteles")
