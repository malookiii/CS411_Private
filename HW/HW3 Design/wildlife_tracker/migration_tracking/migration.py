from typing import Any

from wildlife_tracker.migration_tracking.migration_path import MigrationPath
class Migration:

    def _init_(self, migration_id: int, migration_path: MigrationPath, current_location: str , start_date: str, status: str = "Scheduled"):

        self.migration_id = migration_id
        self.migration_path = migration_path
        self.status = status
        self.current_location = current_location
        self.start_date = start_date
    
    def update_migration_details(migration_id: int, **kwargs: Any) -> None:
        pass
    def get_migration_details(migration_id: int) -> dict[str, Any]:
        pass