# schedule_module.py
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
            
            choice = input("Pilih menu: ")
            
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
        day = input("Hari (Senin/Selasa/Rabu/Kamis/Jumat/Sabtu/Minggu): ")
        start_time = input("Waktu Mulai (HH:MM): ")
        end_time = input("Waktu Selesai (HH:MM): ")
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
            
            confirm = input(f"Hapus jadwal '{self.schedules[idx]['course']}'? (y/n): ")
            if confirm.lower() == 'y':
                deleted = self.schedules.pop(idx)
                self.save_data()
                print(f"✓ Jadwal '{deleted['course']}' berhasil dihapus!")
        except:
            print("Pilihan tidak valid!")
        
        input("\nTekan Enter untuk lanjut...")