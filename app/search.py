from flask import current_app


def add_to_index(index, model):
    if not current_app.elasticsearch:
        print("Elasticsearch is not configured.")
        return
    try:
        payload = {field: getattr(model, field) for field in model.__searchable__}
        current_app.elasticsearch.index(index=index, id=model.id, document=payload)
    except Exception as e:
        print(f"Error indexing document: {e}")


def remove_from_index(index, model):
    if not current_app.elasticsearch:
        return
    try:
        current_app.elasticsearch.delete(index=index, id=model.id)
    except Exception as e:
        print(f"Error removing document from index: {e}")


def query_index(index, query, page, per_page, fields=None):
    if not current_app.elasticsearch:
        print("Elasticsearch is not configured.")
        return [], 0
    fields = fields or ['*']  # Default to all fields if none are provided

    search_body = {
        "query": {
        "bool": {
            "should": [
                {"multi_match": {"query": query, "fields": fields, "fuzziness": "AUTO"}},
                {"wildcard": {"body": f"*{query}*"}}  # Wildcard search
            ]
        }
    },
        "from": (page - 1) * per_page,
        "size": per_page
    }

    search = current_app.elasticsearch.search(index=index, body=search_body)
    ids = [int(hit['_id']) for hit in search['hits']['hits']]
    return ids, search['hits']['total']['value']

    #search = current_app.elasticsearch.search(
        #index=index,
        #query={'multi_match': {'query': query, 'fields': fields}},
        #from_=(page - 1) * per_page,
        #size=per_page)
    #ids = [int(hit['_id']) for hit in search['hits']['hits']]
    #return ids, search['hits']['total']['value']


def reindex(model):
    from app.models import db
    if not current_app.elasticsearch:
        print("Elasticsearch is not configured.")
        return
    for obj in db.session.scalars(model.query):
        try:
            add_to_index(model.__tablename__, obj)
        except Exception as e:
            print(f"Error indexing document {obj.id}: {e}")
    print(f"Reindexed all objects for {model.__tablename__}.")


