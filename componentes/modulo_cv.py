import os
import webbrowser
import subprocess
import time
from componentes.colores import Colors
from componentes.servidor_nucleo import nodo_servidor # Importamos el núcleo

def menu_gestor_cv():
    """Muestra el menú de gestión para el Curriculum Vitaem (Enhanced with Verix Node)."""
    cv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'curriculumvitaem')
    
    # Iniciamos el motor en segundo plano si no está activo
    print(f"\n{Colors.CYAN}[VERIX NODE] Iniciando motor de microservicios...{Colors.ENDC}")
    try:
        nodo_servidor.iniciar_segundo_plano()
    except Exception as e:
        print(f"{Colors.YELLOW}[INFO] El nodo ya estaba activo o puerto ocupado: {e}{Colors.ENDC}")

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\n{Colors.CYAN}{Colors.BOLD}--- GESTOR CURRICULUM VITAEM (Smarter & Better) ---{Colors.ENDC}")
        print(f"{Colors.YELLOW}Estado del Nodo:{Colors.ENDC} {Colors.GREEN}ONLINE (localhost:5000){Colors.ENDC}")
        print("\n  1. 📝 Abrir Editor Inteligente (Web App Local)")
        print("  2. ☁️  Forzar Sincronización (GitHub)")
        print("  3. 📂 Abrir carpeta de recursos")
        print("  0. Volver al Panel Principal")
        
        opcion = input("\n>> Selecciona una opción: ").strip()

        if opcion == '1':
            print(f"\n{Colors.GREEN}Lanzando interfaz web...{Colors.ENDC}")
            nodo_servidor.abrir_navegador()
            input("Presiona Enter para continuar...")

        elif opcion == '2':
            print(f"\n{Colors.MAGENTA}Iniciando protocolo de sincronización...{Colors.ENDC}")
            try:
                # Usamos la lógica del servidor para sincronizar
                from componentes.servidor_nucleo import _git_sync
                exito, msg = _git_sync()
                if exito:
                    print(f"\n{Colors.GREEN}[EXITO] {msg}{Colors.ENDC}")
                else:
                    print(f"\n{Colors.RED}[ERROR] {msg}{Colors.ENDC}")
            except Exception as e:
                print(f"\n{Colors.RED}[ERROR] Fallo crítico: {e}{Colors.ENDC}")
            input("Presiona Enter para continuar...")

        elif opcion == '3':
            os.startfile(cv_path)
        
        elif opcion == '0':
            break
        
    return "Acceso a Gestor CV finalizado."
