### Simple Cmake Project

В этом туториале я собрал тестовый проект и запустил его. Шаги:

1) Сгенерировал профиль по-умолчанию с помощью команды `conan profile detect --force`
2) Нашёл профиль в ФС с помощью команды `conan profile path default`
3) Модифицировал найденный профиль `$HOME/.conan2/profiles/default`:
   - `tools.build:compiler_executables`
   - `compiler.version`
   - `compiler.cppstd`
   - `compiler=clang`
4) Создал python venv и установил библиотеку conan для написания рецептов на python:
   - `python3 -m venv ./.env`
   - `source .env/bin/activate`
   - `python3 -m pip install conan`
5) Заменил `conanfile.txt` на `conanfile.py`
6) Установил зависимости командой `conan install . --output-folder=./.build --build=missing`
7) Сгенерировал `Makefile` командой `cd .build; cmake .. --preset conan-release`
8) Запустил `make`
9) Запустил бинарь `compressor`

> **_NOTE:_** Также вместо 4го шага можно использовать в качестве python-интерпретатора 
`/opt/homebrew/Cellar/conan/2.12.0/libexec/bin/python3.13`


### Using build tools as Conan packages

В этом примере conan позволяет выбирать версию инструментов сборки, таких как CMake.

1) Добавил в `conanfile.py` `tool_requires = ["cmake/3.31.3"]`, чтобы использовать конкретную версию CMake при сборке этого проекта
2) Установил зависимости командой: `conan install . --output-folder=./.build --build=missing`
3) Активировал виртуальное окружение командой `source .build/conanbuild.sh`
4) Вызвал команду `cmake` и получил информацию о том, что правда используется `cmake/3.31/3`. 
   Это видно при генерации `Makefile`, так как в `CMakeLists.txt` добавили строку `message("Building with CMake version: ${CMAKE_VERSION}")`
5) Деактивировал виртуальное окружение командой `source .build/deactivate_conanbuild.sh`

> **_NOTE:_**  `tools_requires` стоит использовать для запускаемых приложений, не нужно использовать его для библиотек или подобных им зависимостей