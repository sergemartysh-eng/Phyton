def find_common_participants(participants1, participants2, separator=','):
    list1 = participants1.split(separator)
    list2 = participants2.split(separator)
    set1 = set(list1)
    set2 = set(list2)
    common_participants = set1.intersection(set2)
    return sorted(common_participants)
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
common = find_common_participants(participants_first_group, participants_second_group, separator='|')
print(f"Общие участники: {common}")




































# TODO Провеьте работу функции с разделителем отличным от запятой