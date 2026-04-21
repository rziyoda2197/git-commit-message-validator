class PipelineDataProcessor:
    def __init__(self):
        self.pipeline = []

    def add_step(self, step):
        self.pipeline.append(step)

    def process_data(self, data):
        for step in self.pipeline:
            data = step(data)
        return data

class DataStep:
    def __init__(self, func):
        self.func = func

    def __call__(self, data):
        return self.func(data)

def clean_data(data):
    # Data cleaning logic
    return data.strip()

def transform_data(data):
    # Data transformation logic
    return data.upper()

def validate_data(data):
    # Data validation logic
    return data

def main():
    processor = PipelineDataProcessor()

    clean_step = DataStep(clean_data)
    transform_step = DataStep(transform_data)
    validate_step = DataStep(validate_data)

    processor.add_step(clean_step)
    processor.add_step(transform_step)
    processor.add_step(validate_step)

    data = "  Hello, World!  "
    processed_data = processor.process_data(data)
    print(processed_data)

if __name__ == "__main__":
    main()
```

Kodda quyidagilar mavjud:

1. `PipelineDataProcessor` klassi: bu klass pipelinega qo'shish uchun `add_step` metodi va pipeline orqali ma'lumotlarni qayta ishlash uchun `process_data` metodi mavjud.
2. `DataStep` klassi: bu klass har bir qadam uchun ishlatiladi. Uning ichida `func` parametriga qadamni bajaruvchi funksiya beriladi.
3. `clean_data`, `transform_data` va `validate_data` funksiyalari: bu funksiyalar har bir qadam uchun ishlatiladi. Ular ma'lumotlarni tozalash, o'zgartirish va tasdiqlash uchun ishlatiladi.
4. `main` funksiyasi: bu funksiya pipeline yaratish, qadam qo'shish va ma'lumotlarni qayta ishlash uchun ishlatiladi.
