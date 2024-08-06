import os
from cumulusci.core.tasks import BaseTask, CCIOptions
from cumulusci.utils.options import Field

class SetEnvVars(BaseTask):
    class Options(CCIOptions):
        name: str = Field(..., description="The name of the experience site")
        url_prefix: str = Field(..., description="The prefix of the experience site")
        template: str = Field(..., description="The template file to use")

    parsed_options: Options

    def _run_task(self):
        os.environ['EXPERIENCE_SITE_NAME'] = self.parsed_options.name
        os.environ['EXPERIENCE_SITE_PREFIX'] = self.parsed_options.url_prefix
        os.environ['EXPERIENCE_SITE_TEMPLATE'] = self.parsed_options.template
        self._set_return_values()
        self.logger.info(f"Set EXPERIENCE_SITE_NAME to {self.parsed_options.name}")
        self.logger.info(f"Set EXPERIENCE_SITE_PREFIX to {self.parsed_options.url_prefix}")
        self.logger.info(f"Set EXPERIENCE_SITE_TEMPLATE to {self.parsed_options.template}")
        
    def _set_return_values(self):
        self.return_values = {
            "name": self.parsed_options.name,
            "url_prefix": self.parsed_options.url_prefix,
            "template": self.parsed_options.template,
        }