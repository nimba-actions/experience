import os
from cumulusci.core.tasks import BaseTask, CCIOptions
from cumulusci.utils.options import Field

class SetEnvVars(BaseTask):
    class Options(CCIOptions):
        name: str = Field(..., description="The name of the experience site")
        path: str = Field(..., description="The path of the experience bundle and related metadata")
        url_prefix: str = Field(..., description="The prefix of the experience site")
        template: str = Field(..., description="The template file to use")

    parsed_options: Options

    def _run_task(self):
        os.environ['EXPERIENCE_SITE_NAME'] = self.parsed_options.name
        os.environ['EXPERIENCE_SITE_PATH'] = self.parsed_options.path
        os.environ['EXPERIENCE_SITE_PREFIX'] = self.parsed_options.url_prefix
        os.environ['EXPERIENCE_SITE_TEMPLATE'] = self.parsed_options.template
        self._set_return_values()
        self.logger.info(f"Set EXPERIENCE_SITE_NAME to {self.parsed_options.name}")
        self.logger.info(f"Set EXPERIENCE_SITE_PATH to {self.parsed_options.path}")
        self.logger.info(f"Set EXPERIENCE_SITE_PREFIX to {self.parsed_options.url_prefix}")
        self.logger.info(f"Set EXPERIENCE_SITE_TEMPLATE to {self.parsed_options.template}")
        
    def _set_return_values(self):
        self.return_values = {
            "EXPERIENCE_SITE_NAME": self.parsed_options.name,
            "EXPERIENCE_SITE_PREFIX": self.parsed_options.url_prefix,
            "EXPERIENCE_SITE_TEMPLATE": self.parsed_options.template,
            "EXPERIENCE_SITE_PATH": self.parsed_options.path,
        }