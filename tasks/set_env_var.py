import os
from cumulusci.core.tasks import BaseTask, CCIOptions
from cumulusci.utils.options import Field

class SetEnvVars(BaseTask):
    class Options(CCIOptions):
        name: str = Field(..., description="The name of the experience site")
        url_prefix: str = Field(..., description="The prefix of the experience site")

    parsed_options: Options

    def _run_task(self):
        os.environ['EXPERIENCE_SITE_NAME'] = self.parsed_options.name
        os.environ['EXPERIENCE_SITE_PREFIX'] = self.parsed_options.url_prefix
        self.logger.info(f"Set EXPERIENCE_SITE_NAME to {self.parsed_options.name}")
        self.logger.info(f"Set EXPERIENCE_SITE_PREFIX to {self.parsed_options.url_prefix}")
