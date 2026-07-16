from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()


app = Flask(__name__)


DB_HOST = os.getenv("POSTGRES_HOST", "localhost")

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql://{os.getenv('POSTGRES_USER')}:"
    f"{os.getenv('POSTGRES_PASSWORD')}@{DB_HOST}:5432/"
    f"{os.getenv('POSTGRES_DB')}"
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Contact(db.Model):
    __tablename__ = "contacts"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    company = db.Column(db.String(150), nullable=False)

    email = db.Column(db.String(120), nullable=False)

    message = db.Column(db.Text, nullable=False)

    created_at = db.Column(
        db.DateTime,
        default=db.func.current_timestamp()
    )


    def __repr__(self):
        return f"<Contact {self.name}>"

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    submitted = False


    if request.method == "POST":
    

        contact = Contact(
            name=request.form["name"],
            company=request.form["company"],
            email=request.form["email"],
            message=request.form["message"]
        )

        db.session.add(contact)
    

        db.session.commit()
        

        submitted = True

    return render_template("contact.html", submitted=submitted)
@app.route("/admin/contacts")
def admin_contacts():
    contacts = Contact.query.order_by(Contact.id).all()
    return render_template(
        "admin_contacts.html",
        contacts=contacts
    )
@app.route("/admin/contacts/<int:id>/edit", methods=["GET", "POST"])
def edit_contact(id):
    contact = Contact.query.get_or_404(id)

    if request.method == "POST":
        contact.name = request.form["name"]
        contact.company = request.form["company"]
        contact.email = request.form["email"]
        contact.message = request.form["message"]

        db.session.commit()

        return redirect("/admin/contacts")

    return render_template(
        "edit_contact.html",
        contact=contact
    )    
@app.route("/admin/contacts/<int:id>/delete", methods=["POST"])
def delete_contact(id):
    contact = Contact.query.get_or_404(id)

    db.session.delete(contact)
    db.session.commit()

    return redirect("/admin/contacts")    
    
with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
