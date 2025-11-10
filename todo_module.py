# todo_module.py
from datetime import datetime

class TodoFeature:
    
    def todo_menu(self):
        while True:
            self.clear_screen()
            print("=" * 50)
            print("TO-DO LIST")
            print("=" * 50)
            print("1. Tambah Tugas")
            print("2. Lihat Semua Tugas")
            print("3. Tandai Tugas Selesai")
            print("4. Hapus Tugas")
            print("5. Lihat Tugas Selesai")
            print("0. Kembali")
            print("=" * 50)
            
            choice = input("Pilih menu: ")
            
            if choice == '1':
                self.add_todo()
            elif choice == '2':
                self.view_todos()
            elif choice == '3':
                self.complete_todo()
            elif choice == '4':
                self.delete_todo()
            elif choice == '5':
                self.view_completed_todos()
            elif choice == '0':
                break
    
    def add_todo(self):
        self.clear_screen()
        print("=== TAMBAH TUGAS BARU ===")
        
        task = input("Nama Tugas: ")
        priority = input("Prioritas (Tinggi/Sedang/Rendah): ")
        deadline = input("Deadline (YYYY-MM-DD, kosongkan jika tidak ada): ")
        notes = input("Catatan (opsional): ")
        
        self.todos.append({
            'task': task,
            'priority': priority,
            'deadline': deadline if deadline else None,
            'notes': notes,
            'completed': False,
            'created': datetime.now().isoformat()
        })
        self.save_data()
        
        print(f"\n✓ Tugas '{task}' berhasil ditambahkan!")
        input("\nTekan Enter untuk lanjut...")
    
    def view_todos(self):
        self.clear_screen()
        print("=== DAFTAR TUGAS ===\n")
        
        active_todos = [t for t in self.todos if not t['completed']]
        
        if not active_todos:
            print("Tidak ada tugas aktif.")
        else:
            for i, todo in enumerate(active_todos, 1):
                status = "[ ]"
                print(f"{i}. {status} {todo['task']}")
                print(f"   Prioritas: {todo['priority']}")
                if todo['deadline']:
                    print(f"   Deadline: {todo['deadline']}")
                if todo['notes']:
                    print(f"   Catatan: {todo['notes']}")
                print()
        
        input("Tekan Enter untuk lanjut...")
    
    def complete_todo(self):
        active_todos = [t for t in self.todos if not t['completed']]
        
        if not active_todos:
            print("\nTidak ada tugas aktif!")
            input("Tekan Enter untuk lanjut...")
            return
        
        self.view_todos()
        try:
            idx = int(input("\nPilih tugas yang sudah selesai (nomor): ")) - 1
            if idx < 0 or idx >= len(active_todos):
                raise ValueError
            
            task = active_todos[idx]
            for todo in self.todos:
                if todo['task'] == task['task'] and todo['created'] == task['created']:
                    todo['completed'] = True
                    todo['completed_date'] = datetime.now().isoformat()
                    break
            
            self.save_data()
            print(f"\n✓ Tugas '{task['task']}' ditandai sebagai selesai!")
        except:
            print("Pilihan tidak valid!")
        
        input("\nTekan Enter untuk lanjut...")
    
    def delete_todo(self):
        if not self.todos:
            print("\nBelum ada tugas tersedia!")
            input("Tekan Enter untuk lanjut...")
            return
        
        self.clear_screen()
        print("=== HAPUS TUGAS ===\n")
        
        for i, todo in enumerate(self.todos, 1):
            status = "[✓]" if todo['completed'] else "[ ]"
            print(f"{i}. {status} {todo['task']}")
        
        try:
            idx = int(input("\nPilih tugas yang akan dihapus (nomor): ")) - 1
            if idx < 0 or idx >= len(self.todos):
                raise ValueError
            
            confirm = input(f"Hapus tugas '{self.todos[idx]['task']}'? (y/n): ")
            if confirm.lower() == 'y':
                deleted = self.todos.pop(idx)
                self.save_data()
                print(f"✓ Tugas '{deleted['task']}' berhasil dihapus!")
        except:
            print("Pilihan tidak valid!")
        
        input("\nTekan Enter untuk lanjut...")
    
    def view_completed_todos(self):
        self.clear_screen()
        print("=== TUGAS YANG SUDAH SELESAI ===\n")
        
        completed_todos = [t for t in self.todos if t['completed']]
        
        if not completed_todos:
            print("Belum ada tugas yang diselesaikan.")
        else:
            for i, todo in enumerate(completed_todos, 1):
                print(f"{i}. [✓] {todo['task']}")
                print(f"   Selesai pada: {todo.get('completed_date', 'N/A')[:10]}")
                print()
        
        input("Tekan Enter untuk lanjut...")
