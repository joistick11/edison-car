from echo_sensor import has_obstacle
from motors_controller import run_forward, full_stop

if __name__ == '__main__':
    try:
        while True:
            if not has_obstacle():
                run_forward(1)
    except KeyboardInterrupt:
        full_stop()
        exit(1)
