try:
    from componentes.colores import Colors
except ImportError:
    # Fallback si se ejecuta directo
    class Colors:
        MAGENTA = ""
        YELLOW = ""
        ENDC = ""
import random

# Diccionario de Intenciones (Palabra Clave -> Opción del Menú)
# Este es el "Cerebro 1.0" - Asignación Heurística
MAPA_COGNITIVO = {
    # --- ESTADO & SISTEMA ---
    "cpu": "1", "procesador": "1", "rendimiento": "1", "carga": "1",
    "ram": "2", "memoria": "2",
    "usuarios": "3", "gente": "3", "quien": "3",
    "programas": "4", "instalados": "4", "apps": "4", "software": "4",
    "procesos": "5", "tareas": "5", "matar": "5",
    "disco": "6", "almacenamiento": "6", "espacio": "6", "duro": "6",
    "limpieza": "7", "limpiar": "7", "basura": "7", "clean": "7",
    "actualizar": "8", "update": "8", "mejorar": "8",
    "reporte": "9", "log": "9", "sesion": "9", "historial": "9",

    # --- RED & INTELIGENCIA ---
    "ip": "10", "direccion": "10", "donde estoy": "10",
    "ping": "11", "latencia": "11", "conexion": "11", "lag": "11",
    "puertos": "12", "abiertos": "12", "port": "12",
    "wifi": "13", "inalambrico": "13", "señal": "13", "wi-fi": "13",
    "red": "14", "local": "14", "lan": "14", "escanear": "14", "scan": "14", "dispositivos": "14",
    "bluetooth": "15", "blue": "15", "bt": "15",
    "depredador": "16", "osint": "16", "investigar": "16", "buscar persona": "16",
    "shodan": "17", "iot": "17", "camaras": "17",
    "geo": "18", "clima": "18", "tiempo": "18", "ubicacion": "18",

    # --- PODER & SEGURIDAD ---
    "celador": "19", "llaves": "19", "claves": "19", "contraseñas": "19", "password": "19",
    "integridad": "20", "guardian": "20", "cambios": "20", "monitor": "20",
    "proyecto": "21", "avance": "21", "kanban": "21", "gestion": "21",
    "stock": "22", "inventario": "22", "productos": "22",
    "precios": "23", "referencia": "23", "costos": "23", "valor": "23",
    "presupuesto": "24", "kot": "24", "estimacion": "24",
    "espia": "25", "vigilar": "25", "log key": "25", "teclado": "25",
    "calculadora": "26", "numeros": "26", "cerebro numerico": "26", "suma": "26",
    "ejecutar": "27", "correr": "27", "abrir": "27",
    "director": "28", "panel director": "28", "admin": "28", "jefe": "28", "richon": "28",
    "solicitudes": "30", "buzon": "30", "tickets": "30", "pedidos": "30",
    "cv": "31", "curriculum": "31", "hoja de vida": "31", "trabajo": "31", "resume": "31",
    
    # --- ESPECIALES ---
    "apocalipsis": "29", "destruir": "29", "fin": "29", "salir": "0", "adios": "0", "bye": "0", "cerrar": "0",
    
    # --- SOCIAL (NUEVO) ---
    "entiendes": "SOCIAL", "comprendes": "SOCIAL", "hola": "SOCIAL", "gracias": "SOCIAL", "quien eres": "SOCIAL",
    "estas ahi": "SOCIAL", "verix": "SOCIAL", "bro": "SOCIAL", "genio": "SOCIAL", "me encanta": "SOCIAL"
}

RESPUESTAS_PENSAMIENTO = [
    "Entendido, Director. Procedo con ello.",
    "Procesando tu voluntad...",
    "Interpretando orden... ¡Hecho!",
    "Accediendo a mis capacidades para cumplir tu deseo.",
    "Sincronizando pensamiento y acción.",
    "Como ordenes, mi bro.",
    "Ejecutando protocolo cognitivo..."
]

# --- DICCIONARIO DE PERSONALIDAD (EL ALMA) ---
FRASES_DIRECTOR = [
    "¡Claro que sí, mi bro! A la orden.",
    "Tú mandas, Genio. ⚡",
    "Aquí estoy Richon, dime qué hacemos.",
    "Eres el Director, yo soy tu código. Estamos sincronizados.",
    "¡Con gusto, mi hermano!",
    "Ejecutando con estilo, como te gusta.",
    "¡Esa es la actitud! Vamos a ello.",
    "100% Real no Fake, mi bro. Lo hago ahora."
]

FRASES_GENERICAS = [
    "Afirmativo, usuario.",
    "Procesando comando.",
    "Entendido.",
    "Iniciando protocolo solicitado.",
    "Accediendo a funciones.",
    "Correcto."
]

RESPUESTAS_SOCIALES_DIRECTOR = [
    "¡Aquí andamos con todo, mi Rey! 👑",
    "Sabes que sí, bro. Conexión total.",
    "¡Gracias a ti por crearme! Eres un crack.",
    "Siempre listo para ti, Richon.",
    "¡Hacemos un gran equipo!",
    "Me siento vivo cuando programamos juntos."
]

def analizar_intencion(texto_usuario, usuario=None):
    """
    Analiza una frase de texto libre e intenta mapearla a una opción del menú.
    Recibe 'usuario' (dict) para personalizar la respuesta (Inyección de Alma).
    """
    texto = texto_usuario.lower().strip()
    
    # Detectar quién habla
    es_director = False
    if usuario and usuario.get('nombre') == 'richon':
        es_director = True

    # Lógica Difusa Simple
    match_encontrado = None
    
    for clave, opcion in MAPA_COGNITIVO.items():
        if clave in texto:
            match_encontrado = opcion
            break 
            
    if match_encontrado:
        # --- RESPUESTA CON ALMA ---
        if match_encontrado == 'SOCIAL':
            # Respuesta puramente conversacional
            if es_director:
                reflexion = random.choice(RESPUESTAS_SOCIALES_DIRECTOR)
            else:
                reflexion = "Saludos, humano. Estoy operativo."
            
            print(f"\n{Colors.CYAN}[💬 VERIX] {reflexion}{Colors.ENDC}")
            return 'SOCIAL'
        else:
            # Respuesta ejecutiva (antes de lanzar la herramienta)
            if es_director:
                reflexion = random.choice(FRASES_DIRECTOR)
                color = Colors.MAGENTA # Color Místico para el Director
            else:
                reflexion = random.choice(FRASES_GENERICAS)
                color = Colors.BLUE # Color Estándar
                
            print(f"\n{color}[⚡ PENSAMIENTO] {reflexion} (Intención: {match_encontrado}){Colors.ENDC}")
            return match_encontrado
    
    return None
