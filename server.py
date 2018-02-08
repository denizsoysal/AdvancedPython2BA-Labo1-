# server.py
# Math tools web application
# Author: Sébastien Combéfis
# Version: February 8, 2018

import cherrypy
import os

class WebApp:
    @cherrypy.expose
    def index(self):
        return 'Hello World!'

cherrypy.quickstart(WebApp(), '', 'server.conf')
