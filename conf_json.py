import sys
import re
import json

def parse_input(input_text):
    # Удаляем однострочные комментарии
    input_text = re.sub(r'!\s.*', '', input_text)
    # Удаляем многострочные комментарии
    input_text = re.sub(r'\(comment.*?\)', '', input_text, flags=re.DOTALL)

    # Ищем объявления констант
    const_pattern = r'def\s+([A-Z0-9_]+)\s*:=\s*([^;]+);'
    constants = {}
    for match in re.finditer(const_pattern, input_text):
        name = match.group(1)
        value = match.group(2).strip()
        constants[name] = value

    # Ищем словари
    dict_pattern = r'@{\s*([^}]*)\s*}'
    dictionaries = {}
    for match in re.finditer(dict_pattern, input_text):
        dict_content = match.group(1).strip()
        items = dict_content.split(';')
        dict_name = f'dictionary_{len(dictionaries) + 1}'  # Генерируем имя словаря
        dictionaries[dict_name] = {}
        for item in items:
            if '=' in item:
                key, value = item.split('=', 1)
                key = key.strip()
                value = value.strip()
                # Подстановка значения константы
                if value in constants:
                    value = constants[value]
                dictionaries[dict_name][key] = value

    return {
        'constants': constants,
        'dictionaries': dictionaries
    }

def main():
    input_text = sys.stdin.read()
    try:
        result = parse_input(input_text)
        print(json.dumps(result, indent=4, ensure_ascii=False))
    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
