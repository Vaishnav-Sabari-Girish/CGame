from pathlib import Path
from platformdirs import PlatformDirs



class DirectoryManager:

    def __init__(self, app_name : str = "CGAME") -> None:
        self.dirs = PlatformDirs(
            appname=app_name,
            appauthor="BITS-Rohit"
        )

        self.root_dir = Path(self.dirs.user_data_dir)
        self.log_dir = Path(self.dirs.user_log_dir)

