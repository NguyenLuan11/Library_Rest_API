from library import _init_

if __name__ == "__main__":
    app = _init_.create_app()
    app.run(debug=True)

