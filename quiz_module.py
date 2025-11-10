import json
import os
from datetime import datetime

class QuizFeature:
    
    def quiz_menu(self):
        while True:
            self.clear_screen()
            print("=" * 50)
            print("QUIZ")
            print("=" * 50)
            print("1. Buat Quiz Baru")
            print("2. Mulai Quiz")
            print("3. Lihat Daftar Quiz")
            print("4. Hapus Quiz")
            print("0. Kembali")
            print("=" * 50)
            
            choice = input("Pilih menu: ")
            
            if choice == '1':
                self.create_quiz()
            elif choice == '2':
                self.start_quiz()
            elif choice == '3':
                self.list_quizzes()
            elif choice == '4':
                self.delete_quiz()
            elif choice == '0':
                break
    
    def create_quiz(self):
        self.clear_screen()
        print("=== BUAT QUIZ BARU ===")
        title = input("Judul Quiz: ")
        questions = []
        
        while True:
            print(f"\nSoal ke-{len(questions) + 1}")
            question = input("Pertanyaan (atau ketik 'selesai' untuk finish): ")
            if question.lower() == 'selesai':
                break
            
            options = []
            for i in range(4):
                opt = input(f"Opsi {chr(65+i)}: ")
                options.append(opt)
            
            correct = input("Jawaban benar (A/B/C/D): ").upper()
            
            questions.append({
                'question': question,
                'options': options,
                'correct': correct
            })
        
        if questions:
            self.quizzes.append({
                'title': title,
                'questions': questions,
                'created': datetime.now().isoformat()
            })
            self.save_data()
            print(f"\n✓ Quiz '{title}' berhasil dibuat dengan {len(questions)} soal!")
        else:
            print("\n✗ Quiz dibatalkan (tidak ada soal)")
        
        input("\nTekan Enter untuk lanjut...")
    
    def start_quiz(self):
        if not self.quizzes:
            print("\nBelum ada quiz tersedia!")
            input("Tekan Enter untuk lanjut...")
            return
        
        self.clear_screen()
        print("=== DAFTAR QUIZ ===")
        for i, quiz in enumerate(self.quizzes, 1):
            print(f"{i}. {quiz['title']} ({len(quiz['questions'])} soal)")
        
        try:
            idx = int(input("\nPilih quiz (nomor): ")) - 1
            if idx < 0 or idx >= len(self.quizzes):
                raise ValueError
        except:
            print("Pilihan tidak valid!")
            input("Tekan Enter untuk lanjut...")
            return
        
        quiz = self.quizzes[idx]
        score = 0
        
        self.clear_screen()
        print(f"=== {quiz['title']} ===\n")
        
        for i, q in enumerate(quiz['questions'], 1):
            print(f"Soal {i}: {q['question']}")
            for j, opt in enumerate(q['options']):
                print(f"  {chr(65+j)}. {opt}")
            
            answer = input("\nJawaban Anda (A/B/C/D): ").upper()
            
            if answer == q['correct']:
                print("✓ Benar!")
                score += 1
            else:
                print(f"✗ Salah! Jawaban yang benar: {q['correct']}")
            print()
        
        print(f"\n{'='*50}")
        print(f"SKOR ANDA: {score}/{len(quiz['questions'])} ({score/len(quiz['questions'])*100:.1f}%)")
        print(f"{'='*50}")
        input("\nTekan Enter untuk lanjut...")
    
    def list_quizzes(self):
        self.clear_screen()
        print("=== DAFTAR QUIZ ===")
        if not self.quizzes:
            print("Belum ada quiz tersedia.")
        else:
            for i, quiz in enumerate(self.quizzes, 1):
                print(f"\n{i}. {quiz['title']}")
                print(f"   Jumlah soal: {len(quiz['questions'])}")
                print(f"   Dibuat: {quiz['created'][:10]}")
        input("\nTekan Enter untuk lanjut...")
    
    def delete_quiz(self):
        if not self.quizzes:
            print("\nBelum ada quiz tersedia!")
            input("Tekan Enter untuk lanjut...")
            return
        
        self.list_quizzes()
        try:
            idx = int(input("\nPilih quiz yang akan dihapus (nomor): ")) - 1
            if idx < 0 or idx >= len(self.quizzes):
                raise ValueError
            
            confirm = input(f"Hapus quiz '{self.quizzes[idx]['title']}'? (y/n): ")
            if confirm.lower() == 'y':
                deleted = self.quizzes.pop(idx)
                self.save_data()
                print(f"✓ Quiz '{deleted['title']}' berhasil dihapus!")
        except:
            print("Pilihan tidak valid!")
        
        input("\nTekan Enter untuk lanjut...")