# wordcounter_module.py

class WordCounterFeature:

    def word_counter_menu(self):
        while True:
            self.clear_screen()
            print("=" * 50)
            print("WORD COUNTER")
            print("=" * 50)
            print("1. Hitung Kata dari Input Langsung")
            print("2. Hitung Kata dari File")
            print("0. Kembali")
            print("=" * 50)
            
            choice = input("Pilih menu: ")
            
            if choice == '1':
                self.count_words_input()
            elif choice == '2':
                self.count_words_file()
            elif choice == '0':
                break
    
    def count_words_input(self):
        self.clear_screen()
        print("=== WORD COUNTER - INPUT LANGSUNG ===")
        print("Ketik atau paste teks Anda (ketik 'SELESAI' di baris baru untuk finish):\n")
        
        lines = []
        while True:
            line = input()
            if line == 'SELESAI':
                break
            lines.append(line)
        
        text = '\n'.join(lines)
        self.display_word_count(text)
    
    def count_words_file(self):
        self.clear_screen()
        print("=== WORD COUNTER - FILE ===")
        
        file_path = input("Masukkan path file: ")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
            
            self.display_word_count(text)
        except FileNotFoundError:
            print(f"\n✗ File '{file_path}' tidak ditemukan!")
            input("\nTekan Enter untuk lanjut...")
        except Exception as e:
            print(f"\n✗ Error: {e}")
            input("\nTekan Enter untuk lanjut...")
    
    def display_word_count(self, text):
        words = text.split()
        word_count = len(words)
        char_count = len(text)
        char_no_space = len(text.replace(' ', '').replace('\n', '').replace('\t', ''))
        line_count = len(text.split('\n'))
        
        sentence_count = text.count('.') + text.count('!') + text.count('?')
        
        avg_word_length = char_no_space / word_count if word_count > 0 else 0
        
        print(f"\n{'='*50}")
        print("STATISTIK TEKS")
        print(f"{'='*50}")
        print(f"Jumlah Kata      : {word_count}")
        print(f"Jumlah Karakter  : {char_count}")
        print(f"Karakter (no spasi): {char_no_space}")
        print(f"Jumlah Baris     : {line_count}")
        print(f"Jumlah Kalimat   : {sentence_count}")
        print(f"Rata-rata Panjang Kata: {avg_word_length:.1f} karakter")
        print(f"{'='*50}\n")
        
        input("Tekan Enter untuk lanjut...")