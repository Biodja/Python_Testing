from flask import Flask,render_template,request,redirect,flash,url_for
import helper1 as HELPER


app = Flask(__name__)
app.secret_key = 'something_special'

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/showSummary", methods=["POST"])
def show_summary():
    selected_club = HELPER.get_club_by_mail(mail=request.form["email"])
    if selected_club is None:
        print("pas trouvé !")
        flash("Sorry, that email wasn't found !!")
        return render_template("index.html")

    

    if selected_club :

        HELPER.USER_CLUB = selected_club
        print("trouvé !")
        return render_template(
            "welcome.html",
            club=HELPER.USER_CLUB,
            competitions=HELPER.COMPETITIONS,
        )

    flash("Email address not found")
    return render_template("index.html")



@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])
    competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
    flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions)


# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))