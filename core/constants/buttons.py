class ButtonsConstants:
    box_confirm = {
        "components": [
            {
                "type": 1,
                "components": [
                    {
                        "type": 2,
                        "emoji": {"name": "✔️"},
                        "style": 3,
                        "custom_id": "box_confirm",
                    },
                ],
            }
        ],
    }
    bigbox_confirm = {
        "components": [
            {
                "type": 1,
                "components": [
                    {
                        "type": 2,
                        "emoji": {"name": "✔️"},
                        "style": 3,
                        "custom_id": "bigbox_confirm",
                    },
                ],
            }
        ],
    }
    megabox_confirm = {
        "components": [
            {
                "type": 1,
                "components": [
                    {
                        "type": 2,
                        "emoji": {"name": "✔️"},
                        "style": 3,
                        "custom_id": "megabox_confirm",
                    },
                ],
            }
        ],
    }

    confirm_stop = {
        "components": [
            {
                "type": 1,
                "components": [
                    {
                        "type": 2,
                        "emoji": {"name": "✔️"},
                        "style": 3,
                        "disabled": True,
                        "custom_id": "confirm_timeout_check",
                    },
                    {
                        "type": 2,
                        "emoji": {"name": "✖"},
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
                        "emoji": {"name": "⬅"},
                        "style": 1,
                        "disabled": True,
                        "custom_id": "paginate_timeout_previous",
                    },
                    {
                        "type": 2,
                        "emoji": {"name": "➡"},
                        "style": 1,
                        "disabled": True,
                        "custom_id": "paginate_timeout_next",
                    },
                    {
                        "type": 2,
                        "label": "✖",
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
                        "emoji": {"name": "✔️"},
                        "style": 3,
                        "custom_id": "prestige_confirm",
                    },
                ],
            }
        ],
    }
