# src/shared/domain/aggregate_root.py
from abc import ABC, abstractmethod
from typing import List, Any


class AggregateRoot(ABC):
    _events: List[Any] = []

    def add_event(self, event: Any) -> None:
        self._events.append(event)

    def get_events(self) -> List[Any]:
        return self._events.copy()

    def clear_events(self) -> None:
        self._events.clear()
