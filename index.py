
import pyttsx3
import speech_recognition as sr
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Speak your command")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        speak("Recognizing your command")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Unable to Recognize your command")
        speak("Unable to Recognize your command")
        return "None"
    return query


if __name__ == '__main__':
    def clear(): return os.system('cls')
    clear()
    speak("Hello, I am the Royal Constructor who will assist you to make a website. Please answer the questions. What is the name of your html file?")
    fileName = takeCommand()
    speak("What is the name of your website?")
    name = takeCommand()
    f = open(fileName+".html", "w")
    f.write("<!DOCTYPE html>\n<html>\n<head>\n<title>")
    f.write(name)
    f.write("</title>\n</head>\n<body>\n<h1>")
    f.write(name)
    f.write("</h1>\n<p>")
    f.write(name)
    f.write("</p>\n</body>\n</html>")
    f.close()

    speak("Your basic website is ready. Do you want to add a description?")
    ans = takeCommand()
    if "yes" in ans:
        speak("Please enter your description.")
        desc = takeCommand()
        f = open(fileName+".html", "a")
        f.write("\n<p>")
        f.write(desc)
        f.write("</p>\n</body>\n</html>")
        f.close()
    else:
        speak("Your basic website is ready.")

    speak("Now, please say the required commands to add features to your website.")
    speak("The command should be in the form of 'add feature'.")
    speak("For example, if you want to add a heading, you should say 'add heading'.")
    speak("If you want to add a paragraph, you should say 'add paragraph'.")
    speak("To open your website, say 'open website' or 'start'.")
    speak("If you need help, say 'help'.")
    speak("If you want to exit, say 'exit'.")
    speak("Now, let's begin.")

    runAssistant = True

    while runAssistant:
        query = takeCommand().lower()
        if ("close" or "stop" or "exit") in query:
            speak("Thank you for using Royal Constructor. If you like the project, please star it on GitHub and fork it to add your own command. Have a nice day!")
            runAssistant = False
        elif ("who" or "created you") in query:
            speak("I was created by Royal a.k.a Subham Roy.")
        elif "heading" in query:
            speak("Please enter the heading.")
            heading = takeCommand()
            f = open(fileName+".html", "a")
            f.write("\n<h1>")
            f.write(heading)
            f.write("</h1>")
            f.close()
            speak("Heading added.")
        elif "paragraph" in query:
            speak("Please enter the paragraph.")
            paragraph = takeCommand()
            f = open(fileName+".html", "a")
            f.write("\n<p>")
            f.write(paragraph)
            f.write("</p>")
            f.close()
            speak("Paragraph added.")
        elif "list" in query:
            speak("Please enter the list.")
            list = takeCommand()
            f = open(fileName+".html", "a")
            f.write("\n<ul>\n<li>")
            f.write(list)
            f.write("</li>\n</ul>")
            f.close()
            speak("List added.")
        elif "image" in query:
            speak("Please enter the image.")
            image = takeCommand()
            f = open(fileName+".html", "a")
            f.write("\n<img src=")
            f.write(image)
            f.write(">")
            f.close()
            speak("Image added.")
        elif "video" in query:
            speak("Please enter the video.")
            video = takeCommand()
            f = open(fileName+".html", "a")
            f.write("\n<video src=")
            f.write(video)
            f.write(">")
            f.close()
            speak("Video added.")
        elif "link" in query:
            speak("Please enter the link.")
            link = takeCommand()
            f = open(fileName+".html", "a")
            f.write("\n<a href=")
            f.write(link)
            f.write(">")
            f.close()
            speak("Link added.")
        elif "button" in query:
            speak("Please enter the button.")
            button = takeCommand()
            f = open(fileName+".html", "a")
            f.write("\n<button>")
            f.write(button)
            f.write("</button>")
            f.close()
            speak("Button added.")
        elif "slider" in query:
            f = open(fileName+".html", "a")
            f.write("\n<input type=")
            f.write("slider")
            f.write("/>")
            f.close()
            speak("Slider field added.")
        elif "dropdown" in query:
            speak("Please enter the dropdown.")
            dropdown = takeCommand()
            f = open(fileName+".html", "a")
            f.write("\n<select>\n<option>")
            f.write(dropdown)
            f.write("</option>\n</select>")
            f.close()
            speak("Dropdown field added.")
        elif "checkbox" in query:
            f = open(fileName+".html", "a")
            f.write("\n<input type=")
            f.write("checkbox")
            f.write(">")
            f.close()
            speak("Checkbox field added.")
        elif "textbox" in query:
            f = open(fileName+".html", "a")
            f.write("\n<input type=")
            f.write("text")
            f.write(">")
            f.close()
            speak("Textbox added.")
        elif "textarea" in query:
            speak("Please enter the paragraph to be in textarea.")
            textarea = takeCommand()
            f = open(fileName+".html", "a")
            f.write("\n<textarea>")
            f.write(textarea)
            f.write("</textarea>")
            f.close()
            speak("Textarea added.")
        elif "date" in query:
            f = open(fileName+".html", "a")
            f.write("\n<input type=")
            f.write("date")
            f.write(">")
            f.close()
            speak("Date field added.")
        elif "time" in query:
            f = open(fileName+".html", "a")
            f.write("\n<input type=")
            f.write("time")
            f.write(">")
            f.close()
            speak("Time field added.")
        elif "email" in query:
            f = open(fileName+".html", "a")
            f.write("\n<input type=")
            f.write("email")
            f.write(">")
            f.close()
            speak("Email field added.")
        elif "password" in query:
            f = open(fileName+".html", "a")
            f.write("\n<input type=")
            f.write("password")
            f.write(">")
            f.close()
            speak("Password field added.")
        elif ("open" or "start") in query:
            speak("Opening your beautiful website.")
            webbrowser.open(fileName+".html")
        elif "help" in query:
            speak("You can add any of the following things to the file.")
            speak("add heading. add paragraph, add image, add video, add link, add table, add form, add button, add slider, add dropdown, add checkbox, add radio button, add textbox, add textarea, add date, add time, add email, add password, add submit, add reset.")
            speak("The command should be in the form of 'add feature'.")
            speak(
                "For example, if you want to add a heading, you should say 'add heading'.")
            speak("You can also open the file by spaking open website.")
            speak("If you want to exit, say 'close' or 'exit' or 'stop'.")
        else:
            speak("I didn't get that, please try again")
