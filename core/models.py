from django.db import models


# Create your models here.
class Proxy(models.Model):
    ip = models.CharField()
    port = models.IntegerField(blank=True, null=True)
    type = models.CharField()
    country = models.CharField(blank=True, null=True)
    provider = models.CharField(blank=True, null=True)
    continent = models.CharField(blank=True, null=True)
    isocode = models.CharField(blank=True, null=True)
    region = models.CharField(blank=True, null=True)
    regioncode = models.CharField(blank=True, null=True)
    city = models.CharField(blank=True, null=True)
    latitude = models.CharField(blank=True, null=True)
    longitude = models.CharField(blank=True, null=True)
    portPreferred = models.IntegerField(blank=True, null=True)
    registered_at = models.DateTimeField(auto_now=True)

    def to_dict_json(self):
        return dict(
            ip=self.ip,
            port=self.port if self.port else 80,
            type=self.type,
            country=self.country,
            provider=self.provider,
            continent=self.continent,
            isocode=self.isocode,
            region=self.region,
            regioncode=self.regioncode,
            city=self.city,
            latitude=self.latitude,
            longitude=self.longitude,
        )
