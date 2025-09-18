from http.server import BaseHTTPRequestHandler, HTTPServer
import time

# Настройки сервера
hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        # Устанавливаем код ответа
        self.send_response(200)

        # Устанавливаем тип содержимого
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # Читаем содержимое HTML-файла
        try:
            with open("contacts.html", "r", encoding="utf-8") as file:
                content = file.read()
            self.wfile.write(bytes(content, "utf-8"))
        except FileNotFoundError:
            self.send_error(404, "File not found!")


if __name__ == "__main__":
    # Создаем сервер
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Сервер запущен по адресу http://{hostName}:{serverPort}")

    try:
        # Запускаем сервер
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    # Останавливаем сервер
    webServer.server_close()
    print("Сервер остановлен.")