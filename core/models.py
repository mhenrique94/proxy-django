from django.db import models


# Create your models here.
class Proxy(models.Model):
    ip = models.CharField()
    port = int
    type = models.CharField()
    country = models.CharField(blank=True, null=True)
    provider = models.CharField(blank=True, null=True)
    continent = models.CharField(blank=True, null=True)
    isocode = models.CharField(blank=True, null=True)
    region = models.CharField(blank=True, null=True)
    regioncode = models.CharField(blank=True, null=True)
    city = models.CharField(blank=True, null=True)
    latitude = models.DecimalField(blank=True, null=True, max_digits=8, decimal_places=6)
    longitude = models.DecimalField(blank=True, max_digits=8, null=True, decimal_places=6)
    portPreferred = int

    def to_dict_json(self):
        return dict(
            ip=self.ip,
            port=self.port,
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
