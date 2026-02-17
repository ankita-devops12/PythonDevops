import psutil
user_cpu = int(input("Enter CPU Thresholds:"))
sys_cpu = psutil.cpu_percent(interval=1)
print("System CPU Threshold", sys_cpu)
user_memory = int(input("Enter Memory Threshold:"))
sys_memory = psutil.virtual_memory()
memory_usage = sys_memory.percent
print("System memory usage", memory_usage)
def check_threshold():
    if user_cpu > sys_cpu:
        print("send an email to user for CPU threshold...")
    elif user_memory > sys_memory:
        print("sent an warning mail to user memory threshold...")
    else:
        print("everything is ok..")
check_threshold()
