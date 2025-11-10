from collections import Counter


def log_analyzer():
    try:
        with open('sample_access.log', 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print('File is not found')
        return

    gets = 0
    posts = 0
    deletes = 0
    puts = 0
    dirs = []
    empty_dirs = []
    all_ips = []
    all_sizes = []

    for line in lines:
        if not line:
            continue
        parts = line.split()

        # Методы
        method = parts[5].replace('"', '')
        if method == 'GET':
            gets += 1
        elif method == 'POST':
            posts += 1
        elif method == 'DELETE':
            deletes += 1
        elif method == 'PUT':
            puts += 1

        # Размеры
        try:
            sizes = parts[-1]
            sizes_int = int(sizes)
            all_sizes.append(sizes_int)
        except (ValueError, IndexError):
            continue

        # URL
        if len(parts) > 6 and parts[6].startswith('/'):
            url = parts[6]
            if len(url) > 1:
                dirs.append(url)
            else:
                empty_dirs.append(url)

        # IP
        ips = parts[0]
        all_ips.append(ips)

    # Статистика
    ip_counter = Counter(all_ips)
    top_10 = ip_counter.most_common(10)
    top_10_slowest = sorted(all_sizes, reverse=True)[:10]

    def write_report():
        with open('statistics_report.txt', 'w', encoding='utf-8') as report_file:  # 'w' вместо 'r'
            report_file.write('=== Log Analyzer Report ===\n')
            report_file.write(f'Total requests: {len(lines)}\n')
            report_file.write('Requests by method:\n')
            report_file.write(f'- GET: {gets}\n')
            report_file.write(f'- POST: {posts}\n')
            report_file.write(f'- PUT: {puts}\n')
            report_file.write(f'- DELETE: {deletes}\n')
            report_file.write('Top 10 IP addresses:\n')
            for ip, count in top_10:
                report_file.write(f"- {ip}: {count} requests\n")
            report_file.write('Top 10 slowest requests (by response size):\n')
            for i, size in enumerate(top_10_slowest, 1):
                report_file.write(f"{i}. {size} bytes\n")

    # ВЫЗЫВАЕМ функцию записи
    write_report()

    # Также выводим в консоль для проверки
    print('Report saved to statistics_report.txt')


if __name__ == '__main__':
    log_analyzer()