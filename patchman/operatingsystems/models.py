# Copyright 2012 VPAC, http://www.vpac.org
# Copyright 2013-2016 Marcus Furlong <furlongm@gmail.com>
#
# This file is part of Patchman.
#
# Patchman is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 only.
#
# Patchman is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Patchman. If not, see <http://www.gnu.org/licenses/>

from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.db import models

from patchman.repos.models import Repository


@python_2_unicode_compatible
class OSGroup(models.Model):

    name = models.CharField(max_length=255, unique=True)
    repos = models.ManyToManyField(Repository, blank=True)

    class Meta(object):
        verbose_name = 'Operating System Group'
        verbose_name_plural = 'Operating System Groups'

    def __str__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('osgroup_detail', [self.id])


@python_2_unicode_compatible
class OS(models.Model):

    name = models.CharField(max_length=255, unique=True)
    osgroup = models.ForeignKey(OSGroup, blank=True, null=True,
                                on_delete=models.SET_NULL)

    class Meta(object):
        verbose_name = 'Operating System'
        verbose_name_plural = 'Operating Systems'
        ordering = ('name',)

    def __str__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('os_detail', [self.id])
