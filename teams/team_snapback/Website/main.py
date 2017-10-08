from flask import Flask
from flask import render_template
from flask import abort, redirect, url_for
from flask import request, send_from_directory
import requests
import dropbox
import updown
import json
import config

TOKEN = config.dropbox_key
dbx = dropbox.Dropbox(TOKEN)
fileLists = updown.list_folder(dbx, "SnapBack", "")
for name in fileLists.iterkeys():
    print name

app = Flask(__name__)


@app.route('/')
def home():
    return redirect(url_for('index'))


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/videos')
def videos():
    fileList = updown.list_folder(dbx, "SnapBack", "")
    videoList = []
    for name in fileList.iterkeys():
        if name.endswith('.avi') or name.endswith('.mp4'):
            videoList.append(name)
        print videoList
    return render_template('videosPage.html', videosList=videoList)

# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name)


@app.route('/video/<fileName>')
def video(fileName):
    video = updown.download(dbx, "SnapBack", "", fileName)
    with open('file/' + fileName, 'wb') as writer:
        writer.write(video)
    return render_template('videoPlayer.html', video='/file/' + fileName)


@app.route('/file/<path:path>')
def send_file(path):
    return send_from_directory('file', path)


@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)


@app.route('/custom/<path:path>')
def send_cust(path):
    return send_from_directory('custom', path)
