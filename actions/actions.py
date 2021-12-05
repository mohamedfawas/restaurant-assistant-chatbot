# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
class ActionReceiveName(Action):
    def name(self) -> Text:
        return "action_receive_name"
        
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
        text = tracker.latest_message['text']
        dispatcher.utter_message(text=f"I'll remember your name {text}!")
        return [SlotSet("name", text)]

class ActionSayName(Action):

    def name(self) -> Text:
        return "action_say_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name = tracker.get_slot("name")
        if not name:
            dispatcher.utter_message(text="I don't know your name.")
        else:
            dispatcher.utter_message(text=f"Your name is saved as {name}!. What would you like to order today?")
        return []
        
class ActionReceiveOrderOne(Action):
    def name(self) -> Text:
        return "action_receive_order_one"
        
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
        order_one = tracker.latest_message['text']
        print(order_one)
        dispatcher.utter_message(text=f"Your order consists of {order_one}!")
        return [SlotSet("order1", order_one)]

class ActionReceiveOrderTwo(Action):
    def name(self) -> Text:
        return "action_receive_order_two"
        
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
        order1 = tracker.get_slot("order1")
        order_two = tracker.latest_message['text']
        print(order_two)
        dispatcher.utter_message(text=f"Now your order consists of {order1} and {order_two}")
        return [SlotSet("order2", order_two)]
