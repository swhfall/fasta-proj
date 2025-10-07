# FASTA Tools 🧬
Python библиотека для работы с биологическими последовательностями и FASTA файлами.
## Установка и запуск
**Клонируйте репозиторий:**
git clone https://github.com/swhfall/fasta-proj

Перейдите в папку проекта: cd fasta-proj

Установите пакет: pip install -e .

Запустите демо-программу: python examples/demo.py

# Описание классов
## Класс Seq

Работа с биологическими последовательностями

Хранение заголовка и последовательности

Определение алфавита (белковый/нуклеотидный)

FASTA форматирование вывода

## Класс FastaReader

Чтение FASTA файлов

Проверка формата файла

Поддержка больших файлов через итераторы

Пакетное чтение последовательностей
## Документация
HTML документация доступна в папке html_docs/:

html_docs/fasta.html - документация всего пакета

html_docs/fasta.seq.html - документация класса Seq

html_docs/fasta.fasta_reader.html - документация класса FastaReader
## Структура проекта

fasta-proj/
├── fasta/                 
│   ├── __init__.py
│   ├── seq.py           
│   └── fasta_reader.py  
├── examples/             
│   ├── demo.py         
│   ├── GCA_000006945.2_ASM694v2_genomic.fna  
│   └── protein.faa       
├── html_docs/            
├── setup.py              
└── README.md             
