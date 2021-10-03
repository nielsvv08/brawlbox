class PaginateConstants:
    stop_embed = {
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
