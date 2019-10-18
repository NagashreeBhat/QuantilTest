from datetime import datetime
from random import randint
import sys


def generate_log(myDate):
    file_path = str(sys.argv[1])
    try:
        # To create a file name using date
        fp = open(file_path + '/server_log_' + myDate + '.txt', 'w+')
    except IOError:
        # Check for errors in opening file
        print("File opening failed.")
        return False
    # Calculate the timerange of 24 hours window for CPU Usage
    for hour in range(0, 24):
        for minute in range(0, 60):
            timestamp = datetime.strptime("{0} {1}:{2}".format(myDate, hour, minute), "%Y-%m-%d %H:%M").strftime("%s")
            cpu_id = randint(0, 1)
            cpu_usage = randint(1, 99)
            ip_addr = '.'.join([str(randint(0, 255)) for x in range(4)])
            print('{0}\t{1}\t{2}\t{3}%'.format(int(timestamp), ip_addr, cpu_id, cpu_usage))
            fp.write('{0}\t{1}\t{2}\t{3}\n'.format(int(timestamp), ip_addr, cpu_id, cpu_usage))
    fp.close()
    return True


# Hashmap the start and end of the time
def find_cpu_time(log_file, from_time, to_time):
    map = dict()
    with open(log_file, 'r') as fp:
        for line in fp:
            row = line.strip('\n').split('\t')
            try:
                key = int(row[0])
            except:
                print(row[0])
            value = row[1:]
            map[key] = value

    for mykey in sorted(map.keys()):
        if from_time < mykey < to_time:
            print('CPU {0} usage on {1} = {2}%\n'.format(map[mykey][1],
                                                         datetime.fromtimestamp(mykey).strftime('%Y-%m-%d %H:%M'),
                                                         map[mykey][2], ))


# timestamp in unixtime
def timestamp_to_epoch(timestamp):
    utc_time = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M")
    epoch_time = (utc_time - datetime(1970, 1, 1)).total_seconds()
    return int(epoch_time)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        date = input("Enter date in YYYY-MM-DD format: ")
        if generate_log(date):
            print('Success!')
        else:
            print('Failed!')
            # Pass the start and end time as argv array
    elif len(sys.argv) == 4:
        file_path = sys.argv[1]
        from_time = sys.argv[2]
        to_time = sys.argv[3]
        find_cpu_time(file_path, timestamp_to_epoch(from_time), timestamp_to_epoch(to_time))
