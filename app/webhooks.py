from app import agent
from app import handlers
from flask_dialogflow.conversation import V2beta1DialogflowConversation

@agent.handle(intent="park.info")
def park_info_callback(conv: V2beta1DialogflowConversation):
    return handlers.retrieve_park_info(conv)

@agent.handle(intent="park.find")
def park_find_callback(conv: V2beta1DialogflowConversation):
    return handlers.find_park(conv)

@agent.handle(intent="park.find - yes")
def park_find_followup_callback(conv: V2beta1DialogflowConversation):
    return handlers.find_followup_info(conv)