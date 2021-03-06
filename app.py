"""Flask Application"""

# load libraries
from flask import Flask, jsonify

# load modules
from endpoints.producto import producto
from endpoints.swagger import swagger_ui_blueprint, SWAGGER_URL


# init Flask app
app = Flask(__name__)

# register blueprints. ensure that all paths are versioned!
app.register_blueprint(producto, url_prefix="/api/v1/producto")
app.config.from_pyfile('settings.py')

from api_spec import spec

with app.test_request_context():
    # register all swagger documented functions here
    for fn_name in app.view_functions:
        if fn_name == 'static':
            continue
        print(f"Loading swagger docs for function: {fn_name}")
        view_fn = app.view_functions[fn_name]
        spec.path(view=view_fn)


@app.route("/api/swagger.json")
def create_swagger_spec():
    return jsonify(spec.to_dict())

app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == "__main__":
    ####################
    # FOR DEVELOPMENT
    ####################
    # initialize_app(app)
    app.run(host='0.0.0.0', debug=True)