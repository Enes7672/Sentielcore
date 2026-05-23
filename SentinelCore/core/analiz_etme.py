class LogAnalyzer:
    def __init__(self, keywords=None):
        self.keywords = keywords or ["error", "critical", "failed"]

    def analiz_et(self, data: str) -> dict:
        temizlenmis_data = data.strip().lower()
        for keyword in self.keywords:
            if keyword.lower() in temizlenmis_data:
                return {"durum": "TEHLIKE", "mesaj": data}
        return {"durum": "TEMIZ", "mesaj": data}
