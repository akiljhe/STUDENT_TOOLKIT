# flashcard_module.py
from datetime import datetime

class FlashcardFeature:
    
    def flashcard_menu(self):
        while True:
            self.clear_screen()
            print("=" * 50)
            print("FLASHCARD")
            print("=" * 50)
            print("1. Buat Flashcard Baru")
            print("2. Belajar dengan Flashcard")
            print("3. Lihat Semua Flashcard")
            print("4. Hapus Flashcard")
            print("0. Kembali")
            print("=" * 50)
            
            choice = input("Pilih menu: ")
            
            if choice == '1':
                self.create_flashcard()
            elif choice == '2':
                self.study_flashcard()
            elif choice == '3':
                self.list_flashcards()
            elif choice == '4':
                self.delete_flashcard()
            elif choice == '0':
                break
    
    def create_flashcard(self):
        self.clear_screen()
        print("=== BUAT FLASHCARD BARU ===")
        category = input("Kategori/Topik: ")
        cards = []
        
        while True:
            print(f"\nKartu ke-{len(cards) + 1}")
            front = input("Depan/Pertanyaan (atau ketik 'selesai' untuk finish): ")
            if front.lower() == 'selesai':
                break
            
            back = input("Belakang/Jawaban: ")
            cards.append({'front': front, 'back': back})
        
        if cards:
            self.flashcards.append({
                'category': category,
                'cards': cards,
                'created': datetime.now().isoformat()
            })
            self.save_data()
            print(f"\n✓ Flashcard '{category}' berhasil dibuat dengan {len(cards)} kartu!")
        else:
            print("\n✗ Flashcard dibatalkan")
        
        input("\nTekan Enter untuk lanjut...")
    
    def study_flashcard(self):
        if not self.flashcards:
            print("\nBelum ada flashcard tersedia!")
            input("Tekan Enter untuk lanjut...")
            return
        
        self.clear_screen()
        print("=== DAFTAR FLASHCARD ===")
        for i, fc in enumerate(self.flashcards, 1):
            print(f"{i}. {fc['category']} ({len(fc['cards'])} kartu)")
        
        try:
            idx = int(input("\nPilih flashcard (nomor): ")) - 1
            if idx < 0 or idx >= len(self.flashcards):
                raise ValueError
        except:
            print("Pilihan tidak valid!")
            input("Tekan Enter untuk lanjut...")
            return
        
        fc = self.flashcards[idx]
        
        for i, card in enumerate(fc['cards'], 1):
            self.clear_screen()
            print(f"=== {fc['category']} - Kartu {i}/{len(fc['cards'])} ===\n")
            print(f"[DEPAN]\n{card['front']}")
            input("\nTekan Enter untuk melihat jawaban...")
            print(f"\n[BELAKANG]\n{card['back']}")
            
            if i < len(fc['cards']):
                input("\nTekan Enter untuk kartu berikutnya...")
        
        print("\n✓ Semua kartu sudah selesai!")
        input("\nTekan Enter untuk lanjut...")
    
    def list_flashcards(self):
        self.clear_screen()
        print("=== DAFTAR FLASHCARD ===")
        if not self.flashcards:
            print("Belum ada flashcard tersedia.")
        else:
            for i, fc in enumerate(self.flashcards, 1):
                print(f"\n{i}. {fc['category']}")
                print(f"   Jumlah kartu: {len(fc['cards'])}")
                print(f"   Dibuat: {fc['created'][:10]}")
        input("\nTekan Enter untuk lanjut...")
    
    def delete_flashcard(self):
        if not self.flashcards:
            print("\nBelum ada flashcard tersedia!")
            input("Tekan Enter untuk lanjut...")
            return
        
        self.list_flashcards()
        try:
            idx = int(input("\nPilih flashcard yang akan dihapus (nomor): ")) - 1
            if idx < 0 or idx >= len(self.flashcards):
                raise ValueError
            
            confirm = input(f"Hapus flashcard '{self.flashcards[idx]['category']}'? (y/n): ")
            if confirm.lower() == 'y':
                deleted = self.flashcards.pop(idx)
                self.save_data()
                print(f"✓ Flashcard '{deleted['category']}' berhasil dihapus!")
        except:
            print("Pilihan tidak valid!")
        
        input("\nTekan Enter untuk lanjut...")
