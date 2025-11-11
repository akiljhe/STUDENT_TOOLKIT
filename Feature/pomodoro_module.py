# pomodoro_module.py
import time

class PomodoroFeature:
    
    def pomodoro_timer(self):
        self.clear_screen()
        print("=" * 50)
        print("TIMER POMODORO")
        print("=" * 50)
        print("Teknik Pomodoro: 25 menit kerja, 5 menit istirahat")
        print()
        
        try:
            work_minutes = int(input("Durasi kerja (menit) [default: 25]: ") or "25")
            break_minutes = int(input("Durasi istirahat (menit) [default: 5]: ") or "5")
            cycles = int(input("Jumlah siklus [default: 4]: ") or "4")
        except:
            print("Input tidak valid!")
            input("Tekan Enter untuk lanjut...")
            return
        
        for cycle in range(1, cycles + 1):
            self.clear_screen()
            print(f"=== SIKLUS {cycle}/{cycles} - WAKTU KERJA ===")
            print(f"Mulai bekerja selama {work_minutes} menit!")
            print("\nTekan Ctrl+C untuk membatalkan")
            
            try:
                self.countdown_timer(work_minutes * 60, "KERJA")
                
                self.clear_screen()
                print(f"=== SIKLUS {cycle}/{cycles} - WAKTU ISTIRAHAT ===")
                print(f"Istirahat selama {break_minutes} menit!")
                
                self.countdown_timer(break_minutes * 60, "ISTIRAHAT")
            except KeyboardInterrupt:
                print("\n\nTimer dibatalkan!")
                input("\nTekan Enter untuk lanjut...")
                return
        
        self.clear_screen()
        print("=" * 50)
        print("SELAMAT! SEMUA SIKLUS POMODORO SELESAI!")
        print("=" * 50)
        input("\nTekan Enter untuk lanjut...")
    
    def countdown_timer(self, seconds, session_type):
        start_time = time.time()
        end_time = start_time + seconds
        
        while time.time() < end_time:
            remaining = int(end_time - time.time())
            mins, secs = divmod(remaining, 60)
            
            print(f"\r{session_type}: {mins:02d}:{secs:02d} ", end='', flush=True)
            time.sleep(1)
        
        print(f"\n\n✓ Sesi {session_type} selesai!")
        print("\a")
        time.sleep(2)
