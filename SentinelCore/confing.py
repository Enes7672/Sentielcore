# uygulama içi yapılandırma ayarları
class confing:
    def __init__(self):
        self.nexus_host = 'localhost'
        self.nexus_port = 12345
        self.raporlama_dosyasi = 'raporlar.txt'
        self.analiz_kritik_kelime = ['error', 'critical', 'failed']
    