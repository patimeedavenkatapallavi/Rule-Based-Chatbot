print("🤖 Welcome to Pallavi Chatbot")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi Pallavi 👋")

    elif user == "how are you":
        print("Bot: I am fine 😊")

    elif user == "your name":
        print("Bot: I am your Internship Chatbot.")

    elif user == "college":
        print("Bot: I am your college assistant bot.")

    elif user == "time":
        import datetime
        print("Bot:", datetime.datetime.now().strftime("%H:%M"))

    elif user == "date":
        import datetime
        print("Bot:", datetime.date.today())

    elif user == "joke":
        print("Bot: Why programmers hate bugs? Because they debug life 😄")

    elif user == "thank you":
        print("Bot: Welcome Pallavi 😊")

    elif user == "about":
        print("Bot: This chatbot is created by Pallavi for AI Internship.")

    elif user == "course":
        print("Bot: I help students with AI learning.")

    elif user == "help":
        print("Bot: You can ask hello, time, date, joke, bye.")

    elif user == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: I don't understand.")