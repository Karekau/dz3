
# CL Tool

## Описание
CL Tool — это инструмент для парсинга текстовых конфигураций и преобразования их в формат JSON. Он позволяет определять константы и словари, а затем выводить их в структурированном виде.

## Функции
- Поддержка определения констант.
- Парсинг словарей с подстановкой значений констант.
- Вывод результата в формате JSON.

## Установка
1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/ваш_пользователь/cl_tool.git
   ```
2. Перейдите в директорию проекта:
   ```bash
   cd cl_tool
   ```

## Использование
1. Подготовьте файл `input.txt` с конфигурацией. Пример:
   ```plaintext
   ! Это комментарий
   def CONST1 := 100;
   def CONST2 := 200;

   @{
       KEY1 = CONST1;
       KEY2 = 123;
   }
   ```

2. Запустите скрипт:
   ```bash
   python conf_json.py < input.txt
   ```

## Пример вывода
После выполнения скрипта будет сгенерирован JSON-вывод, например:
```json
{
    "constants": {
        "CONST1": "100",
        "CONST2": "200"
    },
    "dictionaries": {
        "dictionary_1": {
            "KEY1": "100",
            "KEY2": "123"
        }
    }
}
```

## Требования
- Python 3.x
- Библиотеки: `json`, `re`
