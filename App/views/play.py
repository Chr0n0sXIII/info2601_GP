
@auth_views.route('/play')
def play_page():
    return render_template("play.html")