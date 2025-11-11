from collections import Counter



class Log_Analyzer():

    def __init__(self):
        self.gets = 0
        self.posts = 0
        self.deletes = 0
        self.puts = 0
        self.dirs = []
        self.empty_dirs = []
        self.all_ips = []
        self.all_sizes = []



    def log_opener(self):
        try:
            with open('sample_access.log', 'r') as file:
                lines = file.readlines()
        except FileNotFoundError:
            print('File is not found')
            return[]

        for line in lines:
            if not line.split():
                continue
            parts = line.split()
            self.log_analyzer(parts)
    def log_analyzer(self, parts):
            # Методы
            method = parts[5].replace('"', '')
            if method == 'GET':
                self.gets += 1
            elif method == 'POST':
                self.posts += 1
            elif method == 'DELETE':
                self.deletes += 1
            elif method == 'PUT':
                self.puts += 1


            # Размеры
            try:
                sizes = parts[-1]
                sizes_int = int(sizes)
                self.all_sizes.append(sizes_int)
            except (ValueError, IndexError):
                pass  # или sizes_int = 0

            # URL
            try:
                if len(parts) > 6 and parts[6].startswith('/'):
                    url = parts[6]
                    if len(url) > 1:
                        self.dirs.append(url)
                    else:
                        self.empty_dirs.append(url)
            except IndexError:
                pass

            # IP
            try:
                ips = parts[0]
                self.all_ips.append(ips)
            except IndexError:
                pass


    def report(self):
        # Статистика
        ip_counter = Counter(self.all_ips)
        top_10 = ip_counter.most_common(10)
        top_10_slowest = sorted(self.all_sizes, reverse=True)[:10]
        with open('statistics_report.txt', 'w', encoding='utf-8') as report_file:  # 'w' вместо 'r'
            report_file.write('=== Log Analyzer Report ===\n')
            report_file.write(f'Total requests: {len(self.all_ips)}\n')
            report_file.write('Requests by method:\n')
            report_file.write(f'- GET: {self.gets}\n')
            report_file.write(f'- POST: {self.posts}\n')
            report_file.write(f'- PUT: {self.puts}\n')
            report_file.write(f'- DELETE: {self.deletes}\n')
            report_file.write('Top 10 IP addresses:\n')
            for ip, count in top_10:
                report_file.write(f"- {ip}: {count} requests\n")
            report_file.write('Top 10 slowest requests (by response size):\n')
            for i, size in enumerate(top_10_slowest, 1):
                report_file.write(f"{i}. {size} bytes\n")


        # Также выводим в консоль для проверки
        print('Report saved to statistics_report.txt')


if __name__ == '__main__':
    analyzer = Log_Analyzer()  # Создаем объект
    analyzer.log_opener()      # Запускаем анализ
    analyzer.report()          # Генерируем отчет