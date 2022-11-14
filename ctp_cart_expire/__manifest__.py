# -*- coding: utf-8 -*-
###################################################################################
#
#    Cybernetics Plus Co., Ltd.
#    Set Time Website Cart Expire
#
###################################################################################

{
    "name": "Cart Expire",
    "version": "14.0.0.1.1",
    "summary": """ 
            Set Time Website Cart Expire
            .""",
    "description": """ 
            Set Time Website Cart Expire
            .""",
    "author": "Cybernetics+",
    "website": "https://www.cybernetics.plus",
    "live_test_url": "https://www.cybernetics.plus",
    "images": ["static/description/banner.gif"],
    "category": "Website",
    "license": "AGPL-3",
    "installable": True,
    "application": True,
    "auto_install": False,
    "contributors": [
        "Developer <dev@cybernetics.plus>",
    ],
    "depends": [
        "website_sale",
    ],
    "data": [
        "data/ir_cron.xml",
        "views/res_config_settings.xml"
    ],
}