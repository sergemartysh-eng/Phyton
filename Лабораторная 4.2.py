# TODO импортировать необходимые модули
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # TODO считать содержимое csv файла
    with open(INPUT_FILENAME, 'r') as f:
        lines = f.readlines()

    headers = lines[0].strip().split(',')
    result = []

    for line in lines[1:]:
        values = line.strip().split(',')
        result.append(dict(zip(headers, values)))

    # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w') as f:
        json.dump(result, f, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
