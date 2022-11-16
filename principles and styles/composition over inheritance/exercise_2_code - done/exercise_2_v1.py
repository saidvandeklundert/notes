from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Div:
    parent: Div | None = None
    x: int = 0
    y: int = 0

    def compute_screen_position(self) -> tuple[int, int]:
        if not self.parent:
            return (self.x, self.y)
        parent_x, parent_y = self.parent.compute_screen_position()
        return (parent_x + self.x, parent_y + self.y)


@dataclass
class Button:
    parent: Div
    x: int
    y: int

    def click(self) -> None:
        print("Click!")


@dataclass
class Span:
    parent: Div
    x: int
    y: int
    text: str


def main() -> None:
    root = Div(None, 25, 25)
    button = Button(root, 0, 0)
    sub_div = Div(root, 100, 100)
    span = Span(sub_div, 40, 40, "Hello")
    button.click()
    print(sub_div.compute_screen_position())


if __name__ == "__main__":
    main()
