# startUpManager

### Application providing support for adding applications to the autostart via windows registers
 
##### Available options:

- ShowOne 

- ShowAll

- PossibleKeys

- ExistingKeys

- Add

- Delete

### Building

1. Go to the repository folder and create a new virtual environment
        
        >>> cd path\to\repository
        >>> python -mvenv venv
2. Activate the environment
        
        >>> venv\Scripts\activate.bat
        
3. Install packages from requirements.txt file
        
        >>> pip install -r requirements.txt
        
4. Build your application

        >>> pyinstaller -F --specpath=./startUpManager/build --workpath=./startUpManager/build --distpath=. startUpManager.py