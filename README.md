# Rasa Chatbot

Made by Rémi Barbosa & Alban Perrier for a third year course in Artificial Intelligence

# Installation Followed
https://stackoverflow.com/a/67030859

# Features
- Form : ask about the user's age and city
- API : call openweathermap API to get informations about the weather of a city
- One happy path and two unhappy paths

# Happy path example
```
Your input ->  Hello there!
Hey! How are you?
Your input ->  Amazing
ok, can I have some information about you ?
Your input ->  yes
How old are you ?
Your input ->  I'm 18
What's your city ?
Your input ->  I live in Bordeaux
Thank you for your information.
Your input ->  What's the weather
Here is the weather for the city Bordeaux: 5°
Your input ->  thank you
You're welcome, I'm here for that.
Your input ->  bye
Bye
```

# Unhappy path 1 example
```
Your input ->  Hi
Hey! How are you?
Your input ->  My day was horrible
If you don't feel well, you should try Brasilia, the weather should cheer you up: 25°
Did that help you?
Your input ->  Yes
Great, carry on!
Bye
```

# Unhappy path 2 example
```
Your input ->  Hey
Hey! How are you?
Your input ->  I don't feel very well
If you don't feel well, you should try Brasilia, the weather should cheer you up: 25°
Did that help you?
Your input ->  No
Ok, such a shame for you, bye.
Your input ->  bye
```



