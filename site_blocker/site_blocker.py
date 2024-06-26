from datetime import datetime, time
from time import sleep

allowed_start_time = time(17, 0)  # 5pm
allowed_end_time = time(23, 0)  # 11pm
hosts_path = "/etc/hosts"
redirect = "127.0.0.1"

sites_to_block = {
    'www.atptour.com': set(),
    'atptour.com': set(),
    'www.chess.com': set(),
    'chess.com': set(),
    'www.filmfreeway.com': set(),
    'filmfreeway.com': set(),
    'www.imdb.com': set(),
    'imdb.com': set(),
    'www.linkedin.com': set(),
    'linkedin.com': set(),
    'www.meetup.com': set(),
    'meetup.com': set(),
    'www.mubi.com': set(),
    'mubi.com': set(),
    'www.ritzcinemas.com.au': set(),
    'ritzcinemas.com.au': set(),
    'www.rumble.com': set(),
    'rumble.com': set(),
    'www.sbs.com.au': set(),
    'sbs.com.au': set(),
    'www.tubitv.com': set(),
    'tubitv.com': set(),
    'www.twitter.com': set(),
    'twitter.com': set(),
}

while True:
    now = datetime.now().time()
    print(f"Current time: {now}")
    print(f"Allowed time range: {allowed_start_time} - {allowed_end_time}")
    if allowed_start_time <= now <= allowed_end_time:
        print("Sites not blocked")
        # Unblock the sites if they were previously blocked
        with open(hosts_path, 'r+') as hostsfile:
            hosts_content = hostsfile.read()
            for site in sites_to_block:
                if site in hosts_content:
                    hostsfile.seek(0)
                    lines = hostsfile.readlines()
                    hostsfile.seek(0)
                    hostsfile.truncate()
                    for line in lines:
                        if not line.startswith(redirect):
                            hostsfile.write(line)
                    hostsfile.flush()
                    print(f"{site} is unblocked")
    else:
        print("Block sites")
        # Block the sites if they are not already blocked
        with open(hosts_path, 'r+') as hostsfile:
            hosts_content = hostsfile.read()
            for site in sites_to_block:
                if site not in hosts_content:
                    hostsfile.write(redirect + " " + site + "\n")
                    hostsfile.flush()
                    print(f"{site} is blocked")
    sleep(60)  # Wait for 60 seconds before checking the time again
