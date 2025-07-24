import psutil

battery = psutil.sensors_battery()

if battery is not None:
    print(f"Battery percentage: {battery.percent}%")
    print(f"Power plugged in: {'Yes' if battery.power_plugged else 'No'}")