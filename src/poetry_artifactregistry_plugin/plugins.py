from cleo.commands.command import Command
from poetry.plugins.application_plugin import ApplicationPlugin


class ArtifactRegistryCommand(Command):

    name = "artifactregistry"

    def handle(self) -> int:
        self.line("My command")

        return 0


def factory():
    return ArtifactRegistryCommand()


class ArtifactRegistryApplicationPlugin(ApplicationPlugin):
    def activate(self, application):
        application.command_loader.register_factory("artifactregistry", factory)