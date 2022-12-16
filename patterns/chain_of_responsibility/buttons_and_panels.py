from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional


class Handler(ABC):
    def __init__(self) -> None:
        self.next: Optional[Handler] = None

    def set_next(self, handler: Handler) -> None:
        self.next = handler

    def handle_click_event(self) -> None:
        if self.on_click() and self.next:
            self.next.handle_click_event()

    @abstractmethod
    def on_click(self) -> bool:
        """handle a click"""


class Button(Handler):
    def __init__(self, name: str = "button", disabled: bool = False) -> None:
        super().__init__()
        self.name = name
        self.disabled = disabled

    def on_click(self) -> bool:
        if self.disabled:
            return True
        print(f"Button {self.name} was clicked.")
        return False


class Panel(Handler):
    def __init__(self, name: str = "panel", disabled: bool = False) -> None:
        super().__init__()
        self.name = name
        self.disabled = disabled

    def on_click(self) -> bool:
        if self.disabled:
            return True
        print(f"panel {self.name} was clicked.")
        return False


class Window(Handler):
    def __init__(self, name: str = "window", disabled: bool = False) -> None:
        super().__init__()
        self.name = name
        self.disabled = disabled

    def on_click(self) -> bool:
        if self.disabled:
            return True
        print(f"window {self.name} was clicked.")
        return False


def main() -> None:
    button = Button()
    panel = Panel()
    window = Window()

    button.set_next(panel)
    panel.set_next(window)

    button.handle_click_event()

    button.disabled = True
    button.handle_click_event()

    button.disabled = True
    panel.disabled = True
    button.handle_click_event()


if __name__ == "__main__":
    main()
