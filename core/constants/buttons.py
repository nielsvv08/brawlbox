class ButtonsConstants:
    confirm_stop = {
        "components": [
            {
                "type": 1,
                "components": [
                    {
                        "type": 2,
                        "label": "✅",
                        "style": 1,
                        "disabled": True,
                        "custom_id": "confirm_timeout_check",
                    },
                    {
                        "type": 2,
                        "label": "❌",
                        "style": 4,
                        "disabled": True,
                        "custom_id": "confirm_timeout_cross",
                    },
                ],
            }
        ],
    }

    paginate_stop = {
        "components": [
            {
                "type": 1,
                "components": [
                    {
                        "type": 2,
                        "label": "⬅️",
                        "style": 1,
                        "disabled": True,
                        "custom_id": "paginate_timeout_previous",
                    },
                    {
                        "type": 2,
                        "label": "➡️",
                        "style": 1,
                        "disabled": True,
                        "custom_id": "paginate_timeout_next",
                    },
                    {
                        "type": 2,
                        "label": "❌",
                        "style": 4,
                        "disabled": True,
                        "custom_id": "paginate_timeout_cross",
                    },
                ],
            }
        ],
    }

    prestige_confirm = {
        "components": [
            {
                "type": 1,
                "components": [
                    {
                        "type": 2,
                        "label": "✅",
                        "style": 1,
                        "custom_id": "prestige_confirm",
                    },
                ],
            }
        ],
    }
