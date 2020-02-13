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


class Event_Cocktail(db.Model):
    """Data model for a type of liquor."""

    __tablename__ = "event_cocktails"

    event_cocktail_id = db.Column(db.Integer,
                                  autoincrement=True,
                                  nullable=False,
                                  primary_key=True)
    event_id = db.Column(db.Integer,
                         db.ForeignKey('events.event_id'),
                         nullable=False)
    cocktail_id = db.Column(db.Integer,
                            nullable = False)

    event = db.relationship("Event")

    def __repr__(self):
        """Return a human-readable representation of a Liquor."""

        return f'{self.event}'


class Event(db.Model):
    """Data model for a user's favorite cocktails."""

    __tablename__ = "events"

    event_id = db.Column(db.Integer,
                             autoincrement=True,
                             nullable=False,
                             primary_key=True)
    name = db.Column(db.String(25), nullable = False)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.user_id'),
                        nullable=False)

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