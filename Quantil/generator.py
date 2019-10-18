from datetime import datetime
from random import randint
import sys


def generate_log(myDate):
    file_path = str(sys.argv[1])
    try:
        # To create a file name using date
        fp = open(file_path+'server_log_' + myDate + '.txt', 'w+')
    except IOError:
        # Check for errors in opening file
        print("File opening failed.")
        return False
    # Calculate the timerange of 24 hours window for CPU Usage
    fp.write('Timestamp\tIP\tcpu_id\tcpu_usage\n')
    for hour in range(0, 1):
        for minute in range(0, 60):
            timestamp = datetime.strptime("{0} {1}:{2}".format(myDate, hour, minute), "%Y-%m-%d %H:%M").strftime("%s")
            cpu_id = randint(0, 1)
            cpu_usage = randint(1, 99)
            ip_addr = '.'.join([str(randint(0, 255)) for x in range(4)])
            print('{0}\t{1}\t{2}\t{3}%'.format(int(timestamp), ip_addr, cpu_id, cpu_usage))
            fp.write('{0}\t{1}\t{2}\t{3}%\n'.format(int(timestamp), ip_addr, cpu_id, cpu_usage))
    fp.close()
    return True


if __name__ == '__main__':
    date = input("Enter date in YYYY-MM-DD format: ")
    if generate_log(date):
        print('Success!')
    else:
        print('Failed!')
