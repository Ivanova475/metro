# coding=utf-8

LINES = {
    1: 'Сокольническая линия',
    2: 'Замоскворецкая линия',
    3: 'Арбатско-Покровская линия',
    4: 'Филевская линия',
    5: 'Кольцевая линия',
    6: 'Калужско-Рижская линия',
    7: 'Таганско-Краснопресненская линия',
    8: 'Калининско-Солнцевская линия',
    9: 'Серпуховско-Тимирязевская линия',
    10: 'Люблинско-Дмитровская линия',
    11: 'Каховская линия',
    12: 'Бутовская линия',
    13: 'Московский монорельс',
    14: 'Московское центральное кольцо',
    15: 'Большая кольцевая линия'
}


STATIONS = {
    1: {'line': 1, 'name': 'Бульвар Рокоссовского'},
    2: {'line': 1, 'name': 'Черкизовская'},
    3: {'line': 1, 'name': 'Преображенская площадь'},
    4: {'line': 1, 'name': 'Сокольники'},
    5: {'line': 1, 'name': 'Красносельская'},
    6: {'line': 1, 'name': 'Комсомольская'},
    7: {'line': 1, 'name': 'Красные Ворота'},
    8: {'line': 1, 'name': 'Чистые пруды'},
    9: {'line': 1, 'name': 'Лубянка'},
    10: {'line': 1, 'name': 'Охотный Ряд'},
    11: {'line': 1, 'name': 'Библиотека имени Ленина'},
    12: {'line': 1, 'name': 'Кропоткинская'},
    13: {'line': 1, 'name': 'Парк культуры'},
    14: {'line': 1, 'name': 'Фрунзенская'},
    15: {'line': 1, 'name': 'Спортивная'},
    16: {'line': 1, 'name': 'Воробьёвы горы'},
    17: {'line': 1, 'name': 'Университет'},
    18: {'line': 1, 'name': 'Проспект Вернадского'},
    19: {'line': 1, 'name': 'Юго-Западная'},
    20: {'line': 2, 'name': 'Речной вокзал'},
    21: {'line': 2, 'name': 'Водный стадион'},
    22: {'line': 2, 'name': 'Войковская'},
    23: {'line': 2, 'name': 'Сокол'},
    24: {'line': 2, 'name': 'Аэропорт'},
    25: {'line': 2, 'name': 'Динамо'},
    26: {'line': 2, 'name': 'Белорусская'},
    27: {'line': 2, 'name': 'Маяковская'},
    28: {'line': 2, 'name': 'Тверская'},
    29: {'line': 2, 'name': 'Театральная'},
    30: {'line': 2, 'name': 'Новокузнецкая'},
    31: {'line': 2, 'name': 'Павелецкая'},
    32: {'line': 2, 'name': 'Автозаводская'},
    33: {'line': 2, 'name': 'Коломенская'},
    34: {'line': 2, 'name': 'Каширская'},
    35: {'line': 2, 'name': 'Кантемировская'},
    36: {'line': 2, 'name': 'Царицыно'},
    37: {'line': 2, 'name': 'Орехово'},
    38: {'line': 2, 'name': 'Домодедовская'},
    39: {'line': 2, 'name': 'Красногвардейская'},
    40: {'line': 3, 'name': 'Щёлковская'},
    41: {'line': 3, 'name': 'Первомайская'},
    42: {'line': 3, 'name': 'Измайловская'},
    43: {'line': 3, 'name': 'Партизанская'},
    44: {'line': 3, 'name': 'Семёновская'},
    45: {'line': 3, 'name': 'Электрозаводская'},
    46: {'line': 3, 'name': 'Бауманская'},
    47: {'line': 3, 'name': 'Курская'},
    48: {'line': 3, 'name': 'Площадь Революции'},
    49: {'line': 3, 'name': 'Арбатская'},
    50: {'line': 3, 'name': 'Смоленская'},
    51: {'line': 3, 'name': 'Киевская'},
    52: {'line': 3, 'name': 'Парк Победы'},
    53: {'line': 3, 'name': 'Славянский бульвар'},
    54: {'line': 3, 'name': 'Кунцевская'},
    55: {'line': 3, 'name': 'Молодёжная'},
    56: {'line': 3, 'name': 'Крылатское'},
    57: {'line': 3, 'name': 'Строгино'},
    58: {'line': 4, 'name': 'Кунцевская'},
    59: {'line': 4, 'name': 'Пионерская'},
    60: {'line': 4, 'name': 'Филёвский парк'},
    61: {'line': 4, 'name': 'Багратионовская'},
    62: {'line': 4, 'name': 'Фили'},
    63: {'line': 4, 'name': 'Кутузовская'},
    64: {'line': 4, 'name': 'Студенческая'},
    65: {'line': 4, 'name': 'Киевская'},
    66: {'line': 4, 'name': 'Смоленская'},
    67: {'line': 4, 'name': 'Арбатская'},
    68: {'line': 4, 'name': 'Александровский сад'},
    69: {'line': 4, 'name': 'Выставочная'},
    70: {'line': 4, 'name': 'Международная'},
    71: {'line': 5, 'name': 'Парк культуры'},
    72: {'line': 5, 'name': 'Октябрьская'},
    73: {'line': 5, 'name': 'Добрынинская'},
    74: {'line': 5, 'name': 'Павелецкая'},
    75: {'line': 5, 'name': 'Таганская'},
    76: {'line': 5, 'name': 'Курская'},
    77: {'line': 5, 'name': 'Комсомольская'},
    78: {'line': 5, 'name': 'Проспект Мира'},
    79: {'line': 5, 'name': 'Новослободская'},
    80: {'line': 5, 'name': 'Белорусская'},
    81: {'line': 5, 'name': 'Краснопресненская'},
    82: {'line': 5, 'name': 'Киевская'},
    83: {'line': 6, 'name': 'Медведково'},
    84: {'line': 6, 'name': 'Бабушкинская'},
    85: {'line': 6, 'name': 'Свиблово'},
    86: {'line': 6, 'name': 'Ботанический сад'},
    87: {'line': 6, 'name': 'ВДНХ'},
    88: {'line': 6, 'name': 'Алексеевская'},
    89: {'line': 6, 'name': 'Рижская'},
    90: {'line': 6, 'name': 'Проспект Мира'},
    91: {'line': 6, 'name': 'Сухаревская'},
    92: {'line': 6, 'name': 'Тургеневская'},
    93: {'line': 6, 'name': 'Китай-город'},
    94: {'line': 6, 'name': 'Третьяковская'},
    95: {'line': 6, 'name': 'Октябрьская'},
    96: {'line': 6, 'name': 'Шаболовская'},
    97: {'line': 6, 'name': 'Ленинский проспект'},
    98: {'line': 6, 'name': 'Академическая'},
    99: {'line': 6, 'name': 'Профсоюзная'},
    100: {'line': 6, 'name': 'Новые Черёмушки'},
    101: {'line': 6, 'name': 'Калужская'},
    102: {'line': 6, 'name': 'Беляево'},
    103: {'line': 6, 'name': 'Коньково'},
    104: {'line': 6, 'name': 'Тёплый Стан'},
    105: {'line': 6, 'name': 'Ясенево'},
    106: {'line': 6, 'name': 'Новоясеневская'},
    107: {'line': 7, 'name': 'Планерная'},
    108: {'line': 7, 'name': 'Сходненская'},
    109: {'line': 7, 'name': 'Тушинская'},
    110: {'line': 7, 'name': 'Щукинская'},
    111: {'line': 7, 'name': 'Октябрьское Поле'},
    112: {'line': 7, 'name': 'Полежаевская'},
    113: {'line': 7, 'name': 'Беговая'},
    114: {'line': 7, 'name': 'Улица 1905 года'},
    115: {'line': 7, 'name': 'Баррикадная'},
    116: {'line': 7, 'name': 'Пушкинская'},
    117: {'line': 7, 'name': 'Кузнецкий Мост'},
    118: {'line': 7, 'name': 'Китай-город'},
    119: {'line': 7, 'name': 'Таганская'},
    120: {'line': 7, 'name': 'Пролетарская'},
    121: {'line': 7, 'name': 'Волгоградский проспект'},
    122: {'line': 7, 'name': 'Текстильщики'},
    123: {'line': 7, 'name': 'Кузьминки'},
    124: {'line': 7, 'name': 'Рязанский проспект'},
    125: {'line': 7, 'name': 'Выхино'},
    126: {'line': 8, 'name': 'Новогиреево'},
    127: {'line': 8, 'name': 'Перово'},
    128: {'line': 8, 'name': 'Шоссе Энтузиастов'},
    129: {'line': 8, 'name': 'Авиамоторная'},
    130: {'line': 8, 'name': 'Площадь Ильича'},
    131: {'line': 8, 'name': 'Марксистская'},
    132: {'line': 8, 'name': 'Третьяковская'},
    133: {'line': 9, 'name': 'Алтуфьево'},
    134: {'line': 9, 'name': 'Бибирево'},
    135: {'line': 9, 'name': 'Отрадное'},
    136: {'line': 9, 'name': 'Владыкино'},
    137: {'line': 9, 'name': 'Петровско-Разумовская'},
    138: {'line': 9, 'name': 'Тимирязевская'},
    139: {'line': 9, 'name': 'Дмитровская'},
    140: {'line': 9, 'name': 'Савёловская'},
    141: {'line': 9, 'name': 'Менделеевская'},
    142: {'line': 9, 'name': 'Цветной бульвар'},
    143: {'line': 9, 'name': 'Чеховская'},
    144: {'line': 9, 'name': 'Боровицкая'},
    145: {'line': 9, 'name': 'Полянка'},
    146: {'line': 9, 'name': 'Серпуховская'},
    147: {'line': 9, 'name': 'Тульская'},
    148: {'line': 9, 'name': 'Нагатинская'},
    149: {'line': 9, 'name': 'Нагорная'},
    150: {'line': 9, 'name': 'Нахимовский проспект'},
    151: {'line': 9, 'name': 'Севастопольская'},
    152: {'line': 9, 'name': 'Чертановская'},
    153: {'line': 9, 'name': 'Южная'},
    154: {'line': 9, 'name': 'Пражская'},
    155: {'line': 9, 'name': 'Улица Академика Янгеля'},
    156: {'line': 9, 'name': 'Аннино'},
    157: {'line': 9, 'name': 'Бульвар Дмитрия Донского'},
    158: {'line': 10, 'name': 'Трубная'},
    159: {'line': 10, 'name': 'Сретенский бульвар'},
    160: {'line': 10, 'name': 'Чкаловская'},
    161: {'line': 10, 'name': 'Римская'},
    162: {'line': 10, 'name': 'Крестьянская Застава'},
    163: {'line': 10, 'name': 'Дубровка'},
    164: {'line': 10, 'name': 'Кожуховская'},
    165: {'line': 10, 'name': 'Печатники'},
    166: {'line': 10, 'name': 'Волжская'},
    167: {'line': 10, 'name': 'Люблино'},
    168: {'line': 10, 'name': 'Братиславская'},
    169: {'line': 10, 'name': 'Марьино'},
    170: {'line': 11, 'name': 'Каширская'},
    171: {'line': 11, 'name': 'Варшавская'},
    172: {'line': 11, 'name': 'Каховская'},
    173: {'line': 12, 'name': 'Улица Старокачаловская'},
    174: {'line': 12, 'name': 'Улица Скобелевская'},
    175: {'line': 12, 'name': 'Бульвар Адмирала Ушакова'},
    176: {'line': 12, 'name': 'Улица Горчакова'},
    177: {'line': 12, 'name': 'Бунинская аллея'},
    178: {'line': 3, 'name': 'Мякинино'},
    179: {'line': 3, 'name': 'Волоколамская'},
    180: {'line': 3, 'name': 'Митино'},
    181: {'line': 10, 'name': 'Марьина Роща'},
    182: {'line': 10, 'name': 'Достоевская'},
    183: {'line': 10, 'name': 'Борисово'},
    184: {'line': 10, 'name': 'Шипиловская'},
    185: {'line': 10, 'name': 'Зябликово'},
    186: {'line': 8, 'name': 'Новокосино'},
    187: {'line': 2, 'name': 'Алма-Атинская'},
    188: {'line': 3, 'name': 'Пятницкое шоссе'},
    189: {'line': 7, 'name': 'Лермонтовский проспект'},
    190: {'line': 7, 'name': 'Жулебино'},
    191: {'line': 12, 'name': 'Битцевский парк'},
    192: {'line': 12, 'name': 'Лесопарковая'},
    193: {'line': 8, 'name': 'Шелепиха'},
    194: {'line': 8, 'name': 'Парк Победы'},
    195: {'line': 7, 'name': 'Спартак'},
    196: {'line': 1, 'name': 'Тропарёво'},
    197: {'line': 7, 'name': 'Котельники'},
    198: {'line': 2, 'name': 'Технопарк'},
    199: {'line': 1, 'name': 'Румянцево'},
    200: {'line': 1, 'name': 'Саларьево'},
    201: {'line': 14, 'name': 'Ботанический сад'},
    202: {'line': 14, 'name': 'Владыкино'},
    203: {'line': 14, 'name': 'Окружная'},
    204: {'line': 14, 'name': 'Лихоборы'},
    205: {'line': 14, 'name': 'Коптево'},
    206: {'line': 14, 'name': 'Балтийская'},
    207: {'line': 14, 'name': 'Стрешнево'},
    208: {'line': 14, 'name': 'Панфиловская'},
    209: {'line': 14, 'name': 'Зорге'},
    210: {'line': 14, 'name': 'Хорошёво'},
    211: {'line': 14, 'name': 'Шелепиха'},
    212: {'line': 14, 'name': 'Деловой центр'},
    213: {'line': 14, 'name': 'Кутузовская'},
    214: {'line': 14, 'name': 'Лужники'},
    215: {'line': 14, 'name': 'Площадь Гагарина'},
    216: {'line': 14, 'name': 'Крымская'},
    217: {'line': 14, 'name': 'Верхние Котлы'},
    218: {'line': 14, 'name': 'ЗИЛ'},
    219: {'line': 14, 'name': 'Автозаводская'},
    220: {'line': 14, 'name': 'Дубровка'},
    221: {'line': 14, 'name': 'Угрешская'},
    222: {'line': 14, 'name': 'Новохохловская'},
    223: {'line': 14, 'name': 'Нижегородская'},
    224: {'line': 14, 'name': 'Андроновка'},
    225: {'line': 14, 'name': 'Шоссе Энтузиастов'},
    226: {'line': 14, 'name': 'Соколиная гора'},
    227: {'line': 14, 'name': 'Измайлово'},
    228: {'line': 14, 'name': 'Локомотив'},
    229: {'line': 14, 'name': 'Бульвар Рокоссовского'},
    230: {'line': 14, 'name': 'Белокаменная'},
    231: {'line': 14, 'name': 'Ростокино'},
    232: {'line': 10, 'name': 'Бутырская'},
    233: {'line': 10, 'name': 'Фонвизинская'},
    234: {'line': 10, 'name': 'Петровско-Разумовская'},
    235: {'line': 8, 'name': 'Минская'},
    236: {'line': 8, 'name': 'Ломоносовский проспект'},
    237: {'line': 8, 'name': 'Раменки'},
    238: {'line': 15, 'name': 'Деловой центр'},
    239: {'line': 15, 'name': 'Шелепиха'},
    240: {'line': 15, 'name': 'Хорошёвская'},
    241: {'line': 15, 'name': 'ЦСКА'},
    242: {'line': 15, 'name': 'Петровский парк'},
    243: {'line': 8, 'name': 'Хорошёвская'},
    244: {'line': 8, 'name': 'ЦСКА'},
    245: {'line': 8, 'name': 'Петровский парк'},
    246: {'line': 2, 'name': 'Ховрино'},
    247: {'line': 10, 'name': 'Окружная'},
    248: {'line': 10, 'name': 'Верхние Лихоборы'},
    249: {'line': 10, 'name': 'Селигерская'}
}


