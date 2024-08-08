# Demo: Incorporating Model Navigator into Flask App

This is a short demo that shows how to pull in a static 
[model navigator](https://github.com/majensen/model-navigator-standalone)
bundled JS library into a [Flask](https://flask.palletsprojects.com/) Python
app via a template, and make it do something.

This repo contains the [Webpack](https://webpack.js.org) bundled JS, CSS, 
and images in [/python/src/static](/python/src/static).

The template [got_js.html](/python/src/templates/got_js.html) loads the
bundle in the `<script>` tag at line 4. 

The bundle makes the object `modelNavigator` available to the browser.
The `<button>` at line 8 sets the `onClick` event handler to run the
`modelNavigator.placeNavigator()` function. 

* The first argument is a string, the `id` of the HTML element in 
which to place the navigator. 

* The second argument is an array of urls to the MDF files of the 
model to display.

When the button is clicked, the navigator app should appear in the
`<div>` element at line 16.

## Install

```shell
git clone https://github.com/majensen/flask-js
cd flask-js
pip install poetry
poetry install
```

## Run 

```shell
cd python/src
poetry run flask --app flaskjs.py
```

View at http://localhost:5000 .

