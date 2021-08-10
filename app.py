from flask_sqlalchemy import SQLAlchemy

from run import create_app


app, db , api= create_app("settings")


if __name__ == "__main__":
    app.run(debug=True)
