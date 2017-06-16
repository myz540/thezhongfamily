from django.db import models


# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=32)
    victory_points = models.IntegerField()
    brick = models.IntegerField()
    wood = models.IntegerField()
    wheat = models.IntegerField()
    sheep = models.IntegerField()
    stone = models.IntegerField()
    # roads, settlements, and cities are map via foreign keys from Edge and Vertex models

    def __unicode__(self):
        return u"%s with %d victory points" % (self.name, self.victory_points)


class Edge(models.Model):
    available = models.BooleanField()
    road = models.ForeignKey(Player, null=True)


class Vertex(models.Model):
    available = models.BooleanField()
    settlement = models.ForeignKey(Player, null=True)
    has_city = models.BooleanField()


class Tile(models.Model):
    resource_type = models.CharField(max_length=8)
    dice_value = models.IntegerField()
    has_robber = models.BooleanField(default=False)

    # many to many relationships do not get their own column but are given a separate table
    # each tile will have 6 edges and 6 vertices, each vertex will have 1 or more tiles associated with it
    # each edge will have 1 or 2 tiles associated with it
    edge = models.ManyToManyField(Edge)
    vertex = models.ManyToManyField(Vertex)

    def __unicode__(self):
        return u"A %s tile" % self.resource_type


class Resource(models.Model):
    brick = models.IntegerField()
    wood = models.IntegerField()
    wheat = models.IntegerField()
    sheep = models.IntegerField()
    stone = models.IntegerField()

