from stt import recognize_speech
from tts import speak_text
from learning import learn_response
from plugin_assistant import PluginAssistant

def main():
    assistant = PluginAssistant()
    assistant.load_plugins()

    while True:
        text = recognize_speech()
        response = assistant.handle_command(text)
        if not response:
            response = learn_response(text)
        speak_text(response)

if __name__ == "__main__":
    main()
