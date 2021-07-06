# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸 (Blueking) available.
Copyright (C) 2017-2021 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at https://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
"""

from django.utils.translation import ugettext_lazy as _

from ..base import DataAPI
from ..domains import USER_MANAGE_APIGATEWAY_ROOT


class _UserManageApi(object):
    MODULE = _("用户管理模块")

    def __init__(self):
        self.list_users = DataAPI(
            method="GET",
            url=USER_MANAGE_APIGATEWAY_ROOT + "list_users/",
            module=self.MODULE,
            description="获取所有用户",
            cache_time=300,
        )
        self.retrieve_user = DataAPI(
            method="GET", url=USER_MANAGE_APIGATEWAY_ROOT + "retrieve_user/", module=self.MODULE, description="获取单个用户",
        )
