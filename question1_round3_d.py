import threading
import time
import random

class Drone:
    def __init__(self, id):
        self.id = id
        self.target_found = False
        self.position = [0, 0]  # Placeholder for position
        self.lidar_sensor = LidarSensor()
        self.color_sensor = ColorSensor()
        self.target_color = 'green'

    def move(self):
        while not self.target_found:
            self.position[0] += random.choice([-1, 1])
            self.position[1] += random.choice([-1, 1])
            print(f"Drone {self.id} moving to position {self.position}")
            self.check_for_obstacle()
            time.sleep(1)

    def check_for_obstacle(self):
        height, width, depth = self.lidar_sensor.measure()
        if height == 15 and width == 15 and depth == 15:
            color = self.color_sensor.detect_color()
            if color == self.target_color:
                print(f"Drone {self.id} found the target at position {self.position}")
                self.target_found = True
                swarm_communication(self.id)

    def stop(self):
        print(f"Drone {self.id} stopping search.")
        self.target_found = True

class LidarSensor:
    def measure(self):
        # Simulated measurement, replace with actual sensor data
        return 15, 15, 15

class ColorSensor:
    def detect_color(self):
        # Simulated color detection, replace with actual sensor data
        return random.choice(['red', 'blue', 'green', 'yellow'])

def swarm_communication(finding_drone_id):
    global drones
    for drone in drones:
        if drone.id != finding_drone_id:
            drone.stop()

if __name__ == "__main__":
    drones = [Drone(id=i) for i in range(3)]
    threads = []

    for drone in drones:
        t = threading.Thread(target=drone.move)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
