# NTU_course_bot

## To run
### under python
1.  pip install -r requirements.txt
2.  python src/main.py

### under .exe
1. pip install -r requirements.txt
2. pyinstaller --noconfirm --onefile --windowed --add-data "c:\users\vigne\appdata\local\programs\python\python39\lib\site-packages;customtkinter/"  "src/main.py"
3. run main.exe located in ./dist/