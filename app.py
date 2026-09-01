from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "totem_pole_creations_secret_key"

@app.route('/sitemap.xml')
def sitemap():
    pages = [
        'https://totempolecreations.in/',
        'https://totempolecreations.in/about',
        'https://totempolecreations.in/services',
        'https://totempolecreations.in/contact'
        'https://totempolecreations.in/portfolio'
        'https://totempolecreations.in/projects'
        'https://totempolecreations.in/enquiry'
    ]

    xml = '<?xml version="1.0" encoding="UTF-8"?>'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'

    for page in pages:
        xml += f'''
        <url>
            <loc>{page}</loc>
        </url>
        '''

    xml += '</urlset>'

    return xml, 200, {'Content-Type': 'application/xml'}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/mission")
def mission():
    return render_template("mission.html")

@app.route("/vision")
def vision():
    return render_template("vision.html")

@app.route("/milestones")
def milestones():
    return render_template("milestones.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/services/graphic-designing")
def service_graphic():
    return render_template("service_graphic.html")

@app.route("/services/printing")
def service_printing():
    return render_template("service_printing.html")

@app.route("/services/fabrication")
def service_fabrication():
    return render_template("service_fabrication.html")

@app.route("/services/construction")
def service_construction():
    return render_template("service_construction.html")

@app.route("/services/electrical")
def service_electrical():
    return render_template("service_electrical.html")

@app.route("/services/plumbing")
def service_plumbing():
    return render_template("service_plumbing.html")

@app.route("/contacts")
def contacts():
    return render_template("contacts.html")

@app.route("/get-in-touch", methods=["GET", "POST"])
def enquiry():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        message = request.form.get("message")
        # Inga contact form data processing or DB storage seyyalam
        flash("Thank you for reaching out! We will get in touch shortly.", "success")
        return redirect(url_for("enquiry"))
    return render_template("enquiry.html")

if __name__ == "__main__":
    app.run(debug=True)