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
            
            choice = self.get_validated_input(
                "Pilih menu: ",
                r"^[0-4]$",
                "Input tidak valid. Harap masukkan angka antara 0 dan 4."
            )
            
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
        
        author = self.get_validated_input(
            "Nama Penulis (Belakang, D.): ",
            r"^[A-Z][a-z']+, [A-Z]\.$",
            "Format harus 'NamaBelakang, I.' (Contoh: Kurniawan, A.)"
        )
        year = self.get_validated_input(
            "Tahun Terbit: ",
            r"^\d{4}$",
            "Format tahun harus 4 digit angka (Contoh: 2023)."
        )
        title = input("Judul Buku: ")
        publisher = input("Penerbit: ")
        location = input("Kota Terbit: ")
        
        citation = f"{author} ({year}). {title}. {location}: {publisher}."
        
        print(f"\n{'='*50}\nHASIL:\n{'='*50}\n{citation}\n{'='*50}\n")
        input("Tekan Enter untuk lanjut...")
    
    def format_journal_citation(self):
        self.clear_screen()
        print("=== FORMAT SITASI JURNAL (APA Style) ===\n")
        
        author = self.get_validated_input(
            "Nama Penulis (Belakang, D.): ",
            r"^[A-Z][a-z']+, [A-Z]\.$",
            "Format harus 'NamaBelakang, I.' (Contoh: Kurniawan, A.)"
        )
        year = self.get_validated_input(
            "Tahun: ",
            r"^\d{4}$",
            "Format tahun harus 4 digit angka (Contoh: 2023)."
        )
        title = input("Judul Artikel: ")
        journal = input("Nama Jurnal: ")
        volume = input("Volume: ")
        issue = input("Issue/Nomor: ")
        pages = input("Halaman (contoh: 123-145): ")
        
        citation = f"{author} ({year}). {title}. {journal}, {volume}({issue}), {pages}."
        
        print(f"\n{'='*50}\nHASIL:\n{'='*50}\n{citation}\n{'='*50}\n")
        input("Tekan Enter untuk lanjut...")
    
    def format_website_citation(self):
        self.clear_screen()
        print("=== FORMAT SITASI WEBSITE (APA Style) ===\n")
        
        author = self.get_validated_input(
            "Nama Penulis/Organisasi: ",
            r".+",
            "Nama Penulis/Organisasi tidak boleh kosong."
        )
        year = self.get_validated_input(
            "Tahun: ",
            r"^\d{4}$",
            "Format tahun harus 4 digit angka (Contoh: 2023)."
        )
        title = self.get_validated_input(
            "Judul Halaman: ",
            r".+",
            "Judul Halaman tidak boleh kosong."
        )
        url = self.get_validated_input(
            "URL: ",
            r"^https?://.+$",
            "Format URL tidak valid. Harus dimulai dengan 'http://' atau 'https://'"
        )
        access_date = self.get_validated_input(
            "Tanggal Akses (YYYY-MM-DD): ",
            r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$",
            "Format tanggal harus YYYY-MM-DD (Contoh: 2025-12-24)"
        )
        
        citation = f"{author}. ({year}). {title}. Diakses pada {access_date}, dari {url}"
        
        print(f"\n{'='*50}\nHASIL:\n{'='*50}\n{citation}\n{'='*50}\n")
        input("Tekan Enter untuk lanjut...")
    
    def format_online_article_citation(self):
        self.clear_screen()
        print("=== FORMAT SITASI ARTIKEL ONLINE (APA Style) ===\n")
        
        author = self.get_validated_input(
            "Nama Penulis (Belakang, D.): ",
            r"^[A-Z][a-z']+, [A-Z]\.$",
            "Format harus 'NamaBelakang, I.' (Contoh: Kurniawan, A.)"
        )
        year = self.get_validated_input(
            "Tahun: ",
            r"^\d{4}$",
            "Format tahun harus 4 digit angka (Contoh: 2023)."
        )
        month_day = self.get_validated_input(
            "Bulan dan Tanggal (contoh: Maret 15): ",
            r"^(Januari|Februari|Maret|April|Mei|Juni|Juli|Agustus|September|Oktober|November|Desember) (([1-9])|([12]\d)|(3[01]))$",
            "Format harus 'NamaBulan Tanggal' (Contoh: Maret 15)."
        )
        title = input("Judul Artikel: ")
        website = input("Nama Website: ")
        url = self.get_validated_input(
            "URL: ",
            r"^https?://.+$",
            "Format URL tidak valid. Harus dimulai dengan 'http://' atau 'https://'"
        )
        
        citation = f"{author} ({year}, {month_day}). {title}. {website}. {url}"
        
        print(f"\n{'='*50}\nHASIL:\n{'='*50}\n{citation}\n{'='*50}\n")
        input("Tekan Enter untuk lanjut...")