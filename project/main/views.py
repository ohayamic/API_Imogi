# project/main/views.py


from flask import render_template, Blueprint, redirect, url_for, jsonify
from .forms import SearchForm
#imported requests for accessing the url
import requests
import json

main_blueprint = Blueprint('main', __name__,)


@main_blueprint.route('/', methods=('GET', 'POST'))
def search():
    form = SearchForm()
    if form.validate_on_submit():
        return search_results(form.searchterm.data)
    '''lmt = 3
    tenor_apikey = "G5AGB76O808J"
    responds = requests.get("https://api.tenor.com/v1/autocomplete?key=%s&q=%s&limit=%s" %(tenor_apikey, form.searchterm.data, lmt)).json()
    url =[]
    for item in responds['results']:
        url.append(item)'''
    return render_template('main/index.html', form=form)


@main_blueprint.route("/results")
def search_results(search_query):
    search_results = query_API(search_query)
    return render_template('main/results.html', results=search_results, query=search_query)

def query_API(searchterm):
    # included my API key 
    tenor_apikey = "G5AGB76O808J"
    # get url from tenor-gif website
    url = "https://api.tenor.com/v1/search?q=%s&key=%s" % (searchterm, tenor_apikey)
    # extract information from the url and convert it to json file
    json_query = requests.get(url).json()
    finalurls = []    
    for item in json_query['results']:
        temp = item['media'][0]['tinygif']['url']
        finalurls.append(temp)
    return finalurls
