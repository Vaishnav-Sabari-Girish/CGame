from typing import List

from src.ProfileManager.profile_data import ProfileConfig


class ProfileManager:

    profiles : List[ProfileConfig]

    def __init__(self):
        init()

    @classmethod
    def init(cls):
        """Init the profiles"""
        if cls.profiles is None:
            cls.profiles = []

    @classmethod
    def add_profile(cls, profile: ProfileConfig) -> None:
        """Add profile to the singleton List"""
        cls.profiles.append(profile)

    @classmethod
    def remove_profile(cls, profile: ProfileConfig) -> None:
        """Remove profile from the singleton List if exists"""
        if not profile in cls.profiles:
            return
        cls.profiles.remove(profile)

    @classmethod
    def get_profiles(cls) -> List[ProfileConfig]: return cls.profiles

    @classmethod
    def profile_size(cls) -> int: return len(cls.profiles)

    @classmethod
    def profile_exists(cls, profile: ProfileConfig) -> bool: return profile in cls.profiles

    def load_profile(self, profile: ProfileConfig) -> None:
        ...

    def create_profile(self, profile: ProfileConfig) -> None:
        ...

    def delete_profile(self, profile: ProfileConfig) -> None:
        ...

    def create_backup(self, profile: ProfileConfig) -> None:
        ...
