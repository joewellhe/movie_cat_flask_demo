from application import app


@app.errorhandler(404)
def error_404(e):
    return "opps 404"

