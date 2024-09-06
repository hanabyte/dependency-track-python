# SPDX-License-Identifier: GPL-2.0+

from .exceptions import DependencyTrackApiError


class Bom:
    """Class dedicated to all "bom" related endpoints"""

    def upload_bom(
        self,
        bom_data,
        project_uuid=None,
        project_name=None,
        project_version=None,
        auto_create=False,
    ):
        """Upload a supported bill of material format document

        API Endpoint: POST /bom

        :return: UUID-Token
        :rtype: string
        :raises DependencyTrackApiError: if the REST call failed
        """
        multipart_form_data = {}
        multipart_form_data["bom"] = bom_data

        if project_uuid:
            multipart_form_data["project"] = project_uuid
        if project_name:
            multipart_form_data["projectName"] = project_name
        if project_version:
            multipart_form_data["projectVersion"] = project_version
        multipart_form_data["autoCreate"] = auto_create
        response = self.session.post(
            self.api + "/bom",
            params=self.paginated_param_payload,
            files=multipart_form_data,
        )
        if response.status_code == 200:
            return response.json()
        else:
            description = f"Unable to upload BOM file"
            raise DependencyTrackApiError(description, response)
