from textual.app import App, ComposeResult
from textual.reactive import reactive
from textual.widgets import Static

MAP_WIDTH = 20
MAP_HEIGHT = 10

class GameMap(Static):
# 1. State mgmt : Reactives handle automatic UI updates
    player_x = reactive(MAP_WIDTH // 2)
    player_y = reactive(MAP_HEIGHT // 2)

    def render(self) -> str:
        lines = []
        for y in range(MAP_HEIGHT) :
            row = ""
            for x in range(MAP_WIDTH) :
                if x == self.player_x and y == self.player_y :
                    row += "P"
                else :
                    row += "."
            lines.append(row)

        return "\n".join(lines)

class GameApp(App) :
    BINDINGS = [
        ("q", "quit", "Quit"),
        ("w", "move_up", "Up"),
        ("s", "move_down", "Down"),
        ("a", "move_left", "Left"),
        ("d", "move_right", "Right"),
    ]

    def compose(self) -> ComposeResult :
        yield GameMap()

    def action_move_up(self) :
        game_map = self.query_one(GameMap)
        if game_map.player_y > 0:
            game_map.player_y -= 1

    def action_move_down(self): 
        game_map = self.query_one(GameMap)
        if game_map.player_y < MAP_HEIGHT - 1 :
            game_map.player_y += 1

    def action_move_left(self): 
        game_map = self.query_one(GameMap)
        if game_map.player_x > 0 :
            game_map.player_x -= 1

    def action_move_right(self): 
        game_map = self.query_one(GameMap)
        if game_map.player_x < MAP_WIDTH - 1 :
            game_map.player_x += 1


if __name__ == "__main__" :
    app = GameApp()
    app.run()
