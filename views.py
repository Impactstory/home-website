from flask import make_response
from flask import request
from flask import redirect
from flask import abort
from flask import render_template
from flask import jsonify
from flask import g

import json
import os
import sys

from app import app


#support CORS
@app.after_request
def add_crossdomain_header(resp):
    resp.headers['Access-Control-Allow-Origin'] = "*"
    resp.headers['Access-Control-Allow-Methods'] = "POST, GET, OPTIONS, PUT, DELETE, PATCH"
    resp.headers['Access-Control-Allow-Headers'] = "origin, content-type, accept, x-requested-with"

    # without this jason's heroku local buffers forever
    sys.stdout.flush()

    return resp


@app.before_request
def do_before_request():
    pass
    # if request.url.startswith("http://www.oadoi.org"):
    #
    #     new_url = request.url.replace(
    #         "http://www.oadoi.org",
    #         "http://oadoi.org"
    #     )
    #     return redirect(new_url, 301)  # permanent
    #
    # g.use_cache = True
    # if ('no-cache', u'') in request.args.items():
    #     g.use_cache = False
    #     print "NOT USING CACHE"










@app.route("/<path:page>")  # from http://stackoverflow.com/a/14023930/226013
@app.route("/")
def index_endpoint(path="index", page=""):

    homepage_slugs = [
        "",
        "press",
        "team",
        "about"
    ]
    if page.lower() in homepage_slugs:
        url = u"https://our-research.org/{}".format(page.strip())

    else:
        url = u"https://profiles.impactstory.org/{}".format(page.strip())

    return redirect(url, code=302)



@app.route("/log/install", methods=["POST"])
def log_install():
    return jsonify({"installed": True})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5010))
    app.run(host='0.0.0.0', port=port, debug=True, threaded=True)

















