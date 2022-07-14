import json

with open('5.7.json', 'w') as fw:
    with open('5.7.txt', encoding='utf-8') as f:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f}
        result = [profit, {'average_profit': round(sum([int(i) for i in profit.values() if int(i) > 0]) /
                                                   len([int(i) for i in profit.values() if int(i) > 0]))}]

    # ensure_ascii=True - экранирование не-ASCII символов, indent=None - количество отступов при сериализации
    json.dump(result, fw, ensure_ascii=False, indent=4)