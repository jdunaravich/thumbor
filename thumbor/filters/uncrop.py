#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/thumbor/thumbor/wiki

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 globo.com timehome@corp.globo.com

from thumbor.filters import BaseFilter, filter_method


class Filter(BaseFilter):

    @filter_method(BaseFilter.Number, BaseFilter.Number,
                   BaseFilter.Number, BaseFilter.Number)
    def uncrop(self, top=0, right=0, bottom=0, left=0):
        if not any([padding for padding in (top, right, bottom, left)]):
            return
        self.engine.uncrop(top=top, right=right, bottom=bottom, left=left)
