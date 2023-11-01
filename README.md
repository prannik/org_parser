# org_parser

<hr>
Развертывание проекта:

```
$ mkdir 'name_directory_project' 
$ cd 'name_directory-project'
$ python3 -m venv venv
$ source venv/bin/activate
$ git init
$ git clone https://github.com/prannik/org_parser.git
// or
// git clone git@github.com:prannik/org_parser.git
$ cd org_parser
$ pip install -r requirements.txt
$ > .env
```
Последней командой мы создали файл '.env' для хранения переменных окружения. Запишите в ваши личный GOOGLE_API_KEY:

'''Файл заполняется без пробелов и ковычек'''
GOOGLE_API_KEY='your_api_key'

Далее:
```
$ cd scraper_github
$ scrapy crawl santaelene  -O jsonfile.json
```