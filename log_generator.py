import random
from datetime import datetime, timedelta


def generate_sample_logs(file_path, num_entries=1000):
    ips = [f"192.168.1.{i}" for i in range(1, 51)]
    methods = ["GET", "POST", "GET", "GET", "PUT", "DELETE"]  # GET чаще
    endpoints = ["/", "/api/users", "/api/login", "/api/data", "/admin", "/images/photo.jpg"]
    status_codes = [200, 200, 200, 404, 500, 301]  # 200 чаще

    with open(file_path, 'w') as f:
        base_time = datetime.now() - timedelta(days=1)

        for i in range(num_entries):
            ip = random.choice(ips)
            method = random.choice(methods)
            endpoint = random.choice(endpoints)
            status = random.choice(status_codes)
            response_size = random.randint(100, 5000)

            # Случайное время в пределах последних 24 часов
            time_offset = random.randint(0, 86400)
            log_time = base_time + timedelta(seconds=time_offset)
            time_str = log_time.strftime('%d/%b/%Y:%H:%M:%S +0000')

            log_line = f'{ip} - - [{time_str}] "{method} {endpoint} HTTP/1.1" {status} {response_size}\n'
            f.write(log_line)

    print(f"Сгенерировано {num_entries} тестовых записей в {file_path}")


if __name__ == "__main__":
    generate_sample_logs("sample_access.log", 1000)