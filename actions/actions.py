# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from weather import Weather


class ActionWeather(Action):

    def name(self) -> Text:
        return "action_weather_api"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        

        city = tracker.get_slot("city")

        if city is None:
            weather = int(Weather("Brasilia")['temp']-273)
            dispatcher.utter_message(response="utter_cheer_up", weather=str(weather))
            return []

        weather = int(Weather(city)['temp']-273)
        dispatcher.utter_message(response="utter_weather_res", weather=str(weather))

        return []
