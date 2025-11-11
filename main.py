

import os
import time
import json
from datetime import datetime, timedelta

from Feature.quiz_module import QuizFeature
from Feature.flashcard_module import FlashcardFeature
from Feature.schedule_module import ScheduleFeature
from Feature.todo_module import TodoFeature
from Feature.citation_module import CitationFeature
from Feature.pomodoro_module import PomodoroFeature
from Feature.wordcounter_module import WordCounterFeature

class StudentHelper(
    QuizFeature, 
    FlashcardFeature, 
    ScheduleFeature, 
    TodoFeature, 
    CitationFeature, 
    PomodoroFeature, 
    WordCounterFeature
):
    
    def __init__(self):
        self.data_file = "student_data.json"
        self.load_data()
    
    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.flashcards = data.get('flashcards', [])
                self.quizzes = data.get('quizzes', [])
                self.schedules = data.get('schedules', [])
                self.todos = data.get('todos', [])
        else:
            self.flashcards = []
            self.quizzes = []
            self.schedules = []
            self.todos = []
    
    def save_data(self):
        data = {
            'flashcards': self.flashcards,
            'quizzes': self.quizzes,
            'schedules': self.schedules,
            'todos': self.todos
        }
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def run(self):
        while True:
            self.clear_screen()
            print("=" * 50)
            print("STUDENT TOOLKIT")
            print("=" * 50)
            print("1. Quiz")
            print("2. FlashCard")
            print("3. Manajemen Waktu Kuliah")
            print("4. To-Do List")
            print("5. Formatter Sitasi")
            print("6. Timer Pomodoro")
            print("7. Word Counter")
            print("0. Keluar")
            print("=" * 50)
            
            choice = input("Pilih menu: ")
            
            if choice == '1':
                self.quiz_menu()
            elif choice == '2':
                self.flashcard_menu()
            elif choice == '3':
                self.schedule_menu()
            elif choice == '4':
                self.todo_menu()
            elif choice == '5':
                self.citation_menu()
            elif choice == '6':
                self.pomodoro_timer()
            elif choice == '7':
                self.word_counter_menu()
            elif choice == '0':
                self.clear_screen()
                print("Terima kasih telah menggunakan Student Toolkit!")
                break

if __name__ == "__main__":
    app = StudentHelper()
    app.run()