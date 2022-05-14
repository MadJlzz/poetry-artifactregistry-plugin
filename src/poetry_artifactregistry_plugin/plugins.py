from cleo.io.io import IO

from poetry.plugins.plugin import Plugin
from poetry.poetry import Poetry

from poetry_artifactregistry_plugin.gcloud import existing_gcloud, authenticate_gcloud

class ArtifactRegistryPlugin(Plugin):

    def activate(self, poetry: Poetry, io: IO):
        if not existing_gcloud():
            io.write_error_line(f'<comment>poetry-artifactregistry-plugin</comment> requires <b><error>gcloud</error></b> to be functionnal.')
            io.write_error_line('Please follow instructions at [<info>https://cloud.google.com/sdk/docs/install?hl=en</info>] to use this plugin.')
            return
        authenticate_gcloud(io)