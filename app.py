from qhue import Bridge, create_new_username
import time

username = create_new_username("192.168.1.204")

b = Bridge("192.168.1.204", username)

print(b.url)
lights = b.lights
print(lights.url)


for i in range(5):
    info = lights[1]()
    status = info['state'].get('on')
    print(status)
    if status is True:
        lights[1].state(on=False)
        print("Lights off")
        time.sleep(3)
    else:
        lights[1].state(on=True)
        print("Lights on")
        time.sleep(3)