LINKS = [
    # List of connections between stations
    # (source, target, time)
    (1, 2, {'time': 190}),
    (1, 229, {'time': 541}),
    (2, 3, {'time': 145}),
    (2, 228, {'time': 300}),
    (3, 4, {'time': 200}),
    (4, 5, {'time': 135}),
    (5, 6, {'time': 115}),
    (6, 7, {'time': 110}),
    (6, 77, {'time': 360}),
    (7, 8, {'time': 100}),
    (8, 9, {'time': 115}),
    (8, 92, {'time': 180}),
    (8, 159, {'time': 180}),
    (9, 10, {'time': 100}),
    (9, 117, {'time': 180}),
    (10, 11, {'time': 105}),
    (10, 29, {'time': 240}),
    (11, 12, {'time': 115}),
    (11, 49, {'time': 300}),
    (11, 68, {'time': 180}),
    (11, 144, {'time': 360}),
    (12, 13, {'time': 130}),
    (13, 14, {'time': 150}),
    (13, 71, {'time': 300}),
    (14, 15, {'time': 95}),
    (15, 16, {'time': 185}),
    (15, 214, {'time': 360}),
    (16, 17, {'time': 225}),
    (17, 18, {'time': 180}),
    (18, 19, {'time': 170}),
    (19, 196, {'time': 170}),
    (20, 21, {'time': 155}),
    (20, 246, {'time': 240}),
    (21, 22, {'time': 180}),
    (22, 23, {'time': 170}),
    (22, 206, {'time': 780}),
    (23, 24, {'time': 130}),
    (24, 25, {'time': 170}),
    (25, 26, {'time': 180}),
    (25, 242, {'time': 360}),
    (25, 245, {'time': 360}),
    (26, 27, {'time': 110}),
    (26, 80, {'time': 180}),
    (27, 28, {'time': 100}),
    (28, 29, {'time': 100}),
    (28, 116, {'time': 180}),
    (28, 143, {'time': 240}),
    (29, 30, {'time': 160}),
    (29, 48, {'time': 300}),
    (30, 31, {'time': 140}),
    (30, 94, {'time': 180}),
    (30, 132, {'time': 180}),
    (31, 32, {'time': 180}),
    (31, 74, {'time': 240}),
    (32, 198, {'time': 140}),
    (32, 219, {'time': 600}),
    (33, 34, {'time': 200}),
    (34, 35, {'time': 205}),
    (34, 170, {'time': 180}),
    (35, 36, {'time': 145}),
    (36, 37, {'time': 165}),
    (37, 38, {'time': 145}),
    (38, 39, {'time': 150}),
    (39, 185, {'time': 150}),
    (39, 187, {'time': 250}),
    (40, 41, {'time': 135}),
    (41, 42, {'time': 170}),
    (42, 43, {'time': 190}),
    (43, 44, {'time': 165}),
    (43, 227, {'time': 540}),
    (44, 45, {'time': 110}),
    (45, 46, {'time': 145}),
    (46, 47, {'time': 175}),
    (47, 48, {'time': 185}),
    (47, 76, {'time': 240}),
    (47, 160, {'time': 180}),
    (48, 49, {'time': 125}),
    (49, 50, {'time': 140}),
    (49, 68, {'time': 180}),
    (49, 144, {'time': 180}),
    (50, 51, {'time': 105}),
    (51, 52, {'time': 270}),
    (51, 65, {'time': 240}),
    (51, 82, {'time': 180}),
    (52, 53, {'time': 260}),
    (52, 194, {'time': 120}),
    (53, 54, {'time': 170}),
    (54, 55, {'time': 180}),
    (54, 58, {'time': 180}),
    (55, 56, {'time': 195}),
    (56, 57, {'time': 420}),
    (57, 178, {'time': 205}),
    (58, 59, {'time': 130}),
    (59, 60, {'time': 115}),
    (60, 61, {'time': 115}),
    (61, 62, {'time': 140}),
    (62, 63, {'time': 145}),
    (63, 64, {'time': 120}),
    (63, 213, {'time': 360}),
    (64, 65, {'time': 140}),
    (65, 66, {'time': 130}),
    (65, 69, {'time': 395}),
    (65, 82, {'time': 360}),
    (66, 67, {'time': 115}),
    (67, 68, {'time': 65}),
    (69, 70, {'time': 120}),
    (69, 238, {'time': 180}),
    (70, 212, {'time': 360}),
    (71, 72, {'time': 120}),
    (72, 73, {'time': 105}),
    (72, 95, {'time': 180}),
    (73, 74, {'time': 115}),
    (73, 146, {'time': 180}),
    (74, 75, {'time': 135}),
    (75, 76, {'time': 170}),
    (75, 119, {'time': 180}),
    (75, 131, {'time': 180}),
    (76, 77, {'time': 175}),
    (76, 160, {'time': 360}),
    (77, 78, {'time': 160}),
    (78, 79, {'time': 160}),
    (78, 90, {'time': 180}),
    (79, 80, {'time': 135}),
    (79, 141, {'time': 180}),
    (80, 81, {'time': 165}),
    (81, 82, {'time': 160}),
    (81, 115, {'time': 180}),
    (82, 71, {'time': 175}),
    (83, 84, {'time': 160}),
    (84, 85, {'time': 140}),
    (85, 86, {'time': 135}),
    (86, 87, {'time': 210}),
    (86, 201, {'time': 240}),
    (87, 88, {'time': 135}),
    (88, 89, {'time': 140}),
    (89, 90, {'time': 130}),
    (90, 91, {'time': 120}),
    (91, 92, {'time': 100}),
    (92, 93, {'time': 125}),
    (92, 159, {'time': 180}),
    (93, 94, {'time': 170}),
    (93, 118, {'time': 120}),
    (94, 95, {'time': 155}),
    (94, 132, {'time': 120}),
    (95, 96, {'time': 130}),
    (96, 97, {'time': 190}),
    (97, 98, {'time': 185}),
    (97, 215, {'time': 180}),
    (98, 99, {'time': 120}),
    (99, 100, {'time': 100}),
    (100, 101, {'time': 140}),
    (101, 102, {'time': 170}),
    (102, 103, {'time': 115}),
    (103, 104, {'time': 150}),
    (104, 105, {'time': 170}),
    (105, 106, {'time': 140}),
    (106, 191, {'time': 120}),
    (107, 108, {'time': 110}),
    (108, 109, {'time': 175}),
    (109, 195, {'time': 100}),
    (110, 111, {'time': 185}),
    (111, 112, {'time': 200}),
    (111, 208, {'time': 720}),
    (112, 113, {'time': 150}),
    (112, 210, {'time': 720}),
    (112, 240, {'time': 180}),
    (112, 243, {'time': 180}),
    (113, 114, {'time': 130}),
    (114, 115, {'time': 125}),
    (115, 116, {'time': 165}),
    (116, 117, {'time': 120}),
    (116, 143, {'time': 240}),
    (117, 118, {'time': 90}),
    (118, 119, {'time': 170}),
    (119, 120, {'time': 145}),
    (119, 131, {'time': 240}),
    (120, 121, {'time': 150}),
    (120, 162, {'time': 300}),
    (121, 122, {'time': 245}),
    (122, 123, {'time': 185}),
    (123, 124, {'time': 185}),
    (124, 125, {'time': 170}),
    (125, 189, {'time': 240}),
    (126, 127, {'time': 150}),
    (127, 128, {'time': 195}),
    (128, 129, {'time': 150}),
    (128, 225, {'time': 600}),
    (129, 130, {'time': 180}),
    (130, 131, {'time': 175}),
    (130, 161, {'time': 180}),
    (131, 132, {'time': 160}),
    (133, 134, {'time': 150}),
    (134, 135, {'time': 195}),
    (135, 136, {'time': 165}),
    (136, 137, {'time': 145}),
    (136, 202, {'time': 420}),
    (137, 138, {'time': 200}),
    (138, 139, {'time': 110}),
    (139, 140, {'time': 120}),
    (140, 141, {'time': 120}),
    (141, 142, {'time': 160}),
    (142, 143, {'time': 110}),
    (142, 158, {'time': 180}),
    (143, 144, {'time': 150}),
    (144, 145, {'time': 145}),
    (145, 146, {'time': 120}),
    (146, 147, {'time': 205}),
    (147, 148, {'time': 225}),
    (148, 149, {'time': 120}),
    (148, 217, {'time': 720}),
    (149, 150, {'time': 100}),
    (150, 151, {'time': 110}),
    (151, 152, {'time': 125}),
    (151, 172, {'time': 240}),
    (152, 153, {'time': 190}),
    (153, 154, {'time': 110}),
    (154, 155, {'time': 150}),
    (155, 156, {'time': 115}),
    (156, 157, {'time': 160}),
    (157, 173, {'time': 120}),
    (158, 159, {'time': 160}),
    (159, 160, {'time': 160}),
    (160, 161, {'time': 175}),
    (161, 162, {'time': 165}),
    (162, 163, {'time': 145}),
    (163, 164, {'time': 130}),
    (163, 220, {'time': 780}),
    (164, 165, {'time': 240}),
    (165, 166, {'time': 160}),
    (166, 167, {'time': 170}),
    (167, 168, {'time': 185}),
    (168, 169, {'time': 140}),
    (169, 183, {'time': 150}),
    (170, 171, {'time': 175}),
    (171, 172, {'time': 125}),
    (173, 174, {'time': 295}),
    (174, 175, {'time': 80}),
    (175, 176, {'time': 105}),
    (176, 177, {'time': 115}),
    (178, 179, {'time': 180}),
    (179, 180, {'time': 170}),
    (180, 188, {'time': 120}),
    (181, 182, {'time': 150}),
    (181, 232, {'time': 205}),
    (182, 158, {'time': 150}),
    (183, 184, {'time': 130}),
    (184, 185, {'time': 110}),
    (186, 126, {'time': 200}),
    (189, 190, {'time': 180}),
    (190, 197, {'time': 120}),
    (191, 192, {'time': 180}),
    (192, 173, {'time': 180}),
    (193, 194, {'time': 310}),
    (193, 211, {'time': 180}),
    (193, 239, {'time': 27}),
    (194, 235, {'time': 180}),
    (195, 110, {'time': 185}),
    (196, 199, {'time': 180}),
    (198, 33,  {'time': 140}),
    (199, 200, {'time': 145}),
    (201, 202, {'time': 290}),
    (202, 203, {'time': 170}),
    (203, 204, {'time': 180}),
    (204, 205, {'time': 210}),
    (205, 206, {'time': 265}),
    (206, 207, {'time': 180}),
    (207, 208, {'time': 180}),
    (208, 209, {'time': 160}),
    (209, 210, {'time': 160}),
    (210, 211, {'time': 225}),
    (210, 240, {'time': 720}),
    (210, 243, {'time': 720}),
    (211, 212, {'time': 150}),
    (211, 239, {'time': 180}),
    (212, 213, {'time': 150}),
    (213, 214, {'time': 220}),
    (214, 215, {'time': 240}),
    (215, 216, {'time': 230}),
    (216, 217, {'time': 140}),
    (217, 218, {'time': 200}),
    (218, 219, {'time': 150}),
    (219, 220, {'time': 150}),
    (220, 221, {'time': 155}),
    (221, 222, {'time': 170}),
    (222, 223, {'time': 165}),
    (223, 224, {'time': 210}),
    (224, 225, {'time': 160}),
    (225, 226, {'time': 170}),
    (226, 227, {'time': 190}),
    (227, 228, {'time': 175}),
    (228, 229, {'time': 180}),
    (229, 230, {'time': 195}),
    (230, 231, {'time': 210}),
    (231, 201, {'time': 180}),
    (232, 233, {'time': 150}),
    (233, 234, {'time': 180}),
    (234, 137, {'time': 60}),
    (234, 247, {'time': 120}),
    (235, 236, {'time': 240}),
    (236, 237, {'time': 120}),
    (238, 239, {'time': 180}),
    (239, 240, {'time': 230}),
    (240, 241, {'time': 120}),
    (241, 242, {'time': 140}),
    (241, 244, {'time': 29}),
    (242, 245, {'time': 27}),
    (243, 193, {'time': 230}),
    (243, 240, {'time': 29}),
    (243, 244, {'time': 120}),
    (244, 245, {'time': 140}),
    (247, 203, {'time': 480}),
    (247, 248, {'time': 120}),
    (248, 249, {'time': 180})
]


COLORS = {
    1: '#D92B2C',
    2: '#44B85C',
    3: '#0078BF',
    4: '#19C1F3',
    5: '#894E35',
    6: '#F58631',
    7: '#8E479C',
    8: '#FFCB31',
    9: '#A1A2A3',
    10: '#B3D445',
    11: '#79CDCD',
    12: '#B0BFE7',
    13: '#2C75C4',
    14: '#FFA8AF',
    15: '#5BBEBB'
}


