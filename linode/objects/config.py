from .dbase import DerivedBase
from .base import Property

class Config(DerivedBase):
    api_endpoint="/linodes/{linode_id}/configs/{id}"
    derived_url_path="configs"
    parent_id_name="linode_id"

    properties = {
        "id": Property(identifier=True),
        "linode_id": Property(identifier=True),
        "helpers": Property(),#TODO: mutable=True),
        "created": Property(is_datetime=True),
        "root_device": Property(mutable=True),
        "kernel": Property(relationship=True, mutable=True),
        "disks": Property(),#TODO: mutable=True),
        "updated": Property(),
        "comments": Property(mutable=True),
        "label": Property(mutable=True),
        "kernel_params": Property(mutable=True),
    }

    def _populate(self, json):
        """
        Override popupate to map the disks more nicely
        """
        DerivedBase._populate(self, json)

        import linode.mappings as mapper

        for key in vars(self.disks):
            if self.disks.__getattribute__(key):
                self.disks.__setattr__(key,
                        mapper.make(self.disks.__getattribute__(key).id,
                        self._client, parent_id=self.linode_id))