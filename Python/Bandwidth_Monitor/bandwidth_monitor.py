import psutil

data_io = psutil.net_io_counters(pernic=True)
# data_connections = psutil.net_connections(kind='inet')
data_if = psutil.net_if_stats()
with open('C:\\Users\\The Gibbon\\Desktop\\Projects\\Python\\Bandwidth_Monitor\\output.txt', 'w', encoding='utf-8') as f:
    for key in data_io:
        io_stats = data_io.get(key)
        if_stats = data_if.get(key)
        f.write(f'{key} {io_stats}\n    {if_stats}\n\n')
    f.close()