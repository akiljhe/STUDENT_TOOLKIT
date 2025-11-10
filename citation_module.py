# citation_module.py

class CitationFeature:
    
    def citation_menu(self):
        while True:
            self.clear_screen()
            print("=" * 50)
            print("FORMATTER SITASI (DAFTAR PUSTAKA)")
            print("=" * 50)
            print("1. Format Sitasi Buku")
            print("2. Format Sitasi Jurnal")
            print("3. Format Sitasi Website")
            print("4. Format Sitasi Artikel Online")
            print("0. Kembali")
            print("=" * 50)
            
            choice = input("Pilih menu: ")
            
            if choice == '1':
                self.format_book_citation()
            elif choice == '2':
                self.format_journal_citation()
            elif choice == '3':
                self.format_website_citation()
            elif choice == '4':
                self.format_online_article_citation()
            elif choice == '0':
                break
    
    def format_book_citation(self):
        self.clear_screen()
        print("=== FORMAT SITASI BUKU (APA Style) ===\n")
        
        author = input("Nama Penulis (Belakang, D.): ")
        year = input("Tahun Terbit: ")
        title = input("Judul Buku: ")
        publisher = input("Penerbit: ")
        location = input("Kota Terbit: ")
        
        citation = f"{author} ({year}). {title}. {location}: {publisher}."
        
        print(f"\n{'='*50}")
        print("HASIL:")
        print(f"{'='*50}")
        print(citation)
        print(f"{'='*50}\n")
        
        input("Tekan Enter untuk lanjut...")
    
    def format_journal_citation(self):
        self.clear_screen()
        print("=== FORMAT SITASI JURNAL (APA Style) ===\n")
        
        author = input("Nama Penulis (Belakang, D.): ")
        year = input("Tahun: ")
        title = input("Judul Artikel: ")
        journal = input("Nama Jurnal: ")
        volume = input("Volume: ")
        issue = input("Issue/Nomor: ")
        pages = input("Halaman (contoh: 123-145): ")
        
        citation = f"{author} ({year}). {title}. {journal}, {volume}({issue}), {pages}."
        
        print(f"\n{'='*50}")
        print("HASIL:")
        print(f"{'='*50}")
        print(citation)
        print(f"{'='*50}\n")
        
        input("Tekan Enter untuk lanjut...")
    
    def format_website_citation(self):
        self.clear_screen()
        print("=== FORMAT SITASI WEBSITE (APA Style) ===\n")
        
        author = input("Nama Penulis/Organisasi: ")
        year = input("Tahun: ")
        title = input("Judul Halaman: ")
        url = input("URL: ")
        access_date = input("Tanggal Akses (YYYY-MM-DD): ")
        
        citation = f"{author}. ({year}). {title}. Diakses pada {access_date}, dari {url}"
        
        print(f"\n{'='*50}")
        print("HASIL:")
        print(f"{'='*50}")
        print(citation)
        print(f"{'='*50}\n")
        
        input("Tekan Enter untuk lanjut...")
    
    def format_online_article_citation(self):
        self.clear_screen()
        print("=== FORMAT SITASI ARTIKEL ONLINE (APA Style) ===\n")
        
        author = input("Nama Penulis (Belakang, D.): ")
        year = input("Tahun: ")
        month_day = input("Bulan dan Tanggal (contoh: Maret 15): ")
        title = input("Judul Artikel: ")
        website = input("Nama Website: ")
        url = input("URL: ")
        
        citation = f"{author} ({year}, {month_day}). {title}. {website}. {url}"
        
        print(f"\n{'='*50}")
        print("HASIL:")
        print(f"{'='*50}")
        print(citation)
        print(f"{'='*50}\n")
        
        input("Tekan Enter untuk lanjut...")
