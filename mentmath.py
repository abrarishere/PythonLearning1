import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.clock import Clock
import random

class RandomNumberApp(App):
    def build(self):
        self.create_ui()
        self.init_game()
        Clock.schedule_interval(self.update_number, 1)
        return self.layout

    def create_ui(self):
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        self.header_label = Label(text="Welcome to the Random Number Game!", font_size=24, bold=True, color=(0.2, 0.6, 1, 1))
        self.layout.add_widget(self.header_label)

        self.current_number_label = Label(text="", font_size=40, color=(0.2, 0.8, 0.2, 1))
        self.layout.add_widget(self.current_number_label)

        self.answer_input = TextInput(hint_text="Enter the sum of numbers", multiline=False, font_size=20, size_hint=(None, None), width=300, height=40, pos_hint={'center_x': 0.5})
        self.layout.add_widget(self.answer_input)

        # Store the reference to the "Check Answer" button
        self.check_button = self.create_button("Check Answer", self.check_answer, (0.2, 0.6, 1, 1))

        self.create_button("Restart Game", self.restart_game, (0.8, 0.2, 0.2, 1))

        self.score_label = Label(text="Score: 0", font_size=18, color=(0, 0, 0, 1))
        self.layout.add_widget(self.score_label)

    def create_button(self, text, on_press, bg_color):
        button = Button(text=text, size_hint=(None, None), size=(150, 50), pos_hint={'center_x': 0.5}, background_color=bg_color)
        button.bind(on_press=on_press)
        self.layout.add_widget(button)
        return button  # Return the created button

    def init_game(self):
        self.rounds = 10
        self.current_round = 0
        self.total_sum = 0
        self.score = 0

    def update_number(self, dt):
        if self.current_round < self.rounds:
            random_num = random.randint(-5, 10)
            self.total_sum += random_num
            self.current_number_label.text = f"{random_num}"
            self.current_round += 1
        else:
            self.header_label.text = "Please enter the sum of all numbers:"
            self.check_button.disabled = False  # Use the stored reference

    def check_answer(self, instance):
        user_input = self.answer_input.text
        try:
            user_input = int(user_input)
            if user_input == self.total_sum:
                self.show_popup("Correct! Well done.")
                self.score += 1
            else:
                self.show_popup(f"Wrong answer. The correct sum is {self.total_sum}.")
            self.restart_game(None)
        except ValueError:
            self.show_popup("Invalid input. Please enter a valid number.")

    def restart_game(self, instance):
        self.current_round = 0
        self.total_sum = 0
        self.current_number_label.text = ""
        self.header_label.text = "Welcome to the Random Number Game!"
        self.answer_input.text = ""
        self.check_button.disabled = True
        self.update_score()

    def show_popup(self, message):
        popup_content = BoxLayout(orientation='vertical', spacing=10, padding=10)
        popup_content.add_widget(Label(text=message, font_size=18, color=(0, 0, 0, 1)))

        close_button = Button(text="Close", size_hint=(None, None), size=(150, 50), background_color=(0.2, 0.6, 1, 1))
        close_button.bind(on_press=lambda instance: self.popup.dismiss())
        popup_content.add_widget(close_button)

        self.popup = Popup(title='Round Result', content=popup_content, size_hint=(None, None), size=(300, 150), background_color=(1, 1, 1, 1))
        self.popup.open()


    def update_score(self):
        self.score_label.text = f"Score: {self.score}"

if __name__ == '__main__':
    RandomNumberApp().run()
