import os
from cumulusci.core.tasks import BaseTask, CCIOptions
from cumulusci.utils.options import Field

class SetEnvVars(BaseTask):
    class Options(CCIOptions):
        env_vars: list = Field(..., description="A list of key-value pairs for environment variables")

    parsed_options: Options

    def _run_task(self):
        for env_var in self.parsed_options.env_vars:
            key = env_var.get('key')
            value = env_var.get('value')
            os.environ[key] = value
            self.logger.info(f"Set {key} environment variable to {value}")
