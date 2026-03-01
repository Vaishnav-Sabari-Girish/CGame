from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Union


@dataclass
class ProfileConfig:
    """Profile data class"""
    name: str
    sshKey: str
    createdAt: int
    lastModifiedAt: int
    profile_path: Path
    backup_path: Path
    is_active: bool
    latest_save_point: Path

    @classmethod
    def from_dict(cls, data: Dict[str, Union[str, int, Path, bool]]):
        """Constructor for ProfileConfig class"""
        return cls(
            name=data["name"],
            sshKey=data["sshKey"],
            createdAt=data["createdAt"],
            lastModifiedAt=data["lastModifiedAt"],
            profile_path=Path(data["profile_path"]),
            backup_path=Path(data["backup_path"]),
            is_active=data["is_active"],
            latest_save_point=Path(data["latest_save_point"])
        )
