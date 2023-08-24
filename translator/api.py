from flask import Flask, request, render_template
from googletrans import Translator
from form import TranslateForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "ashvehfeHUY12hcdhfuefhuujdbu d@@##cjide~"
translator = Translator()

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/translate',methods=["GET", "POST"])
def translate():
    form = TranslateForm()
    if request.method == "POST":
        source_lang = form.source_language.data
        target_lang = form.target_language.data
        text = form.text.data

        translation = translator.translate(text, src=source_lang, dest=target_lang)
        print(translation.text)
        return render_template("trans_page.html",tran = translation.text, form=form)                         
    return render_template("trans_page.html", form = form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

if __name__ == '__main__':
    app.run(debug=True)
