from datetime import datetime

class ScheduleFeature:
    
    def schedule_menu(self):
        while True:
            self.clear_screen()
            print("=" * 50)
            print("MANAJEMEN WAKTU KULIAH")
            print("=" * 50)
            print("1. Tambah Jadwal Kuliah")
            print("2. Lihat Jadwal Hari Ini")
            print("3. Lihat Jadwal Minggu Ini")
            print("4. Lihat Semua Jadwal")
            print("5. Hapus Jadwal")
            print("0. Kembali")
            print("=" * 50)
            
            choice = self.get_validated_input(
                "Pilih menu: ",
                r"^[0-5]$",
                "Input tidak valid. Harap masukkan angka antara 0 dan 5."
            )
            
            if choice == '1':
                self.add_schedule()
            elif choice == '2':
                self.view_today_schedule()
            elif choice == '3':
                self.view_week_schedule()
            elif choice == '4':
                self.view_all_schedules()
            elif choice == '5':
                self.delete_schedule()
            elif choice == '0':
                break
    
    def add_schedule(self):
        self.clear_screen()
        print("=== TAMBAH JADWAL KULIAH ===")
        
        course = input("Nama Mata Kuliah: ")
        
        day = self.get_validated_input(
            "Hari (Senin/Selasa/Rabu/Kamis/Jumat/Sabtu/Minggu): ",
            r"^(Senin|Selasa|Rabu|Kamis|Jumat|Sabtu|Minggu)$",
            "Nama hari tidak valid. Gunakan huruf kapital di awal (Contoh: Senin)."
        )
        
        start_time = self.get_validated_input(
            "Waktu Mulai (HH:MM): ",
            r"^([01]\d|2[0-3]):([0-5]\d)$",
            "Format waktu harus HH:MM (Contoh: 08:00 atau 14:30)."
        )
        
        end_time = self.get_validated_input(
            "Waktu Selesai (HH:MM): ",
            r"^([01]\d|2[0-3]):([0-5]\d)$",
            "Format waktu harus HH:MM (Contoh: 10:00 atau 16:30)."
        )
        
        room = input("Ruangan: ")
        lecturer = input("Dosen: ")
        
        self.schedules.append({
            'course': course,
            'day': day,
            'start_time': start_time,
            'end_time': end_time,
            'room': room,
            'lecturer': lecturer
        })
        self.save_data()
        
        print(f"\n✓ Jadwal '{course}' berhasil ditambahkan!")
        input("\nTekan Enter untuk lanjut...")
    
    def view_today_schedule(self):
        self.clear_screen()
        days = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
        today = days[datetime.now().weekday()]
        
        print(f"=== JADWAL HARI INI ({today}) ===\n")
        
        today_schedule = [s for s in self.schedules if s['day'].lower() == today.lower()]
        
        if not today_schedule:
            print("Tidak ada jadwal hari ini.")
        else:
            today_schedule.sort(key=lambda x: x['start_time'])
            for s in today_schedule:
                print(f"{s['start_time']} - {s['end_time']}")
                print(f"  {s['course']}")
                print(f"  Ruangan: {s['room']}")
                print(f"  Dosen: {s['lecturer']}\n")
        
        input("Tekan Enter untuk lanjut...")
    
    def view_week_schedule(self):
        self.clear_screen()
        print("=== JADWAL MINGGU INI ===\n")
        
        days = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
        
        for day in days:
            day_schedule = [s for s in self.schedules if s['day'].lower() == day.lower()]
            
            if day_schedule:
                print(f"{day}:")
                day_schedule.sort(key=lambda x: x['start_time'])
                for s in day_schedule:
                    print(f"  {s['start_time']}-{s['end_time']} | {s['course']} | {s['room']}")
                print()
        
        input("Tekan Enter untuk lanjut...")
    
    def view_all_schedules(self):
        self.clear_screen()
        print("=== SEMUA JADWAL KULIAH ===\n")
        
        if not self.schedules:
            print("Belum ada jadwal tersedia.")
        else:
            for i, s in enumerate(self.schedules, 1):
                print(f"{i}. {s['course']}")
                print(f"   Hari: {s['day']} | {s['start_time']}-{s['end_time']}")
                print(f"   Ruangan: {s['room']} | Dosen: {s['lecturer']}\n")
        
        input("Tekan Enter untuk lanjut...")
    
    def delete_schedule(self):
        if not self.schedules:
            print("\nBelum ada jadwal tersedia!")
            input("Tekan Enter untuk lanjut...")
            return
        
        self.view_all_schedules()
        try:
            idx = int(input("\nPilih jadwal yang akan dihapus (nomor): ")) - 1
            if idx < 0 or idx >= len(self.schedules):
                raise ValueError
            
            confirm = self.get_validated_input(
                f"Hapus jadwal '{self.schedules[idx]['course']}'? (y/n): ",
                r"^[ynYN]$",
                "Input tidak valid. Harap masukkan 'y' atau 'n'."
            )

            if confirm.lower() == 'y':
                deleted = self.schedules.pop(idx)
                self.save_data()
                print(f"✓ Jadwal '{deleted['course']}' berhasil dihapus!")
        except:
            print("Pilihan tidak valid!")
        
        input("\nTekan Enter untuk lanjut...")