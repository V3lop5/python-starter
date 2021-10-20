"""
This is the main file of project %name%.

It is invoked when someone runs python like:
    python -m %name%
"""
from counter.web import app


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
