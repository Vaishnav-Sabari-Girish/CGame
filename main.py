from typing import ClassVar, cast, override

from textual.app import App, ComposeResult
from textual.binding import BindingType
from textual.reactive import reactive
from textual.widgets import Static

# Import our custom state handlers
from state import load_state, save_state

# MAP_WIDTH: int = 20
# MAP_HEIGHT: int = 10

class GameMap(Static):
    # 1. State mgmt : Reactives handle automatic UI updates
    player_x: reactive[int] = reactive(0)
    player_y: reactive[int] = reactive(0)

    def on_mount(self) -> None:
        """Called automatically when the widget is added to the screen."""
        # cast self.app to App[None]
        app_instance: App[None] = cast(App[None], self.app)
        term_width: int = app_instance.console.size.width
        term_height: int = app_instance.console.size.height

        saved_x, saved_y = load_state(term_width // 2, term_height // 2)
        self.player_x = saved_x
        self.player_y = saved_y

    @override
    def render(self) -> str:
        width: int = self.size.width
        height: int = self.size.height

        lines: list[str] = []

        for y in range(height) :
            row: str = ""
            for x in range(width) :
                if x == self.player_x and y == self.player_y :
                    row += "P"
                else :
                    row += "."
            lines.append(row)

        return "\n".join(lines)

class GameApp(App[None]) :
    # Map should stretch across the whole terminal
    CSS: ClassVar[str] = """
    GameMap {
        width: 100%;
        height: 100%;
    }
    """
    BINDINGS: ClassVar[list[BindingType]] = [
        ("q", "quit", "Quit"),
        ("w", "move_up", "Up"),
        ("s", "move_down", "Down"),
        ("a", "move_left", "Left"),
        ("d", "move_right", "Right"),
    ]

    @override
    def compose(self) -> ComposeResult :
        yield GameMap()

    def action_move_up(self) -> None:
        game_map = self.query_one(GameMap)
        if game_map.player_y > 0:
            game_map.player_y -= 1
            save_state(game_map.player_x, game_map.player_y)

    def action_move_down(self) -> None: 
        game_map = self.query_one(GameMap)
        if game_map.player_y < game_map.size.height - 1 :
            game_map.player_y += 1
            save_state(game_map.player_x, game_map.player_y)

    def action_move_left(self) -> None: 
        game_map = self.query_one(GameMap)
        if game_map.player_x > 0 :
            game_map.player_x -= 1
            save_state(game_map.player_x, game_map.player_y)

    def action_move_right(self) -> None: 
        game_map = self.query_one(GameMap)
        if game_map.player_x < game_map.size.width - 1 :
            game_map.player_x += 1
            save_state(game_map.player_x, game_map.player_y)


if __name__ == "__main__" :
    app = GameApp()
    _ = app.run()
