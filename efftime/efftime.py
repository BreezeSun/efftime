import time

global_efftime = time.time()
step_efftime = time.time()
stop_flag = False

def stop():
    global stop_flag
    stop_flag = True


def start():
    global global_efftime, step_efftime, stop_flag
    if stop_flag:
        return
    global_efftime = time.time()
    step_efftime = time.time()

def end(step=''):
    global global_efftime, step_efftime, stop_flag
    if stop_flag:
        return
    if step == '':
        step_efftime = time.time()
        print(f"Run time:", round(time.time() - global_efftime, 3))
    else:
        total_time = round(time.time() - global_efftime, 3)
        step_time = round(time.time() - step_efftime, 3)
        step_efftime = time.time()
        print(f"[{step}] step_time:{step_time} total_time:{total_time}")

