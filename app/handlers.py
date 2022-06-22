from app import controllers
from flask import render_template
from flask_dialogflow.conversation import V2beta1DialogflowConversation

from app.exceptions import ParkNotFoundExcpetion

def retrieve_park_info(conv: V2beta1DialogflowConversation):
    park_name = conv.parameters.get("park-name")
    park_year, park_area, park_summary = controllers.get_park_year_area_summary(park_name)
    
    conv.ask(render_template("park_info", park_name=park_name, park_year=park_year, park_area=park_area, park_summary=park_summary))
    return conv

def find_park(conv: V2beta1DialogflowConversation):
    park_state = conv.parameters.get("park-state")
    park_desc = conv.parameters.get("park-feature")

    try:
        park_name = controllers.find_park_by_desc(park_state, park_desc)
        conv.contexts.set("park_ctx", lifespan_count=3, park_name=park_name)
        conv.ask(render_template("park_found", park_name=park_name))
    except ParkNotFoundExcpetion:
        conv.ask(render_template("park_not_found"))

    return conv

def find_followup_info(conv: V2beta1DialogflowConversation):
    park_name = conv.contexts.get("park_ctx").parameters["park_name"]
    park_year, park_area, park_summary = controllers.get_park_year_area_summary(park_name)
    
    conv.ask(render_template("park_info", park_name=park_name, park_year=park_year, park_area=park_area, park_summary=park_summary))
    return conv
