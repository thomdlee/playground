from dataclasses import dataclass
from diator.events import Event
from diator.requests import Request, RequestHandler


@dataclass(frozen=True, kw_only=True)
class HelloWorldCommand(Request):
    greeting: str


class HelloWorldCommandHandler(RequestHandler[HelloWorldCommand, str]):
    def __init__(self) -> None:
        self._events: list[Event] = []

    @property
    def events(self) -> list[Event]:
        return self._events

    async def handle(self, request: HelloWorldCommand) -> str:
        return "Hello world using CQRS! Plus a greeting" + request.greeting
