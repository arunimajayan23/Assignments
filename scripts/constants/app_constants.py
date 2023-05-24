class APIs:
    view_all_items_api = '/'
    create_api = '/show_details'
    add_api = '/add'
    update_api = '/update'
    delete_api = '/delete'
    sent_api = '/send email'
    total_amount = '/total_amount_collected'


class pipeline_aggregation:
    pipeline = [
        {
            '$group': {
                '_id': '$course',
                'count': {
                    '$sum': 1
                },
                'total': {
                    '$sum': '$course_fee'
                }
            }
        }
    ]
    pipeline_agg = [
        {
            '$group': {
                '_id': '$course',
                'count': {
                    '$sum': 1
                },
                'total': {
                    '$sum': '$course_fee'
                }
            }
        }, {
            '$group': {
                '_id': None,
                'total': {
                    '$sum': '$total'
                }
            }
        }
    ]


class DBConstants:
    DB_URI = 'mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23'
    DB_NAME = 'interns_b2_23'
    DB_COLLECTION = 'arunima_jayan'