from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """Data model for a user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        nullable=False,
                        primary_key=True)
    fname = db.Column(db.String(25), nullable=False)
    lname = db.Column(db.String(25), nullable=False)
    username = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(25), nullable=False)
    password = db.Column(db.String(25), nullable=False)

    def __repr__(self):
        """Return a human-readable representation of a User"""

        return f'<First: {self.fname}, Last: {self.lname}>'

class Liquor(db.Model):
    """Data model for a type of liquor."""

    __tablename__ = "liquors"

    liquor_id = db.Column(db.Integer,
                          autoincrement=True,
                          nullable=False,
                          primary_key=True)
    name = db.Column(db.String(25), nullable=False)

    def __repr__(self):
        """Return a human-readable representation of a Liquor."""

        return f'{self.name}'


class Cocktail(db.Model):
    """Data model for a cocktail."""

    __tablename__ = "cocktails"

    cocktail_id = db.Column(db.Integer,
                            autoincrement=True,
                            nullable=False,
                            primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    liquor_id = db.Column(db.Integer,
                          db.ForeignKey('liquors.liquor_id'),
                          nullable=False)
    ingredients = db.Column(db.String(50), nullable=False)
    recipe = db.Column(db.String(100), nullable=False)

    liquor = db.relationship("Liquor")


    def __repr__(self):
        """Return a human-readable representation of a Cocktail."""

        return f'{self.name}'


class Event(db.Model):
    """Data model for a user's favorite cocktails."""

    __tablename__ = "events"

    event_id = db.Column(db.Integer,
                             autoincrement=True,
                             nullable=False,
                             primary_key=True)
    cocktail_id = db.Column(db.Integer,
                            db.ForeignKey('cocktails.cocktail_id'),
                            nullable=False)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.user_id'),
                        nullable=False)

    cocktail = db.relationship("Cocktail")
    user = db.relationship("User")

    def __repr__(self):
        """Return a human-readable representation of a favorite cocktail."""

        return f'Cocktail: {self.cocktail_id}'


def connect_to_db(app):
    """Connect the database to my Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cocktails'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    print("Connected to DB.")