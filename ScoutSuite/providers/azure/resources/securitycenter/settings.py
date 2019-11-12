from ScoutSuite.providers.azure.resources.base import AzureResources


class Settings(AzureResources):
    async def fetch_all(self):
        for raw_settings in await self.facade.securitycenter.get_information_protection_policies():
            id, settings = self._parse_settings(
                raw_settings)
            self[id] = settings

    def _parse_settings(self, settings):
        settings_dict = {}
        #auto_provisioning_setting_dict['id'] = auto_provisioning_settings.id

        return settings_dict['id'], settings_dict
